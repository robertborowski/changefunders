# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
from backend.utils.sanitize.sanitize_replace_space_remove_special import sanitize_replace_space_remove_special_function
from backend.utils.sanitize.sanitize_website_url import sanitize_website_url_function
from backend.utils.word_manipulation.number_dict_key import number_dict_key_function
# ------------------------ imports end ------------------------


# ------------------------ get_website_dict_function function start ------------------------
def get_website_dict_function():
  localhost_print_function(' ------------------------ get_website_dict_function function start ------------------------ ')
  # ------------------------ assign/initialize variables start ------------------------
  websites_dict = {}
  # ------------------------ assign/initialize variables end ------------------------
  # ------------------------ loop csv start ------------------------
  filename = 'backend/csv/input/companies_csv.csv'
  with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    next(datareader)    # skip first row in csv
    for row in datareader:
      company_name = sanitize_replace_space_remove_special_function(row[0])
      company_website = sanitize_website_url_function(row[1])
      # ------------------------ dict start ------------------------
      if company_name in websites_dict:
        company_name = number_dict_key_function(company_name)
      websites_dict[company_name] = company_website
      # ------------------------ dict end ------------------------
  # ------------------------ loop csv end ------------------------
  localhost_print_function(' ------------------------ get_website_dict_function function end ------------------------ ')
  return websites_dict
# ------------------------ get_website_dict_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__get_website_dict_function__':
#   get_website_dict_function()
# ------------------------ call end ------------------------