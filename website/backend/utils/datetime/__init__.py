# ------------------------ imports start ------------------------
from website.backend.utils.printing import localhost_print_function
from datetime import date
# ------------------------ imports end ------------------------

localhost_print_function(' ------------------------ __init__ datetime start ------------------------')
# ------------------------ individual function start ------------------------
def current_year_month_function():
  localhost_print_function(' ------------------------ current_year_month_function start ------------------------')
  # ------------------------ month dict start ------------------------
  month_dict = {
    '1' : 'January',
    '2' : 'February',
    '3' : 'March',
    '4' : 'April',
    '5' : 'May',
    '6' : 'June',
    '7' : 'July',
    '8' : 'August',
    '9' : 'September',
    '10' : 'October',
    '11' : 'November',
    '12' : 'December'
  }
  # ------------------------ month dict end ------------------------
  # ------------------------ today start ------------------------
  todays_date = date.today()
  current_year = str(todays_date.year)
  current_month = str(todays_date.month)
  current_month_long = month_dict[current_month]
  current_date_str = current_month_long + ', ' + current_year
  # ------------------------ today end ------------------------
  localhost_print_function(' ------------------------ current_year_month_function end ------------------------')
  return current_date_str
# ------------------------ individual function end ------------------------
localhost_print_function(' ------------------------ __init__ datetime end ------------------------')