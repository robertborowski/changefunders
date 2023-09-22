# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import re
# ------------------------ imports end ------------------------


# ------------------------ sanitize_website_url_function function start ------------------------
def sanitize_website_url_function(url):
  # localhost_print_function(' ------------------------ sanitize_website_url_function function start ------------------------ ')
  # ------------------------ sanitize start ------------------------
  url = url.strip()
  
  url = url.lower()
  
  if url[-1] == '/':
    url = url[:-1]
  
  at_least_one_found = False
  search_starter_str = ['https://', 'http://']
  for i in search_starter_str:
    if i in url:
      at_least_one_found = True
  
  if at_least_one_found == False:
    url = 'https://' + url
  # ------------------------ sanitize end ------------------------
  # localhost_print_function(' ------------------------ sanitize_website_url_function function end ------------------------ ')
  return url
# ------------------------ sanitize_website_url_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__sanitize_website_url_function__':
#   sanitize_website_url_function()
# ------------------------ call end ------------------------