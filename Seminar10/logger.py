import file_lib as fl
import datetime as d

log_filename = 'log.txt'
header_str = 'date, time, user_id, operation, result\n'

if not fl.is_file_exist(log_filename):
    fl.update_txt(header_str, log_filename, 'w')

def add_log_entry(entry:str):
    fl.update_txt(entry, log_filename, 'a')
