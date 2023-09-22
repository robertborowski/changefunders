# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
import pandas as pd
# ------------------------ imports end ------------------------


# ------------------------ check_csv_latest_row_added_to_careers_not_found_file_function function start ------------------------
def check_csv_latest_row_added_to_careers_not_found_file_function():
  localhost_print_function(' ------------------------ check_csv_latest_row_added_to_careers_not_found_file_function function start ------------------------ ')

  # ------------------------ get latest csv info start ------------------------
  file_path = 'backend/csv/output/careers_page_not_found.csv'
  df = pd.read_csv (file_path)
  try:
    subset_check_result = df['company_name'][df.index[-1]]
  except:
    subset_check_result = None
  # ------------------------ get latest csv info end ------------------------

  localhost_print_function(' ------------------------ check_csv_latest_row_added_to_careers_not_found_file_function function end ------------------------ ')
  return subset_check_result
# ------------------------ check_csv_latest_row_added_to_careers_not_found_file_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__main__':
#   check_csv_latest_row_added_to_careers_not_found_file_function()
# ------------------------ call end ------------------------