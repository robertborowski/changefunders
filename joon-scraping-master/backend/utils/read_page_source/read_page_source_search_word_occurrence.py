# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
# ------------------------ imports end ------------------------


# ------------------------ read_page_source_search_word_occurrence_function function start ------------------------
def read_page_source_search_word_occurrence_function(driver, driver_page_source, keywords_to_search_arr, master_str_benefit_html_found, company_name):
  localhost_print_function(' ------------------------ read_page_source_search_word_occurrence_function function start ------------------------ ')
  localhost_print_function(f'... driver_page_source scanning in process, this can take a WHILE for some websites. If the wait gets more than a few minutes: best long term solution is to remove "{company_name}" from csv file location: [backend/csv/input/companies_csv.csv]. Cause of this issue?: 1. {company_name} website has a structure that is different from "<tag>" structure or 2. {company_name} website has massive page_source load for some reason.')
  
  # ------------------------ fail safe start ------------------------
  if len(driver_page_source) <= 2:
    localhost_print_function('invalid: read_page_source_search_word_occurrence_function 01')
    return master_str_benefit_html_found
  # ------------------------ fail safe end ------------------------


  # ------------------------ loop through page source start ------------------------
  try:
    current_long_str_to_check = ''
    i_start = 0
    i_end = 0
    
    for char in driver_page_source:
      i_end += 1
      current_long_str_to_check = driver_page_source[i_start:i_end].lower()
      if char == '>':
        pass
      
      
      # ------------------------ new word longest str start ------------------------
      if char == '<':
        # ------------------------ before starting new word string loop through existing start ------------------------
        # Loop through words
        for word in keywords_to_search_arr:
          word = word.strip()
          word = word.lower()
          if word in current_long_str_to_check:
            master_str_benefit_html_found += current_long_str_to_check
        # ------------------------ before starting new word string loop through existing end ------------------------
        # ------------------------ new word string start ------------------------
        current_long_str_to_check = ''
        i_start = i_end
        # ------------------------ new word string end ------------------------
      # ------------------------ new word longest str end ------------------------


      # ------------------------ building str method fail safe start ------------------------
      character_limit = 50000
      if len(current_long_str_to_check) > character_limit:
        localhost_print_function('searching page source current_long_str_to_check is too many characters long ')
        localhost_print_function('changing to xpath search - 1 resulting element only!')
        for word in keywords_to_search_arr:
          word = word.strip()
          word = word.lower()
          try:
            desired_html_str = driver.find_element(By.XPATH, f'//*[contains(text(), "{word}")]').get_attribute('innerHTML')    # Type: <class 'selenium.webdriver.remote.webelement.WebElement'>
            if len(desired_html_str) >= character_limit:
              desired_html_str = '- '
            
            master_str_benefit_html_found += desired_html_str
          except:
            pass
        localhost_print_function(' ------------------------ read_page_source_search_word_occurrence_function function end ------------------------ ')
        return master_str_benefit_html_found
      # ------------------------ building str method fail safe end ------------------------
    # ------------------------ loop through page source end ------------------------
    return master_str_benefit_html_found
  # ------------------------ loop through page source failed start ------------------------
  except:
    localhost_print_function('except error: read_page_source_search_word_occurrence_function')
    return master_str_benefit_html_found
  # ------------------------ loop through page source failed end ------------------------
# ------------------------ read_page_source_search_word_occurrence_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__sanitize_replace_space_remove_special_function__':
#   read_page_source_search_word_occurrence_function()
# ------------------------ call end ------------------------