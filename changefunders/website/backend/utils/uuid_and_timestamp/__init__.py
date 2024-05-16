# ------------------------ imports start ------------------------
from website.backend.utils.printing import localhost_print_function
import uuid
from datetime import datetime
import os, time
import random
import string
# ------------------------ imports end ------------------------

localhost_print_function(' ------------------------ __init__ uuid_and_timestamp start ------------------------')
# ------------------------ individual function start ------------------------
def create_uuid_function(table_prefix):
  localhost_print_function(' ------------------------ create_uuid_function start ------------------------')
  localhost_print_function(' ------------------------ create_uuid_function end ------------------------')
  return table_prefix + str(uuid.uuid4())
# ------------------------ individual function end ------------------------

# ------------------------ individual function start ------------------------
def create_timestamp_function():
  localhost_print_function(' ------------------------ create_timestamp_function start ------------------------')
  os.environ['TZ'] = 'US/Eastern'
  time.tzset()
  localhost_print_function(' ------------------------ create_timestamp_function end ------------------------')
  return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# ------------------------ individual function end ------------------------

# ------------------------ individual function start ------------------------
def generate_username_uuid_function(num_characters):
  localhost_print_function(' ------------------------ generate_username_uuid_function start ------------------------')
  localhost_print_function(' ------------------------ generate_username_uuid_function end ------------------------')
  generated_value = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num_characters))
  return generated_value
# ------------------------ individual function end ------------------------
localhost_print_function(' ------------------------ __init__ uuid_and_timestamp end ------------------------')