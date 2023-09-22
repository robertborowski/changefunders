# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from backend.utils.dict_utils.get_output_category_dict import get_output_category_dict_function
from backend.utils.read_page_source.read_page_source_search_word_occurrence import read_page_source_search_word_occurrence_function
# ------------------------ imports end ------------------------


# ------------------------ search_keyword_exists_on_page_function function start ------------------------
def search_keyword_exists_on_page_function(driver, driver_page_source, keywords_to_search_arr, scrape_tracking_dict, scrape_tracking_dict_item_to_change):
  localhost_print_function(' ------------------------ search_keyword_exists_on_page_function function start ------------------------ ')
  
  
  # ------------------------ assign variables start ------------------------
  company_name = scrape_tracking_dict['company_name'][-1]
  company_website = scrape_tracking_dict['company_website'][-1]
  # ------------------------ assign variables end ------------------------


  # ------------------------ Part 1 - search for link within page start ------------------------
  at_least_one_found = False
  count_true = 0
  for word in keywords_to_search_arr:
    word = word.strip()
    word = word.lower()
    if word in driver_page_source:
      count_true += 1
      if count_true == 1:
        scrape_tracking_dict[scrape_tracking_dict_item_to_change].append(True)
        localhost_print_function(f'live_check_print_04.00: {scrape_tracking_dict_item_to_change} = True, at least 1 keyword present on page')
      scrape_tracking_dict['words_found_master_str'][-1] += '[[[-' + scrape_tracking_dict_item_to_change + ': ' + word
      at_least_one_found = True
  if at_least_one_found == False:
    localhost_print_function(f'live_check_print_04.01: {scrape_tracking_dict_item_to_change} = False, none found in page source')
    scrape_tracking_dict[scrape_tracking_dict_item_to_change].append(False)
  # ------------------------ Part 1 - search for link within page end ------------------------
  
  
  # ------------------------ capture str block that contains word(s) start ------------------------
  if scrape_tracking_dict_item_to_change == 'keyword_benefits_found_on_page':
    if scrape_tracking_dict[scrape_tracking_dict_item_to_change][-1] == True:
      # ------------------------ testing 02 start ------------------------
      master_str_benefit_html_found = '- '
      master_str_benefit_html_found = read_page_source_search_word_occurrence_function(driver, driver_page_source, keywords_to_search_arr, master_str_benefit_html_found, company_name)
      scrape_tracking_dict['words_found_master_str'][-1] += '[[[-master_str_benefit_html_found: ' + master_str_benefit_html_found
      localhost_print_function(f'live_check_print_04.11: adding the [[[-master_str_benefit_html_found: phrases/words from full page source scrape')
      localhost_print_function(f'live_check_print_04.12: [[[-master_str_benefit_html_found: {master_str_benefit_html_found}')
    else:
      localhost_print_function(f'live_check_print_04.13: [[[-master_str_benefit_html_found = None becuase keyword_benefits_found_on_page is False')
      pass
  # ------------------------ capture str block that contains word(s) end ------------------------
  
  
  # ------------------------ look for match in captured str if exists start ------------------------
  if scrape_tracking_dict_item_to_change == 'keyword_category_found_on_page':
    if scrape_tracking_dict['keyword_benefits_found_on_page'][-1] == True:
      
      counter_topic_hw = 0
      counter_topic_wfh = 0
      counter_topic_ld = 0

      category_match_dict = get_output_category_dict_function()
      words_found_master_str_arr = scrape_tracking_dict['words_found_master_str'][-1].split('[[[-')
      for i_master_words_str in words_found_master_str_arr:
        if 'master_str_benefit_html_found: ' in i_master_words_str:
          for word in keywords_to_search_arr:
            word = word.strip()
            word = word.lower()
            if word in i_master_words_str.lower():
              for k, v in category_match_dict.items():
                if word == k.lower():

                  search_dict_value = 'health & wellness'
                  search_dict_words = 'match_health_and_wellness'
                  if v.lower() == search_dict_value:
                    counter_topic_hw += 1
                    if counter_topic_hw == 1:
                      scrape_tracking_dict[search_dict_words].append(True)
                      localhost_print_function(f'live_check_print_05.00: {search_dict_words} append True')
                
                  search_dict_value = 'work from home'
                  search_dict_words = 'match_work_from_home'
                  if v.lower() == search_dict_value:
                    counter_topic_wfh += 1
                    if counter_topic_wfh == 1:
                      scrape_tracking_dict[search_dict_words].append(True)
                      localhost_print_function(f'live_check_print_05.00: {search_dict_words} append True')
                  
                  search_dict_value = 'learning & development'
                  search_dict_words = 'match_learning_and_development'
                  if v.lower() == search_dict_value:
                    counter_topic_ld += 1
                    if counter_topic_ld == 1:
                      scrape_tracking_dict[search_dict_words].append(True)
                      localhost_print_function(f'live_check_print_05.00: {search_dict_words} append True')

                  # scrape_tracking_dict['scrape_logic_check_01'].append(v)
              scrape_tracking_dict['words_found_master_str'][-1] += '[[[-scrape_benefit_category_proof: word: ' + word + ' | phrase: ' + i_master_words_str
              localhost_print_function(f'live_check_print_05.01: scrape_benefit_category_proof appended')
    else:
      localhost_print_function(f'live_check_print_04.03: no benefits found so nothing to compare category within.')
      pass
  # ------------------------ look for match in captured str if exists end ------------------------


  localhost_print_function(' ------------------------ search_keyword_exists_on_page_function function end ------------------------ ')
  return scrape_tracking_dict
# ------------------------ search_keyword_exists_on_page_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__search_keyword_exists_on_page_function__':
#   search_keyword_exists_on_page_function()
# ------------------------ call end ------------------------