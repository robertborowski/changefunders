# ------------------------ imports start ------------------------
from website.backend.utils.printing import localhost_print_function
import uuid
from datetime import datetime
import os, time
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
localhost_print_function(' ------------------------ __init__ uuid_and_timestamp end ------------------------')