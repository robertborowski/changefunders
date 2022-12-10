# ------------------------ imports start ------------------------
from website.backend.utils.printing import localhost_print_function
from website.backend.redis import redis_connect_to_database_function
from website.backend.utils.sql_scripts import select_general_v1_jobs_function
# ------------------------ imports end ------------------------

localhost_print_function(' ------------------------ __init__ db_cleanup_jobs start ------------------------')
# ------------------------ individual function start ------------------------
def job_candidates_clean_out_redis_function(postgres_connection, postgres_cursor):
  localhost_print_function(' ------------------------ job_candidates_clean_out_redis_function start ------------------------ ')
  # ------------------------ get all current user id's as set start ------------------------
  sql_input = 'user_obj'
  query_result_arr_of_dicts = select_general_v1_jobs_function(postgres_connection, postgres_cursor, 'select_table1_id', additional_input=sql_input)
  user_ids_set = {'a'}
  for i in query_result_arr_of_dicts:
    if i['id'] not in user_ids_set:
      user_ids_set.add(i['id'])
  user_ids_set.remove('a')
  # ------------------------ get all current user id's as set end ------------------------
  # ------------------------ loop through redis start ------------------------
  # Connect to redis database pool (no need to close)
  redis_connection = redis_connect_to_database_function()
  redis_keys = redis_connection.keys()
  redis_candidates_deleted_counter = 0
  for key in redis_keys:
    if 'cfkey' in str(key):
      value = redis_connection.get(key).decode('utf-8')
      print(f'key: {key} | value: {value}')
      if value not in user_ids_set:
        # redis_connection.delete(key)
        redis_candidates_deleted_counter += 1
  localhost_print_function(f'redis_candidates_deleted_counter: {redis_candidates_deleted_counter}')
  # ------------------------ loop through redis end ------------------------
  localhost_print_function(' ------------------------ job_candidates_clean_out_redis_function start ------------------------ ')
  return True
# ------------------------ individual function end ------------------------
localhost_print_function(' ------------------------ __init__ db_cleanup_jobs end ------------------------')