# ------------------------ imports start ------------------------
import os
# ------------------------ imports end ------------------------


# ------------------------ main function start ------------------------
def localhost_print_function(input_value_to_print):
  server_env = os.environ.get('TESTING', 'false')
  
  if server_env and server_env == 'true':
    print(input_value_to_print)
  
  return None
  # ------------------------ main function end ------------------------