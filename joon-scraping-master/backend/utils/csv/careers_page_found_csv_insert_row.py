# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
# ------------------------ imports end ------------------------


# ------------------------ careers_page_found_csv_insert_row_function function start ------------------------
def careers_page_found_csv_insert_row_function(scrape_tracking_dict):
  localhost_print_function(' ------------------------ careers_page_found_csv_insert_row_function function start ------------------------ ')
  company_name = scrape_tracking_dict['company_name'][-1]
  company_website = scrape_tracking_dict['company_website'][-1]
  words_found_master_str = scrape_tracking_dict['words_found_master_str'][-1]
  keyword_careers_found_and_clicked = scrape_tracking_dict['keyword_careers_found_and_clicked'][-1]
  keyword_benefits_found_on_page = scrape_tracking_dict['keyword_benefits_found_on_page'][-1]
  keyword_category_found_on_page = scrape_tracking_dict['keyword_category_found_on_page'][-1]
  match_health_and_wellness = scrape_tracking_dict['match_health_and_wellness'][-1]
  match_work_from_home = scrape_tracking_dict['match_work_from_home'][-1]
  match_learning_and_development = scrape_tracking_dict['match_learning_and_development'][-1]

  fields=[company_name, company_website, words_found_master_str, keyword_careers_found_and_clicked, keyword_benefits_found_on_page, keyword_category_found_on_page, match_health_and_wellness, match_work_from_home, match_learning_and_development]
  with open(r'backend/csv/output/careers_page_found.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
  localhost_print_function(' ------------------------ careers_page_found_csv_insert_row_function function end ------------------------ ')
  return True
# ------------------------ careers_page_found_csv_insert_row_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__main__':
#   careers_page_found_csv_insert_row_function()
# ------------------------ call end ------------------------