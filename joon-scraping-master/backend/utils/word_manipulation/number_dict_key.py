# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
from random import *
# ------------------------ imports end ------------------------


# ------------------------ number_dict_key_function function start ------------------------
def number_dict_key_function(company_name):
  localhost_print_function(' ------------------------ number_dict_key_function function start ------------------------ ')
  # ------------------------ manipulation start ------------------------
  rendom_number = randint(1, 1000)
  company_name = company_name + '_' + str(rendom_number)
  # ------------------------ manipulation end ------------------------
  localhost_print_function(' ------------------------ number_dict_key_function function end ------------------------ ')
  return company_name
# ------------------------ number_dict_key_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__number_dict_key_function__':
#   number_dict_key_function()
# ------------------------ call end ------------------------