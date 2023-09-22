# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
from backend.utils.csv.add_header_to_csv_careers_found_and_not_found import add_header_to_csv_careers_found_and_not_found_function
from backend.csv.input.csv_file_paths_to_clear import csv_file_paths_to_clear_function
# ------------------------ imports end ------------------------


# ------------------------ delete_all_rows_except_header_csv_function function start ------------------------
def delete_all_rows_except_header_csv_function():
  localhost_print_function(' ------------------------ delete_all_rows_except_header_csv_function function start ------------------------ ')

  # ------------------------ get list of csv file paths start ------------------------
  csv_file_paths_to_be_cleared_arr = csv_file_paths_to_clear_function()
  # ------------------------ get list of csv file paths end ------------------------


  # ------------------------ for each csv list start ------------------------
  for i_csv_file_path in csv_file_paths_to_be_cleared_arr:
    # ------------------------ get headers from csv file start ------------------------
    headers_arr = []
    with open(i_csv_file_path) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter = ',')
      for row in csv_reader:
        headers_arr = row
        break
    # ------------------------ get headers from csv file end ------------------------


    # ------------------------ delete all data from csv including headers start ------------------------
    f = open(i_csv_file_path, "w+")
    f.close()
    localhost_print_function(' ------------------------ delete_all_rows_except_header_csv_function function end ------------------------ ')
    # ------------------------ delete all data from csv including headers end ------------------------


    # ------------------------ insert header back into csv file start ------------------------
    add_header_back = add_header_to_csv_careers_found_and_not_found_function(i_csv_file_path, headers_arr)
    # ------------------------ insert header back into csv file end ------------------------
    # ------------------------ for each csv list end ------------------------

  return True


# ------------------------ call start ------------------------
# if __name__ == '__main__':
#   delete_all_rows_except_header_csv_function()
# ------------------------ call end ------------------------