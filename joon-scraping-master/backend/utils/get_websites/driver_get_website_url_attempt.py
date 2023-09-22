# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
from backend.utils.sanitize.sanitize_replace_space_remove_special import sanitize_replace_space_remove_special_function
from backend.utils.sanitize.sanitize_website_url import sanitize_website_url_function
from backend.utils.word_manipulation.number_dict_key import number_dict_key_function
import time
# ------------------------ imports end ------------------------


# ------------------------ driver_get_website_url_attempt_function function start ------------------------
def driver_get_website_url_attempt_function(driver, company_website):
  localhost_print_function(' ------------------------ driver_get_website_url_attempt_function function start ------------------------ ')
  page_loaded_success_status = False
  # ------------------------ go to company website attempt start ------------------------
  # ------------------------ successful attempt start ------------------------
  try:
    localhost_print_function(f'live_check_print_01.00: attempting website: {company_website}')
    # Go to company website
    sec_wait = 2.75
    time.sleep(sec_wait)
    driver.get(company_website)
    time.sleep(sec_wait*2)
    localhost_print_function(f'live_check_print_01.01: successfully got to URL: {company_website} 01')
    page_loaded_success_status = True
  # ------------------------ successful attempt end ------------------------
  # ------------------------ re-running script for page load errors start ------------------------
  except:
    localhost_print_function(f'live_check_print_01.02: URL does NOT work for: {company_website} 01')
    pass
  localhost_print_function(' ------------------------ driver_get_website_url_attempt_function function end ------------------------ ')
  return page_loaded_success_status, driver
# ------------------------ driver_get_website_url_attempt_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__driver_get_website_url_attempt_function__':
#   driver_get_website_url_attempt_function()
# ------------------------ call end ------------------------