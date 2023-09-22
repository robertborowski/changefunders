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
def search_keyword_within_link_function(driver, driver_page_source, keywords_to_search_arr, scrape_tracking_dict, scrape_tracking_dict_item_to_change, run_reason):
  localhost_print_function(' ------------------------ search_keyword_within_link_function function start ------------------------ ')
  # ------------------------ set variables start ------------------------
  company_name = scrape_tracking_dict['company_name'][-1]
  company_website = scrape_tracking_dict['company_website'][-1]
  """
  if company_website[-1] == '/':
    company_website = company_website[:-1]
  """
  at_least_one_found = False
  count_true = 0
  # ------------------------ set variables end ------------------------
  # ------------------------ loop through keywords arr start ------------------------
  for word in keywords_to_search_arr:
    # ------------------------ clean word start ------------------------
    word = word.strip()
    word = word.lower()
    localhost_print_function(' - - - - - - - - - - - - ')
    localhost_print_function(f'cleaned word to search for: {word}')
    # ------------------------ clean word end ------------------------
    # ------------------------ search driver page source start ------------------------
    # Word exists on page
    if word in driver_page_source:
      localhost_print_function(f'company: {company_name} | website: {company_website} | contains word: {word}')
      # ------------------------ careers page attempts start ------------------------
      # ------------------------ attempt #1 click link start ------------------------
      try:
        localhost_print_function(' =============== element about to click start =============== ')
        driver.find_element(By.XPATH, f'//a[contains(@href, "{word}")]').click()
        localhost_print_function(' =============== element CLICKED start =============== ')
        desired_href_str = driver.find_element(By.XPATH, f'//a[contains(@href, "{word}")]').get_attribute('href')    # Type: <class 'selenium.webdriver.remote.webelement.WebElement'>
        localhost_print_function('- - - - - - - 01 - - - - - - -')
        localhost_print_function('desired_href_str')
        localhost_print_function(desired_href_str)
        localhost_print_function(type(desired_href_str))
        localhost_print_function('- - - - - - - 01 - - - - - - -')
        localhost_print_function(' =============== element CLICKED end =============== ')
        localhost_print_function(' =============== element about to click end =============== ')
        count_true += 1
        if count_true == 1:
          scrape_tracking_dict[scrape_tracking_dict_item_to_change].append(True)
        scrape_tracking_dict['words_found_master_str'][-1] += scrape_tracking_dict_item_to_change + ': ' + word + ', '
        at_least_one_found = True
        localhost_print_function(f'company: {company_name} | website: {company_website} | contains link: {word}')
        localhost_print_function(f'breaking out of loop because of word: {word}')
        localhost_print_function(' ------------------------ search_keyword_within_link_function function end ------------------------ ')
        return scrape_tracking_dict
      # ------------------------ attempt #1 click link end ------------------------
      
      except:
        # ------------------------ attempt #2 find href string from page source start ------------------------
        try:
          localhost_print_function(' =============== element NOT clicked start =============== ')
          desired_href_str = driver.find_element(By.XPATH, f'//a[contains(@href, "{word}")]').get_attribute('href')    # Type: <class 'selenium.webdriver.remote.webelement.WebElement'>
          localhost_print_function('- - - - - - - 1 - - - - - - -')
          localhost_print_function('desired_href_str')
          localhost_print_function(desired_href_str)
          localhost_print_function(type(desired_href_str))
          localhost_print_function('- - - - - - - 1 - - - - - - -')
          localhost_print_function(' =============== element NOT clicked end =============== ')
          localhost_print_function(' =============== element about to click end =============== ')
          try:
            # Go to company website
            time.sleep(3)
            driver.get(desired_href_str)
            time.sleep(3)
            count_true += 1
            if count_true == 1:
              scrape_tracking_dict[scrape_tracking_dict_item_to_change].append(True)
            scrape_tracking_dict['words_found_master_str'][-1] += scrape_tracking_dict_item_to_change + ': ' + word + ', '
            at_least_one_found = True
            localhost_print_function(f'company: {company_name} | website: {company_website} | contains link: {word}')
            localhost_print_function(f'breaking out of loop because of word: {word}')
            localhost_print_function(' ------------------------ search_keyword_within_link_function function end ------------------------ ')
            return scrape_tracking_dict
          except:
            localhost_print_function(f'URL does not work for: {company_website} 02')



        # ------------------------ attempt #2 find href string from page source end ------------------------
        except:
          if at_least_one_found == False:
            scrape_tracking_dict[scrape_tracking_dict_item_to_change].append(False)
          localhost_print_function(' ------------------------ search_keyword_within_link_function function end ------------------------ ')
          return scrape_tracking_dict


          """
          # ------------------------ attempt #3 force guess URL containing word start ------------------------
          # Does word exist on website and cannot be clicked for some reason
          if driver.find_element(By.XPATH, f'//a[contains(@href, "{word}")]') != None:
            driver.get('https://' + company_website + f'/{word}')    # When click causes an error, check if URL works
            localhost_print_function(f'company: {company_name} | website: {company_website} | contains url: {word}')
            count_true += 1
            if count_true == 1:
              scrape_tracking_dict[scrape_tracking_dict_item_to_change].append(True)
            scrape_tracking_dict['words_found_master_str'][-1] += scrape_tracking_dict_item_to_change + ': ' + word + ', '
            at_least_one_found = True
            localhost_print_function(f'company: {company_name} | website: {company_website} | contains link: {word}')
            localhost_print_function(f'breaking out of loop because of word: {word}')
            localhost_print_function(' ------------------------ search_keyword_within_link_function function end ------------------------ ')
            return scrape_tracking_dict
            # ------------------------ attempt #3 force guess URL containing word end ------------------------
          else:
            localhost_print_function('not checking the url')
            pass
        except:
          localhost_print_function(f'company: {company_name} | website: {company_website} | does not contain url: {word}')
          pass
        localhost_print_function(f'company: {company_name} | website: {company_website} | does not contain link: {word}')
        pass
      # ------------------------ careers page attempts end ------------------------
    # Word does not exists on page
    else:
      localhost_print_function(f'company: {company_name} | website: {company_website} | does NOT contain word: {word}')
      pass
    # ------------------------ search driver page source end ------------------------


    try:
      # ------------------------ attempt #4 force careers page URL start ------------------------
      driver.get('https://' + company_website + '/careers')    # When click causes an error, check if URL works
      localhost_print_function(f'company: {company_name} | website: {company_website} | contains force url: {word}')
      count_true += 1
      if count_true == 1:
        scrape_tracking_dict[scrape_tracking_dict_item_to_change].append(True)
      scrape_tracking_dict['words_found_master_str'][-1] += scrape_tracking_dict_item_to_change + ': ' + word + ', '
      at_least_one_found = True
      localhost_print_function(f'company: {company_name} | website: {company_website} | contains link: {word}')
      localhost_print_function(f'breaking out of loop because of word: {word}')
      localhost_print_function(' ------------------------ search_keyword_within_link_function function end ------------------------ ')
      return scrape_tracking_dict
      # ------------------------ attempt #4 force careers page URL end ------------------------
    except:
      localhost_print_function(f'company: {company_name} | website: {company_website} | does not contain force url: {word}')
      pass
  # ------------------------ loop through keywords arr end ------------------------

  if at_least_one_found == False:
    scrape_tracking_dict[scrape_tracking_dict_item_to_change].append(False)
  localhost_print_function(' ------------------------ search_keyword_within_link_function function end ------------------------ ')
  return scrape_tracking_dict
  """
# ------------------------ search_keyword_within_link_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__search_keyword_within_link_function__':
#   search_keyword_within_link_function()
# ------------------------ call end ------------------------