# ------------------------ imports start ------------------------
from website.backend.utils.printing import localhost_print_function
from website.backend.postgres import postgres_connect_to_database_function
from website.backend.postgres import postgres_close_connection_to_database_function
from jobs.db_cleanup_jobs import job_candidates_clean_out_redis_function
# ------------------------ imports end ------------------------

# ------------------------ main start ------------------------
def job_caller_function():
  localhost_print_function(' ------------------------ job_caller_function start ------------------------ ')
  # ------------------------ Connect to Postgres DB START ------------------------
  postgres_connection, postgres_cursor = postgres_connect_to_database_function()
  # ------------------------ Connect to Postgres DB END ------------------------

  # ------------------------ remove users start ------------------------
  # job_candidates_remove_unsub_user_all_tables_function(postgres_connection, postgres_cursor)
  job_candidates_clean_out_redis_function(postgres_connection, postgres_cursor)
  # ------------------------ remove users end ------------------------

  # ------------------------ Close Postgres DB START ------------------------
  postgres_close_connection_to_database_function(postgres_connection, postgres_cursor)
  # ------------------------ Close Postgres DB END ------------------------
  localhost_print_function(' ------------------------ job_caller_function end ------------------------ ')
  return True
# ------------------------ main end ------------------------

# ------------------------ run main start ------------------------
if __name__ == "__main__":
  job_caller_function()
# ------------------------ run main end ------------------------