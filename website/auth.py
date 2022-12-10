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
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from website import db
from .models import UserObj, CollectEmailObj
from website.backend.utils.user_inputs import sanitize_email_function, sanitize_password_function
from website.backend.utils.uuid_and_timestamp import create_uuid_function, create_timestamp_function, generate_username_uuid_function
from werkzeug.security import generate_password_hash, check_password_hash
import os
# ------------------------ imports end ------------------------


# ------------------------ function start ------------------------
auth = Blueprint('auth', __name__)
# ------------------------ function end ------------------------

# ------------------------ individual route start ------------------------
@auth.route('/signup', methods=['GET', 'POST'])
def signup_function():
  localhost_print_function(' ------------------------ signup_function start ------------------------ ')
  sign_up_error_message = ''
  if request.method == 'POST':
    # ------------------------ post method hit #1 - various pages start ------------------------
    ui_email = request.form.get('uiEmailVariousPages1')
    if ui_email != None:
      # ------------------------ sanitize/check user input email start ------------------------
      ui_email_cleaned = sanitize_email_function(ui_email)
      if ui_email_cleaned == False:
        sign_up_error_message = 'Please enter a valid email.'
      # ------------------------ sanitize/check user input email end ------------------------
      # ------------------------ check if email already exists in db start ------------------------
      email_exists = CollectEmailObj.query.filter_by(email=ui_email).first()
      # ------------------------ check if email already exists in db end ------------------------
      # ------------------------ create new signup in db start ------------------------
      if not email_exists and sign_up_error_message == '':
        new_email = CollectEmailObj(
          id=create_uuid_function('collect_email_'),
          created_timestamp=create_timestamp_function(),
          email=ui_email
        )
        db.session.add(new_email)
        db.session.commit()
      # ------------------------ create new signup in db end ------------------------
      localhost_print_function('user is being redirected to full sign up page')
      localhost_print_function(' ------------------------ signup_function end ------------------------ ')
      return render_template('candidates_page_templates/not_logged_in_page_templates/create_account_templates/index.html', user=current_user, redirect_var_email = ui_email, error_message_to_html = sign_up_error_message)
    # ------------------------ post method hit #1 - various pages end ------------------------
    # ------------------------ post method hit #2 - sign up page only start ------------------------
    ui_email = request.form.get('uiEmail')
    ui_password = request.form.get('uiPassword')
    # ------------------------ sanitize/check user inputs start ------------------------
    # ------------------------ sanitize/check user input email start ------------------------
    ui_email_cleaned = sanitize_email_function(ui_email)
    if ui_email_cleaned == False:
      sign_up_error_message = 'Please enter a valid email.'
    # ------------------------ sanitize/check user input email end ------------------------
    # ------------------------ sanitize/check user input password start ------------------------
    ui_password_cleaned = sanitize_password_function(ui_password)
    if ui_password_cleaned == False:
      sign_up_error_message = 'Password is not valid.'
    # ------------------------ sanitize/check user input password end ------------------------
    # ------------------------ sanitize/check user inputs end ------------------------
    # ------------------------ if user input error start ------------------------
    if sign_up_error_message != '':
      localhost_print_function(' ------------------------ signup_function end ------------------------ ')
      return render_template('not_signed_in/sign_up/index.html',
                              user=current_user,
                              error_message_to_html=sign_up_error_message,
                              redirect_var_email=ui_email,
                              redirect_var_password=ui_password)
    # ------------------------ if user input error end ------------------------
    # ------------------------ check if user email already exists in db start ------------------------
    user_exists = UserObj.query.filter_by(email=ui_email).first()
    if user_exists:
      sign_up_error_message = 'Account already created for email.'
      localhost_print_function(' ------------------------ signup_function end ------------------------ ')
      return render_template('not_signed_in/sign_up/index.html',
                              user=current_user,
                              error_message_to_html=sign_up_error_message,
                              redirect_var_email=ui_email,
                              redirect_var_password=ui_password)
    # ------------------------ check if user email already exists in db start ------------------------
    else:
      # ------------------------ generate unique username start ------------------------
      randomly_generated_username = generate_username_uuid_function(6)
      username_exists = UserObj.query.filter_by(username=randomly_generated_username).first()
      while username_exists != None:
        randomly_generated_username = generate_username_uuid_function(6)
        username_exists = UserObj.query.filter_by(username=randomly_generated_username).first()
      # ------------------------ generate unique username end ------------------------
      # ------------------------ create new user in db start ------------------------
      new_user = UserObj(
        id=create_uuid_function('user_'),
        created_timestamp=create_timestamp_function(),
        email=ui_email,
        phone=None,
        password=generate_password_hash(ui_password, method="sha256"),
        name=None,
        username=randomly_generated_username,
        fk_stripe_customer_id=None,
        fk_stripe_subscription_id=None
      )
      db.session.add(new_user)
      db.session.commit()
      # ------------------------ create new user in db end ------------------------
      # ------------------------ keep user logged in start ------------------------
      login_user(new_user, remember=True)
      # ------------------------ keep user logged in end ------------------------
      """
      # ------------------------ email self start ------------------------
      try:
        output_to_email = os.environ.get('TRIVIAFY_NOTIFICATIONS_EMAIL')
        output_subject = f'Triviafy - Signup - {ui_email}'
        output_body = f"Hi there,\n\nNew user signed up: {ui_email} \n\nBest,\nTriviafy"
        send_email_template_function(output_to_email, output_subject, output_body)
      except:
        pass
      # ------------------------ email self end ------------------------
      """
      localhost_print_function(' ------------------------ signup_function end ------------------------ ')
      return redirect(url_for('views_si.dashboard_page_function'))
    # ------------------------ post method hit #2 - sign up page only end ------------------------

  localhost_print_function(' ------------------------ signup_function end ------------------------ ')
  return render_template('not_signed_in/sign_up/index.html',user=current_user,error_message_to_html=sign_up_error_message)
# ------------------------ individual route end ------------------------

"""
# ------------------------ individual route start ------------------------
@auth.route('/logout')
@login_required
def logout_function():
  localhost_print_function(' ------------------------ logout_function start ------------------------ ')
  logout_user()
  # ------------------------ auto sign in with cookie start ------------------------
  get_cookie_value_from_browser = redis_check_if_cookie_exists_function()
  # ------------------------ auto sign in with cookie end ------------------------
  if get_cookie_value_from_browser != None:
    try:
      redis_connection.delete(get_cookie_value_from_browser)
    except:
      pass
  # ------------------------ auto sign in with cookie end ------------------------
  localhost_print_function(' ------------------------ logout_function end ------------------------ ')
"""