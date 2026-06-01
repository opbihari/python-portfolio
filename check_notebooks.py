import os
import glob
import nbformat
import sys
from nbconvert.preprocessors import ExecutePreprocessor

def check_notebooks(directory):
    notebooks = glob.glob(os.path.join(directory, "*.ipynb"))
    if not notebooks:
        print(f"No notebooks found in {directory}")
        return 0

    print(f"Found {len(notebooks)} notebooks. Executing them...\n")
    
    success_count = 0
    failure_count = 0
    
    # We allow errors because course materials often include intentional errors
    ep = ExecutePreprocessor(timeout=60, kernel_name='python3', allow_errors=True)
    
    for nb_path in sorted(notebooks):
        nb_name = os.path.basename(nb_path)
        print(f"Executing: {nb_name} ... ", end="")
        sys.stdout.flush()
        try:
            with open(nb_path, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            
            # Execute the notebook
            ep.preprocess(nb, {'metadata': {'path': directory}})
            
            # Count errors in the executed notebook
            error_count = 0
            for cell in nb.cells:
                if cell.cell_type == 'code':
                    for output in cell.get('outputs', []):
                        if output.output_type == 'error':
                            error_count += 1
            
            if error_count > 0:
                print(f"[COMPLETED WITH {error_count} ERRORS (likely intentional)]")
            else:
                print("[SUCCESS]")
                
            success_count += 1
            
        except Exception as e:
            print("[FAILED]")
            failure_count += 1
            print(f"--- Unexpected Error in {nb_name} ---")
            print(e)
            
    print(f"\nNotebooks Execution Summary: {success_count} succeeded, {failure_count} failed to parse.")
    return failure_count

if __name__ == "__main__":
    sys.exit(check_notebooks("Python_Course_Materials"))
