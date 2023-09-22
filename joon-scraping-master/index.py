# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from backend.utils.get_websites.get_websites_dict import get_website_dict_function
from backend.utils.words_to_search_for.keywords_to_search_for import keywords_to_search_for_function
from backend.search_steps_backend.search_keyword_within_link import search_keyword_within_link_function
from backend.search_steps_backend.search_keyword_exists_on_page import search_keyword_exists_on_page_function
from backend.utils.create_scrape_tracking_dict.create_scrape_tracking_dict import create_scrape_tracking_dict_function
from backend.utils.dict_pandas_csv.dict_pandas_csv import dict_pandas_csv_function
from backend.utils.csv.careers_page_not_found_csv_insert_row import careers_page_not_found_csv_insert_row_function
from backend.utils.csv.careers_page_found_csv_insert_row import careers_page_found_csv_insert_row_function
from backend.utils.csv.delete_all_rows_except_header_csv import delete_all_rows_except_header_csv_function
import pandas as pd
from backend.utils.csv.check_csv_if_already_passed_careers_page_check import check_csv_if_already_passed_careers_page_check_function
from backend.utils.csv.check_csv_latest_row_added_to_careers_not_found_file import check_csv_latest_row_added_to_careers_not_found_file_function
from backend.utils.csv.delete_last_row_from_csv_careers_not_found import delete_last_row_from_csv_careers_not_found_function
from backend.utils.get_websites.driver_get_website_url_attempt import driver_get_website_url_attempt_function
from backend.utils.dict_utils.close_out_scrape_tracking_dict_remainder import close_out_scrape_tracking_dict_remainder_function
from backend.utils.csv.create_output_dict import create_output_dict_function
# ------------------------ imports end ------------------------


# ------------------------ index_starting_function function start ------------------------
def index_starting_function(driver, websites_dict, main_function_attempt_int, run_reason):
  localhost_print_function(' function run start spacing ...')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ')
  localhost_print_function(' ------------------------ index_starting_function function start ------------------------ ')
  localhost_print_function(f'run_reason: {run_reason}')
  localhost_print_function(f'main_function_attempt_int: {main_function_attempt_int}')

  # ------------------------ function recall checks start ------------------------
  if run_reason != 'index':
    localhost_print_function(f'main_function_attempt_int + correction')
    main_function_attempt_int += 1
    localhost_print_function(f'main_function_attempt_int: {main_function_attempt_int}')
    
  if main_function_attempt_int >= 4:
    localhost_print_function(f'live_check_print_12.78: fail safe: {main_function_attempt_int} stopping')
    return True
  # ------------------------ function recall checks end ------------------------
  
  
  # ------------------------ create get empty dict start ------------------------
  scrape_tracking_dict = create_scrape_tracking_dict_function()
  # ------------------------ create get empty dict end ------------------------
  
  
  # ------------------------ loop through dict start ------------------------
  test_counter = 0
  for k, v in websites_dict.items():
    localhost_print_function(' ')
    localhost_print_function(' ')
    localhost_print_function(' ')
    localhost_print_function(' ')
    localhost_print_function(' ')
    localhost_print_function(' ')
    localhost_print_function(' ')
    localhost_print_function(' --------------------------- start loop iteration ----------------------------------- ')
    # ------------------------ testing force stop start ------------------------
    test_counter += 1
    # acceptable_arr = ['bloomreach', 'ironclad', 'lex_markets', 'chronicled', 'sibros', 'databook', 'vivvi','deepscribe','swoogo','nowsta']
    # if k not in acceptable_arr:
    #   localhost_print_function(' ')
    #   localhost_print_function(f'skipping, {k} test_counter at: {test_counter}')
    #   continue
    # ------------------------ testing force stop end ------------------------
    # ------------------------ set variables start ------------------------
    company_name = k
    company_website = v
    # ------------------------ set variables end ------------------------
    localhost_print_function(f'------- pre-summary start')
    # ------------------------ get latest csv info start ------------------------
    careers_page_already_stored_for_company = check_csv_if_already_passed_careers_page_check_function(company_name)
    if careers_page_already_stored_for_company == True:
      localhost_print_function(' ')
      localhost_print_function(f'live_check_print_99.00: copmany careers page already found for: {company_name} - continuing to next item in loop 01 | test_counter: {test_counter}')
      continue
    # ------------------------ get latest csv info end ------------------------
    # ------------------------ get latest company not found start ------------------------
    check_csv_latest_row_added_to_careers_not_found_file = check_csv_latest_row_added_to_careers_not_found_file_function()
    # ------------------------ get latest company not found end ------------------------
    # ------------------------ if run reason not index start ------------------------
    if company_name == check_csv_latest_row_added_to_careers_not_found_file and run_reason != 'index':
      delete_last_row_from_csv_careers_not_found_function()
      localhost_print_function(f'live_check_print_66.00: removed {company_name} from the not found csv on the {main_function_attempt_int}(st/th) rerun')
      # ------------------------ check if company not found list empty start ------------------------
      check_csv_latest_row_added_to_careers_not_found_file = check_csv_latest_row_added_to_careers_not_found_file_function()
      localhost_print_function(f'live_check_print_78.03: check_csv_latest_row_added_to_careers_not_found_file: {check_csv_latest_row_added_to_careers_not_found_file}')
      localhost_print_function(f' ')
      # ------------------------ check if company not found list empty end ------------------------
    # ------------------------ if run reason not index end ------------------------
    localhost_print_function(f'------- pre-summary end')
    localhost_print_function(f'------- summary start')
    # ------------------------ force stop start ------------------------
    localhost_print_function(f'company_name: {company_name} | company_website: {company_website} | test_counter: {test_counter}')
    localhost_print_function(f'current run_reason: {run_reason}')
    localhost_print_function(f'current main_function_attempt_int: {main_function_attempt_int}')
    localhost_print_function(f'check_csv_latest_row_added_to_careers_not_found_file: {check_csv_latest_row_added_to_careers_not_found_file}')
    localhost_print_function(f'------- summary end')
    # ------------------------ force stop end ------------------------
    # ------------------------ for index_starting_function function reruns end ------------------------
    # ------------------------ append dict arr start ------------------------
    scrape_tracking_dict['company_name'].append(company_name)
    scrape_tracking_dict['company_website'].append(company_website)
    scrape_tracking_dict['words_found_master_str'].append(',')
    # ------------------------ append dict arr end ------------------------
    # ------------------------ go to company website attempt start ------------------------
    # Website Attempt #1 - landing page
    page_loaded_success_status, driver = driver_get_website_url_attempt_function(driver, company_website)
    
    if page_loaded_success_status == False:
      run_reason = 'run_failure: website attempt #1 landing page'
      scrape_tracking_dict = close_out_scrape_tracking_dict_remainder_function(scrape_tracking_dict)
      careers_page_not_found_csv_insert_row_function(scrape_tracking_dict)
      localhost_print_function(f'Now about to rerun index_starting_function: run_reason: "{run_reason}" | main_function_attempt_int: "{main_function_attempt_int}"')
      index_starting_function(driver, websites_dict, main_function_attempt_int, run_reason)
      localhost_print_function(f'Now about to break rerun index_starting_function: run_reason: "{run_reason}" | main_function_attempt_int: "{main_function_attempt_int}"')
      try:
        driver.close()
      except:
        localhost_print_function('driver already closed v01')
        pass
      return True
      # ------------------------ list of if logic to reset function end ------------------------
    if run_reason == 'run_failure: website attempt #1 landing page':
      run_reason = 'index'
      localhost_print_function('v01 run_reason changed back to "index" after a failure')
    # ------------------------ go to company website attempt end ------------------------
    # ------------------------ get all keywords csv start ------------------------
    keywords_dict = keywords_to_search_for_function()
    # ------------------------ get all keywords csv end ------------------------
    # ------------------------ get page source start ------------------------
    driver_page_source = driver.page_source
    # ------------------------ get page source end ------------------------
    # ------------------------ get keywords career hrefs start ------------------------
    keywords_to_search_arr = list(keywords_dict['careers_keywords'])
    keywords_careers_hrefs_arr = search_keyword_within_link_function(driver, driver_page_source, keywords_to_search_arr, scrape_tracking_dict)
    if keywords_careers_hrefs_arr == None or keywords_careers_hrefs_arr == []:
      localhost_print_function(f'no careers keywords found on landing page for company "{company_name}". Moving on. run_reason: "{run_reason}"')
      scrape_tracking_dict = close_out_scrape_tracking_dict_remainder_function(scrape_tracking_dict)
      careers_page_found_csv_insert_row_function(scrape_tracking_dict)
      continue
    else:
      scrape_tracking_dict['keyword_careers_found_and_clicked'].append(True)
      localhost_print_function(f'live_check_print_03.00: keyword_careers_found_and_clicked = True.')
      # storing just the first careers keyword website link found
      scrape_tracking_dict['words_found_master_str'][-1] += '[[[-keywords_careers_href_1: ' + keywords_careers_hrefs_arr[0]
      localhost_print_function(f'live_check_print_03.01: appended [[[-keywords_careers_href_1: {keywords_careers_hrefs_arr[0]}')
    # ------------------------ get keywords career hrefs end ------------------------


    # ------------------------ attempt to go to careers href start ------------------------
    if scrape_tracking_dict['keyword_careers_found_and_clicked'][-1] == True:
      # ------------------------ go to company website attempt start ------------------------
      # Website Attempt #2 - careers page
      page_loaded_success_status, driver = driver_get_website_url_attempt_function(driver, keywords_careers_hrefs_arr[0])
      if page_loaded_success_status == False:
        run_reason = 'run_failure: website attempt #2 careers page'
        scrape_tracking_dict = close_out_scrape_tracking_dict_remainder_function(scrape_tracking_dict)
        careers_page_not_found_csv_insert_row_function(scrape_tracking_dict)
        localhost_print_function(f'Now about to rerun index_starting_function: run_reason: "{run_reason}" | main_function_attempt_int: "{main_function_attempt_int}"')
        index_starting_function(driver, websites_dict, main_function_attempt_int, run_reason)
        localhost_print_function(f'Now about to break rerun index_starting_function: run_reason: "{run_reason}" | main_function_attempt_int: "{main_function_attempt_int}"')
        try:
          driver.close()
        except:
          localhost_print_function('driver already closed v02')
          pass
        return True
        # ------------------------ list of if logic to reset function end ------------------------
      if run_reason == 'run_failure: website attempt #2 careers page':
        run_reason = 'index'
        localhost_print_function('v01 run_reason changed back to "index" after a failure')
      # ------------------------ go to company website attempt end ------------------------
      # ------------------------ get page source start ------------------------
      driver_page_source = driver.page_source
      # ------------------------ get page source end ------------------------
      # ------------------------ search benefit keywords on careers page start ------------------------
      keywords_word_search_arr = [
        ['benefits_keywords','keyword_benefits_found_on_page'],
        ['category_keywords','keyword_category_found_on_page']
      ]
      for i in keywords_word_search_arr:
        i_keywords_arr = i[0]
        i_found_on_page = i[1]
        keywords_to_search_arr = list(keywords_dict[i_keywords_arr])
        scrape_tracking_dict_item_to_change = i_found_on_page
        scrape_tracking_dict = search_keyword_exists_on_page_function(driver, driver_page_source, keywords_to_search_arr, scrape_tracking_dict, scrape_tracking_dict_item_to_change)
      # ------------------------ search benefit keywords on careers page end ------------------------
      scrape_tracking_dict = close_out_scrape_tracking_dict_remainder_function(scrape_tracking_dict)
    # ------------------------ attempt to go to careers href end ------------------------
    scrape_tracking_dict = close_out_scrape_tracking_dict_remainder_function(scrape_tracking_dict)
    careers_page_found_csv_insert_row_function(scrape_tracking_dict)
  # ------------------------ loop through dict end ------------------------


  # ------------------------ close webdriver start ------------------------
  try:
    driver.close()
  except:
    localhost_print_function('driver already closed 03')
    pass
  # ------------------------ close webdriver end ------------------------


  # ------------------------ better output start ------------------------
  output_status = create_output_dict_function()
  # ------------------------ better output end ------------------------

  localhost_print_function(' ------------------------ index_starting_function function end ------------------------ ')
  return True
# ------------------------ index_starting_function function end ------------------------


# ------------------------ call start ------------------------
if __name__ == '__main__':
  # ------------------------ delete all rows from tracking csv's start ------------------------
  delete_all_rows_except_header_csv_function()
  # ------------------------ delete all rows from tacking csv's end ------------------------
  # ------------------------ get websites dict start ------------------------
  websites_dict = get_website_dict_function()
  # ------------------------ get websites dict end ------------------------
  # ------------------------ open webdriver start ------------------------
  driver = webdriver.Chrome('./chromedriver')
  driver.maximize_window()
  # ------------------------ open webdriver end ------------------------
  # ------------------------ start script start ------------------------
  run_reason = 'index'
  index_starting_function(driver, websites_dict, 0, run_reason)
  # ------------------------ start script end ------------------------
  # ------------------------ close webdriver start ------------------------
  try:
    driver.close()
  except:
    localhost_print_function('driver already closed')
    pass
  # ------------------------ close webdriver end ------------------------
# ------------------------ call end ------------------------