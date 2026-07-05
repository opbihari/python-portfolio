
def initialize_log_file():
    with open('server_logs.txt', 'w') as log_file:
        log_file.write('Server Log Initialized\n')
        log_file.write('Server log initiated.\n')
        log_file.write('10.0.0.5 - - [19/Apr/2026:13:45:27] "GET /index.html HTTP/1.1" 200\n')
        log_file.write('192.168.1.99 - - [19/Apr/2026:13:45:28] "POST /login.php HTTP/1.1" 401\n')
        log_file.write('10.0.0.5 - - [19/Apr/2026:13:45:28] "GET /images/logo.png HTTP/1.1" 200\n')
        log_file.write('10.0.0.5 - - [19/Apr/2026:13:45:29] "GET /admin.php HTTP/1.1" 403\n')
        log_file.write('172.16.0.2 - - [19/Apr/2026:13:45:30] "GET /index.html HTTP/1.1" 200\n')
        log_file.write('192.168.1.99 - - [19/Apr/2026:13:45:31] "POST /login.php HTTP/1.1" 401\n')
    return 'Log file initialized with sample entries.'

#custom log entries
def log_entry(input_string):
    with open('server_logs.txt', 'a') as log_file:
        log_file.write(input_string + '\n')
    return 'Log entry added.'

#view log file
def view_log_file():
    with open('server_logs.txt', 'r') as log_file:
        logs = log_file.read()
    return logs

#main function to initialize log file and add custom entries
def main():
    print(initialize_log_file())
    print(view_log_file())
    to_add_or_not = input('Do you want to add a custom log entry? (yes/no): ').lower()
    if to_add_or_not == 'yes':
        while True:
         custom_entry = input('Enter the log entry you want to add: or type "exit" to stop adding entries: ')
         if custom_entry.lower() == 'exit':
             break
         print(log_entry(custom_entry))
    print(view_log_file())

main()