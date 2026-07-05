from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import sys


def md_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    parts = [p.strip() for p in text.split('\n\n') if p.strip()]

    doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=72)
    styles = getSampleStyleSheet()
    # tweak body style for better leading
    styles['BodyText'].spaceAfter = 6
    story = []

    for p in parts:
        if p.startswith('Practice:') or p.startswith('Warm-up') or p.startswith('Two Sum II') or p.startswith('3Sum'):
            story.append(Paragraph(p, styles['Heading2']))
        elif p.startswith('Prompt:') or p.startswith('Hint:') or p.startswith('Hint A:') or p.startswith('Prompt A'):
            story.append(Paragraph('<b>' + p.replace('\n','<br/>') + '</b>', styles['BodyText']))
        else:
            story.append(Paragraph(p.replace('\n','<br/>'), styles['BodyText']))
        story.append(Spacer(1, 6))

    doc.build(story)


if __name__ == '__main__':
    md = sys.argv[1] if len(sys.argv) > 1 else 'g:/My Drive/Colab Notebooks/practice_two_sum_sheet.md'
    pdf = sys.argv[2] if len(sys.argv) > 2 else 'g:/My Drive/Colab Notebooks/practice_two_sum_sheet.pdf'
    md_to_pdf(md, pdf)
    print('Wrote', pdf)
