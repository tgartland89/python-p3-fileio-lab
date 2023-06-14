def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)
# this clears FAILED module Test write_file() - FileNotFoundError: 
# [Errno 2] No such file or directory: '/tmp/pytest-of-tgart/pytest-0/test_write_file0/test_file.txt'

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)
# this cleared number 2
# FAILED module Test append_file() - AssertionError: 
# assert 'This is a test content.' == 'This is a te...nded content.'

def read_file(file_name):
    with open(f'{file_name}.txt') as f:
        return f.read()
# this cleared number 3
# # FAILED module Test read_file() - AssertionError: assert None == 'This is a test content.'