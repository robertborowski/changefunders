# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import csv
# ------------------------ imports end ------------------------


# ------------------------ get_output_category_dict_function function start ------------------------
def get_output_category_dict_function():
  localhost_print_function(' ------------------------ get_output_category_dict_function function start ------------------------ ')

  # ------------------------ automated dict start ------------------------
  filename = 'backend/csv/input/keywords.csv'
  category_match_dict = {}

  with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    next(datareader)    # skip first row in csv
    for row in datareader:
      category_match_dict[row[2]] = row[3]
  # ------------------------ automated dict end ------------------------

  # # ------------------------ old manual process start ------------------------
  # category_match_dict = {
  #   'Fitness': 'Health & Wellness',
  #   'Health & Wellness': 'Health & Wellness',
  #   'Wellness': 'Health & Wellness',
  #   'Wellbeing': 'Health & Wellness',
  #   'Gym': 'Health & Wellness',
  #   'Work From Home': 'Work From Home',
  #   'WFH': 'Work From Home',
  #   'Desk': 'Work From Home',
  #   'Internet': 'Work From Home',
  #   'Monitor': 'Work From Home',
  #   'Remote': 'Work From Home',
  #   'Professional development': 'Learning & Development',
  #   'Skill development': 'Learning & Development',
  #   'Learning': 'Learning & Development',
  #   'Courses': 'Learning & Development',
  #   'Learning & Development': 'Learning & Development',
  #   'L&D': 'Learning & Development',
  #   'Education': 'Learning & Development'
  # }
  # # ------------------------ old manual process end ------------------------

  localhost_print_function(' ------------------------ get_output_category_dict_function function end ------------------------ ')
  return category_match_dict
# ------------------------ get_output_category_dict_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__close_out_scrape_tracking_dict_based_reruns_function__':
#   get_output_category_dict_function()
# ------------------------ call end ------------------------