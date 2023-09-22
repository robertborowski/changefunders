# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import pandas as pd
from backend.utils.sanitize.sanitize_replace_space_remove_special import sanitize_replace_space_remove_special_function
# ------------------------ imports end ------------------------


# ------------------------ create_scrape_tracking_dict_function function start ------------------------
def create_scrape_tracking_dict_function():
  localhost_print_function(' ------------------------ create_scrape_tracking_dict_function function start ------------------------ ')
  # ------------------------ manipulation start ------------------------
  scrape_tracking_dict = {}
  scrape_tracking_dict['company_name'] = []
  scrape_tracking_dict['company_website'] = []
  scrape_tracking_dict['words_found_master_str'] = []
  scrape_tracking_dict['keyword_careers_found_and_clicked'] = []
  scrape_tracking_dict['keyword_benefits_found_on_page'] = []
  scrape_tracking_dict['keyword_category_found_on_page'] = []
  scrape_tracking_dict['match_health_and_wellness'] = []
  scrape_tracking_dict['match_work_from_home'] = []
  scrape_tracking_dict['match_learning_and_development'] = []
  # ------------------------ manipulation end ------------------------
  localhost_print_function(' ------------------------ create_scrape_tracking_dict_function function end ------------------------ ')
  return scrape_tracking_dict
# ------------------------ create_scrape_tracking_dict_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__create_scrape_tracking_dict_function__':
#   create_scrape_tracking_dict_function()
# ------------------------ call end ------------------------