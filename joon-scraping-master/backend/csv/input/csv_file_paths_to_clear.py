# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
# ------------------------ imports end ------------------------


# ------------------------ csv_file_paths_to_clear_function function start ------------------------
def csv_file_paths_to_clear_function():
  localhost_print_function(' ------------------------ csv_file_paths_to_clear_function function start ------------------------ ')
  csv_file_paths_to_be_cleared_arr = [
    'backend/csv/output/careers_page_found.csv',
    'backend/csv/output/careers_page_not_found.csv',
    'backend/csv/output/output_cleaned.csv'
  ]
  localhost_print_function(' ------------------------ csv_file_paths_to_clear_function function end ------------------------ ')
  return csv_file_paths_to_be_cleared_arr
# ------------------------ csv_file_paths_to_clear_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__main__':
#   csv_file_paths_to_clear_function()
# ------------------------ call end ------------------------