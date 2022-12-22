# ------------------------ info about this file start ------------------------
# -routes = pages. Examples: [landing, about, faq, pricing] pages = routes
# -in this file we store the standard routes for our website
# -Note: any pages related to authentication will not be in this file, they will be routed in the auth.py file.
# -@login_required   # this decorator says that url cannot be accessed unless the user is logged in. 
# -@login_required: <-- This decorator will bring a user to __init__ code: [login_manager.login_view = 'auth.candidates_login_page_function'] if they hit a page that requires login and they are not logged in.
# -use code: <methods=['GET', 'POST']> when you want the user to interact with the page through forms/checkbox/textbox/radio/etc.
# ------------------------ info about this file end ------------------------


# ------------------------ imports start ------------------------
from website.backend.utils.printing import localhost_print_function
from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required, current_user, login_user
from website.backend.utils.user_inputs import sanitize_email_function, sanitize_password_function
from website.models import UserObj
from website import db
from website.backend.utils.send_emails import send_email_template_function
from werkzeug.security import generate_password_hash
from website.backend.utils.datetime import current_year_month_function
from website.backend.redis import redis_connect_to_database_function, redis_check_if_referral_cookie_exists_function
from website.backend.utils.browser import browser_response_set_referral_cookie_function
from website.backend.utils.user_inputs import sanitize_username_function
# ------------------------ imports end ------------------------


# ------------------------ function start ------------------------
views = Blueprint('views', __name__)
# ------------------------ function end ------------------------
# ------------------------ connect to redis start ------------------------
redis_connection = redis_connect_to_database_function()
# ------------------------ connect to redis end ------------------------

# ------------------------ individual route start ------------------------
@views.route('/')
def landing_index_page_function():
  localhost_print_function(' ------------------------ landing_index_page_function start ------------------------')
  localhost_print_function(' ------------------------ landing_index_page_function end ------------------------')
  return render_template('not_signed_in/landing/index.html', user=current_user)
# ------------------------ individual route end ------------------------

# ------------------------ individual route start ------------------------
@views.route('/reset', methods=['GET', 'POST'])
def forgot_password_page_function():
  localhost_print_function(' ------------------------ forgot_password_page_function start ------------------------')
  forgot_password_error_statement = ''
  if request.method == 'POST':
    # ------------------------ post request sent start ------------------------
    ui_email = request.form.get('uiEmail')
    # ------------------------ post request sent end ------------------------
    # ------------------------ sanitize/check user input email start ------------------------
    ui_email_cleaned = sanitize_email_function(ui_email)
    if ui_email_cleaned == False:
      forgot_password_error_statement = 'Please enter a valid work email.'
    # ------------------------ sanitize/check user input email end ------------------------
    # ------------------------ check if user email exists in db start ------------------------
    user_exists = UserObj.query.filter_by(email=ui_email).first()
    if user_exists:
      forgot_password_error_statement = 'Password reset link sent to email.'
      # ------------------------ send email with token url start ------------------------
      serializer_token_obj = UserObj.get_reset_token_function(self=user_exists)
      output_email = ui_email
      output_subject_line = 'Password Reset - ChangeFunders'
      output_message_content = f"To reset your password, visit the following link: http://127.0.0.1:80/reset/{serializer_token_obj} \n\nThis link will expire after 30 minutes.\nIf you did not make this request then simply ignore this email and no changes will be made."
      send_email_template_function(output_email, output_subject_line, output_message_content)
      # ------------------------ send email with token url end ------------------------
    else:
      forgot_password_error_statement = 'Password reset link sent to email.'
      pass
    # ------------------------ check if user email exists in db end ------------------------
  localhost_print_function(' ------------------------ forgot_password_page_function end ------------------------')
  return render_template('not_signed_in/password_forgot/index.html', user=current_user, error_message_to_html=forgot_password_error_statement)
# ------------------------ individual route end ------------------------

# ------------------------ individual route start ------------------------
@views.route('/reset/<token>', methods=['GET', 'POST'])
def candidates_reset_forgot_password_page_function(token):
  localhost_print_function(' ------------------------ candidates_reset_forgot_password_page_function start ------------------------')
  # if current_user.is_authenticated == False:
  #   return redirect(url_for('views.dashboard_test_login_page_function'))
  reset_password_error_statement = ''
  user_obj_from_token = UserObj.verify_reset_token_function(token)
  if user_obj_from_token is None:
    reset_password_error_statement = 'That is an invalid or expired token'
    localhost_print_function(' ------------------------ candidates_reset_forgot_password_page_function end ------------------------')
    return render_template('candidates_page_templates/not_logged_in_page_templates/forgot_password_page_templates/index.html', user=current_user, error_message_to_html=reset_password_error_statement)
  if request.method == 'POST':
    reset_password_error_statement = ''
    # ------------------------ get inputs from form start ------------------------
    ui_password = request.form.get('uiPassword')
    ui_password_confirmed = request.form.get('uiPasswordConfirm')
    # ------------------------ get inputs from form end ------------------------
    # ------------------------ check match start ------------------------
    if ui_password != ui_password_confirmed:
      reset_password_error_statement = 'Passwords do not match.'
    # ------------------------ check match end ------------------------
    # ------------------------ sanitize/check user input password start ------------------------
    ui_password_cleaned = sanitize_password_function(ui_password)
    if ui_password_cleaned == False:
      reset_password_error_statement = 'Password is not valid.'
    # ------------------------ sanitize/check user input password end ------------------------
    # ------------------------ sanitize/check user input password start ------------------------
    ui_password_confirmed_cleaned = sanitize_password_function(ui_password_confirmed)
    if ui_password_confirmed_cleaned == False:
      reset_password_error_statement = 'Password is not valid.'
    # ------------------------ sanitize/check user input password end ------------------------
    # ------------------------ update db start ------------------------
    if reset_password_error_statement == '':
      user_obj_from_token.password = generate_password_hash(ui_password, method="sha256")
      db.session.commit()
      return redirect(url_for('views_si.dashboard_page_function'))
    # ------------------------ update db end ------------------------
  localhost_print_function(' ------------------------ candidates_reset_forgot_password_page_function end ------------------------')
  return render_template('not_signed_in/password_reset/index.html', user=current_user, error_message_to_html=reset_password_error_statement)
# ------------------------ individual route end ------------------------

# ------------------------ individual route start ------------------------
@views.route('/proof', methods=['GET', 'POST'])
def proof_page_function():
  localhost_print_function(' ------------------------ proof_page_function start ------------------------')
  proof_error_statement=''
  ui_username = ''
  # ------------------------ redirect messages start ------------------------
  var1 = request.args.get('var1')
  if var1 == 'Username does not exist.':
    proof_error_statement = var1
  # ------------------------ redirect messages end ------------------------
  # ------------------------ post start ------------------------
  if request.method == 'POST':
    ui_username = request.form.get('uiUsername')
    # ------------------------ sanitize/check user input email start ------------------------
    ui_username_cleaned = sanitize_username_function(ui_username)
    if ui_username_cleaned == False:
      proof_error_statement = 'Please enter a valid username.'
    # ------------------------ sanitize/check user input email end ------------------------
    # ------------------------ check if user email already exists in db start ------------------------
    user_exists = UserObj.query.filter_by(username_db=ui_username.lower()).first()
    if user_exists:
      localhost_print_function(' ------------------------ proof_page_function end ------------------------ ')
      return redirect(url_for('views.i_proof_page_function', search_username=ui_username.lower()))
    else:
      proof_error_statement = 'Username does not exist.'
    # ------------------------ check if user email already exists in db start ------------------------
  # ------------------------ post end ------------------------
  localhost_print_function(' ------------------------ proof_page_function end ------------------------')
  return render_template('not_signed_in/proof/index.html', user=current_user, error_message_to_html=proof_error_statement, redirect_var_username=ui_username)
# ------------------------ individual route end ------------------------

# ------------------------ individual route start ------------------------
@views.route('/proof/<search_username>', methods=['GET', 'POST'])
def i_proof_page_function(search_username):
  localhost_print_function(' ------------------------ i_proof_page_function start ------------------------')
  proof_error_statement = ''
  # ------------------------ check if user exists start ------------------------
  user_exists = UserObj.query.filter_by(username_db=search_username.lower()).first()
  if user_exists:
    username = user_exists.username_db
    # ------------------------ temporary logic start ------------------------
    # This is temporary and should instead point to AWS s3 public bucket of the user's profile picture url location
    if username == 'ashley':
      img_url = '/static/images/proof/proof_ashley.png'
    elif username == 'sara':
      img_url = '/static/images/proof/proof_sara.png'
    elif username == 'olivia':
      img_url = '/static/images/proof/proof_olivia.png'
    else:
      img_url=''
    pass
    # ------------------------ temporary logic end ------------------------
    current_date_str = current_year_month_function()
  else:
    proof_error_statement = 'Username does not exist.'
    return redirect(url_for('views.proof_page_function', var1=proof_error_statement))
  # ------------------------ check if user exists end ------------------------
  localhost_print_function(' ------------------------ i_proof_page_function end ------------------------')
  # return render_template('not_signed_in/proof/individual/index.html', user=current_user, img_url_to_html=img_url, current_date_str_to_html=current_date_str, username_to_html=username)
  template_location_url = 'not_signed_in/proof/individual/index.html'
  # ------------------------ auto set cookie start ------------------------
  get_referral_cookie_value_from_browser = redis_check_if_referral_cookie_exists_function()
  if get_referral_cookie_value_from_browser != None:
    redis_connection.set(get_referral_cookie_value_from_browser, username.encode('utf-8'))
    localhost_print_function(' ------------------------ i_proof_page_function end ------------------------')
    return render_template(template_location_url, user=current_user, img_url_to_html=img_url, current_date_str_to_html=current_date_str, username_to_html=username)
  else:
    browser_response = browser_response_set_referral_cookie_function(current_user, template_location_url, img_url, current_date_str, username)
    localhost_print_function(' ------------------------ i_proof_page_function end ------------------------')
    return browser_response
  # ------------------------ auto set cookie end ------------------------
# ------------------------ individual route end ------------------------

# ------------------------ individual route start ------------------------
@views.route('/about')
def about_page_function():
  localhost_print_function(' ------------------------ about_page_function start ------------------------')
  localhost_print_function(' ------------------------ about_page_function end ------------------------')
  return render_template('not_signed_in/about/index.html', user=current_user)
# ------------------------ individual route end ------------------------

# ------------------------ individual route start ------------------------
@views.route('/blog')
def blog_page_function():
  localhost_print_function(' ------------------------ blog_page_function start ------------------------')
  localhost_print_function(' ------------------------ blog_page_function end ------------------------')
  return render_template('not_signed_in/blog/index.html', user=current_user)
# ------------------------ individual route end ------------------------

# ------------------------ individual route start ------------------------
@views.route('/blog/<i_blog_post_num>')
def blog_i_page_function(i_blog_post_num):
  localhost_print_function(' ------------------------ blog_i_page_function start ------------------------')
  localhost_print_function(' ------------------------ blog_i_page_function end ------------------------')
  return render_template(f'not_signed_in/blog/blog_i/{i_blog_post_num}.html', user=current_user)
# ------------------------ individual route end ------------------------

# ------------------------ individual route start ------------------------
@views.route('/faq')
def faq_page_function():
  localhost_print_function(' ------------------------ faq_page_function start ------------------------')
  localhost_print_function(' ------------------------ faq_page_function end ------------------------')
  return render_template('not_signed_in/faq/index.html', user=current_user)
# ------------------------ individual route end ------------------------