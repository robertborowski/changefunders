# ------------------------ imports start ------------------------
import os
# from website.backend.utils.printing import localhost_print_function
# ------------------------ imports end ------------------------

print(' ------------------------ __init__ printing start ------------------------')
# ------------------------ individual function start ------------------------
def localhost_print_function(input_value_to_print):
  server_env = os.environ.get('TESTING', 'false')
  if server_env and server_env == 'true':
    print(input_value_to_print)
  return None
# ------------------------ individual function end ------------------------
print(' ------------------------ __init__ printing end ------------------------')