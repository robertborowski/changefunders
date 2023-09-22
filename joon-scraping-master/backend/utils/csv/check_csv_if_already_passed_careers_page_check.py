# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
import pandas as pd
# ------------------------ imports end ------------------------


# ------------------------ check_csv_if_already_passed_careers_page_check_function function start ------------------------
def check_csv_if_already_passed_careers_page_check_function(company_name):
  localhost_print_function(' ------------------------ check_csv_if_already_passed_careers_page_check_function function start ------------------------ ')

  # ------------------------ get latest csv info start ------------------------
  file_path = 'backend/csv/output/careers_page_found.csv'
  df = pd.read_csv (file_path)
  subset = pd.Series(list(df['company_name']))
  subset_check = company_name
  subset_check_result = subset[subset.isin([subset_check])].empty
  
  is_found = False
  if subset_check_result == False:
    is_found = True
  # ------------------------ get latest csv info end ------------------------

  localhost_print_function(' ------------------------ check_csv_if_already_passed_careers_page_check_function function end ------------------------ ')
  return is_found
# ------------------------ check_csv_if_already_passed_careers_page_check_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__main__':
#   check_csv_if_already_passed_careers_page_check_function()
# ------------------------ call end ------------------------