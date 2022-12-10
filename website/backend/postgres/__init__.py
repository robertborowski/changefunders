# ------------------------ imports start ------------------------
from website.backend.utils.printing import localhost_print_function
import psycopg2
import os
# ------------------------ imports end ------------------------

localhost_print_function(' ------------------------ __init__ postgres start ------------------------')
# ------------------------ individual function start ------------------------
def postgres_connect_to_database_function():
  localhost_print_function(' ------------------------ postgres_connect_to_database_function start ------------------------ ')
  # Heroku Postgres connection
  DATABASE_URL = os.environ.get('DATABASE_URL')
  postgres_connection = psycopg2.connect(DATABASE_URL, sslmode='require')
  postgres_cursor = postgres_connection.cursor()
  localhost_print_function(' ------------------------ postgres_connect_to_database_function end ------------------------ ')
  return postgres_connection, postgres_cursor
# ------------------------ individual function end ------------------------

# ------------------------ individual function start ------------------------
def postgres_close_connection_to_database_function(postgres_connection, postgres_cursor):
  localhost_print_function(' ------------------------ postgres_close_connection_to_database_function start ------------------------ ')
  postgres_cursor.close()
  postgres_connection.close()
  localhost_print_function(' ------------------------ postgres_close_connection_to_database_function end ------------------------ ')
# ------------------------ individual function end ------------------------
localhost_print_function(' ------------------------ __init__ postgres end ------------------------')