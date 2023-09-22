# ------------------------ imports start ------------------------
from curses.ascii import TAB
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
# ------------------------ imports end ------------------------


# ------------------------ search_keyword_within_link_function function start ------------------------
def search_keyword_within_link_function(driver, driver_page_source, keywords_to_search_arr, scrape_tracking_dict):
  localhost_print_function(' ------------------------ search_keyword_within_link_function function start ------------------------ ')
  # ------------------------ set variables start ------------------------
  company_name = scrape_tracking_dict['company_name'][-1]
  company_website = scrape_tracking_dict['company_website'][-1]
  # ------------------------ set variables end ------------------------
  # ------------------------ loop through keywords arr start ------------------------
  desired_href_str = ''
  desired_href_found_arr = []
  for word in keywords_to_search_arr:
    # ------------------------ clean word start ------------------------
    word = word.strip()
    word = word.lower()
    # localhost_print_function(f' ------------------------ end old i ------------------------------- ')
    # localhost_print_function('-')
    # localhost_print_function('-')
    # localhost_print_function(f' ------------------------ start new i:{word} ------------------------------- ')
    # localhost_print_function(f'cleaned word to search for: {word}')
    # ------------------------ clean word end ------------------------
    # ------------------------ search driver page source start ------------------------
    # Word exists on page
    if word not in driver_page_source:
      # localhost_print_function(f'word {word} not in page source')
      pass
    if word in driver_page_source:
      # localhost_print_function(f'company: {company_name} | website: {company_website} | contains word: {word}')
      # ------------------------ careers page attempts start ------------------------
      # ------------------------ attempt #1 find href string from page source start ------------------------
      try:
        desired_href_str = driver.find_element(By.XPATH, f'//a[contains(@href, "{word}")]').get_attribute('href')    # Type: <class 'selenium.webdriver.remote.webelement.WebElement'>
        # localhost_print_function(f'company: {company_name} | website: {company_website} | contains word: {word} | in href: {desired_href_str}')
        if desired_href_str not in desired_href_found_arr:
          desired_href_found_arr.append(desired_href_str)
      except:
        desired_href_str = None

  # localhost_print_function(f'List of hrefs for these keywords: {desired_href_found_arr}')
  localhost_print_function(' ------------------------ search_keyword_within_link_function function end ------------------------ ')
  return desired_href_found_arr
# ------------------------ search_keyword_within_link_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__search_keyword_within_link_function__':
#   search_keyword_within_link_function()
# ------------------------ call end ------------------------