# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import re
# ------------------------ imports end ------------------------


# ------------------------ sanitize_replace_space_remove_special_function function start ------------------------
def sanitize_replace_space_remove_special_function(word):
  # localhost_print_function(' ------------------------ sanitize_replace_space_remove_special_function function start ------------------------ ')
  # ------------------------ sanitize start ------------------------
  word = word.strip()
  word = word.replace(' ','_')
  word = re.sub('[^A-Za-z0-9_]+','', word)
  word = word.lower()
  # ------------------------ sanitize end ------------------------
  # localhost_print_function(' ------------------------ sanitize_replace_space_remove_special_function function end ------------------------ ')
  return word
# ------------------------ sanitize_replace_space_remove_special_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__sanitize_replace_space_remove_special_function__':
#   sanitize_replace_space_remove_special_function()
# ------------------------ call end ------------------------