# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import pandas as pd
# ------------------------ imports end ------------------------


# ------------------------ dict_pandas_csv_function function start ------------------------
def dict_pandas_csv_function(scrape_tracking_dict):
  localhost_print_function(' ------------------------ dict_pandas_csv_function function start ------------------------ ')
  # ------------------------ assign/initialize variables start ------------------------
  df = pd.DataFrame(scrape_tracking_dict)
  df.to_csv('backend/csv/output/output.csv', index = False, encoding='utf-8') # False: not include index
  # ------------------------ loop csv end ------------------------
  localhost_print_function(' ------------------------ dict_pandas_csv_function function end ------------------------ ')
  return True
# ------------------------ dict_pandas_csv_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__dict_pandas_csv_function__':
#   dict_pandas_csv_function()
# ------------------------ call end ------------------------