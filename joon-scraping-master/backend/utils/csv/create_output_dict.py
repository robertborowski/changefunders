# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
from backend.utils.csv.add_header_to_csv_careers_found_and_not_found import add_header_to_csv_careers_found_and_not_found_function
from backend.csv.input.csv_file_paths_to_clear import csv_file_paths_to_clear_function
# ------------------------ imports end ------------------------


# ------------------------ create_output_dict_function function start ------------------------
def create_output_dict_function():
  localhost_print_function(' ------------------------ create_output_dict_function function start ------------------------ ')

  # ------------------------ get headers from csv file start ------------------------
  # headers_arr = ['Company Name','Company Website','Health and Wellness','Work From Home','Learning and Development']
  # ------------------------ get headers from csv file start ------------------------

  # ------------------------ get headers from csv file start ------------------------
  i_csv_file_path = 'backend/csv/output/careers_page_found.csv'
  with open(i_csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
      company_name = row[0]
      company_website = row[1]

      match_health_and_wellness = row[6]
      if match_health_and_wellness == 'True':
        match_health_and_wellness = 'x'
      else:
        match_health_and_wellness = ''

      match_work_from_home = row[7]
      if match_work_from_home == 'True':
        match_work_from_home = 'x'
      else:
        match_work_from_home = ''

      match_learning_and_development = row[8]
      if match_learning_and_development == 'True':
        match_learning_and_development = 'x'
      else:
        match_learning_and_development = ''
      
      row_arr = [company_name, company_website, match_health_and_wellness, match_work_from_home, match_learning_and_development]
      i_csv_file_path_cleaned = 'backend/csv/output/output_cleaned.csv'
      with open(i_csv_file_path_cleaned, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row_arr)
  # ------------------------ get headers from csv file end ------------------------

  return True


# ------------------------ call start ------------------------
# if __name__ == '__main__':
#   create_output_dict_function()
# ------------------------ call end ------------------------