# ------------------------ imports start ------------------------
from website.backend.utils.printing import localhost_print_function
from website.backend.redis import redis_connect_to_database_function, redis_set_browser_cookie_function, redis_set_referral_browser_cookie_function
from flask import Blueprint, render_template, request, make_response
import datetime
# ------------------------ imports end ------------------------

localhost_print_function(' ------------------------ __init__ browser start ------------------------')
# ------------------------ connect to redis start ------------------------
redis_connection = redis_connect_to_database_function()
# ------------------------ connect to redis end ------------------------

# ------------------------ individual function start ------------------------
def browser_response_set_cookie_function(current_user, input_template_url):
  localhost_print_function(' ------------------------ browser_response_set_cookie_function START ------------------------ ')
  set_browser_cookie_key, set_browser_cookie_value = redis_set_browser_cookie_function()
  browser_response = make_response(render_template(input_template_url, user=current_user))
  browser_response.set_cookie(set_browser_cookie_key, set_browser_cookie_value, expires=datetime.datetime.now() + datetime.timedelta(days=60))
  redis_connection.set(set_browser_cookie_value, current_user.id.encode('utf-8'))
  localhost_print_function(' ------------------------ browser_response_set_cookie_function END ------------------------ ')
  return browser_response
# ------------------------ individual function end ------------------------

# ------------------------ individual function start ------------------------
def browser_response_set_referral_cookie_function(current_user, input_template_url, img_url, current_date_str, username):
  localhost_print_function(' ------------------------ browser_response_set_referral_cookie_function START ------------------------ ')
  set_browser_cookie_key, set_browser_cookie_value = redis_set_referral_browser_cookie_function()
  browser_response = make_response(render_template(input_template_url, user=current_user, img_url_to_html=img_url, current_date_str_to_html=current_date_str, username_to_html=username))
  browser_response.set_cookie(set_browser_cookie_key, set_browser_cookie_value, expires=datetime.datetime.now() + datetime.timedelta(days=60))
  redis_connection.set(set_browser_cookie_value, username.encode('utf-8'))
  localhost_print_function(' ------------------------ browser_response_set_referral_cookie_function END ------------------------ ')
  return browser_response
# ------------------------ individual function end ------------------------
localhost_print_function(' ------------------------ __init__ browser end ------------------------')