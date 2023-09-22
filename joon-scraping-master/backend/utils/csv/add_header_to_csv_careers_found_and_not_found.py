# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
# ------------------------ imports end ------------------------


# ------------------------ add_header_to_csv_careers_found_and_not_found_function function start ------------------------
def add_header_to_csv_careers_found_and_not_found_function(file_path, headers_arr):
  localhost_print_function(' ------------------------ add_header_to_csv_careers_found_and_not_found_function function start ------------------------ ')
  with open(file_path, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(headers_arr)
  localhost_print_function(' ------------------------ add_header_to_csv_careers_found_and_not_found_function function end ------------------------ ')
  return True
# ------------------------ add_header_to_csv_careers_found_and_not_found_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__main__':
#   add_header_to_csv_careers_found_and_not_found_function()
# ------------------------ call end ------------------------