# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
import pandas as pd
# ------------------------ imports end ------------------------


# ------------------------ delete_last_row_from_csv_careers_not_found_function function start ------------------------
def delete_last_row_from_csv_careers_not_found_function():
  localhost_print_function(' ------------------------ delete_last_row_from_csv_careers_not_found_function function start ------------------------ ')

  # ------------------------ get latest csv info start ------------------------
  file_path = 'backend/csv/output/careers_page_not_found.csv'

  f = open(file_path, "r+")
  lines = f.readlines()
  lines.pop()
  f = open(file_path, "w+")
  f.writelines(lines)
  # ------------------------ get latest csv info end ------------------------

  localhost_print_function(' ------------------------ delete_last_row_from_csv_careers_not_found_function function end ------------------------ ')
  return None
# ------------------------ delete_last_row_from_csv_careers_not_found_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__main__':
#   delete_last_row_from_csv_careers_not_found_function()
# ------------------------ call end ------------------------