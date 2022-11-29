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
from website.backend.utils.user_inputs import sanitize_email_function
# ------------------------ imports end ------------------------


# ------------------------ function start ------------------------
auth = Blueprint('auth', __name__)
# ------------------------ function end ------------------------

# ------------------------ individual route start ------------------------
@auth.route('/signup', methods=['GET', 'POST'])
def signup_function():
  localhost_print_function(' ------------------------ signup_function start ------------------------ ')
  create_account_error_statement = ''
  """
  if request.method == 'POST':
    # ------------------------ post method hit #1 - quick sign up start ------------------------
    ui_email = request.form.get('various_pages1_ui_email')
    if ui_email != None:
      # ------------------------ sanitize/check user input email start ------------------------
      ui_email_cleaned = sanitize_email_function(ui_email)
      if ui_email_cleaned == False:
        create_account_error_statement = 'Please enter a valid work email.'
      # ------------------------ sanitize/check user input email end ------------------------
      # ------------------------ check if email already exists in db start ------------------------
      email_exists = CandidatesCollectEmailObj.query.filter_by(email=ui_email).first()
      # ------------------------ check if email already exists in db end ------------------------
      # ------------------------ create new signup in db start ------------------------
      if not email_exists and create_account_error_statement == '':
        new_email = CandidatesCollectEmailObj(
          id=create_uuid_function('collect_email_'),
          created_timestamp=create_timestamp_function(),
          email=ui_email
        )
        db.session.add(new_email)
        db.session.commit()
      # ------------------------ create new signup in db end ------------------------
      localhost_print_function('user is being redirected to full sign up page')
      localhost_print_function(' ------------------------ signup_function end ------------------------ ')
      return render_template('candidates_page_templates/not_logged_in_page_templates/create_account_templates/index.html', user=current_user, redirect_var_email = ui_email, error_message_to_html = create_account_error_statement)
    # ------------------------ post method hit #1 - quick sign up end ------------------------
    # ------------------------ post method hit #2 - full sign up start ------------------------
    ui_email = request.form.get('create_account_page_ui_email')
    ui_password = request.form.get('create_account_page_ui_password')
    ui_name = request.form.get('create_account_page_ui_name')
    ui_company_name = request.form.get('create_account_page_ui_company_name')
    # ------------------------ sanitize/check user inputs start ------------------------
    # ------------------------ sanitize/check user input email start ------------------------
    ui_email_cleaned = sanitize_email_function(ui_email)
    if ui_email_cleaned == False:
      create_account_error_statement = 'Please enter a valid work email.'
    # ------------------------ sanitize/check user input email end ------------------------
    # ------------------------ sanitize/check user input password start ------------------------
    ui_password_cleaned = sanitize_password_function(ui_password)
    if ui_password_cleaned == False:
      create_account_error_statement = 'Password is not valid.'
    # ------------------------ sanitize/check user input password end ------------------------
    # ------------------------ sanitize/check user input name start ------------------------
    if len(ui_name) > 20:
      create_account_error_statement = 'Name can only be 2-20 characters.'
    ui_name_cleaned = sanitize_create_account_text_inputs_function(ui_name)
    if ui_name_cleaned == False:
      create_account_error_statement = 'Name needs to be 2-20 characters. No special characters.'
    # ------------------------ sanitize/check user input name end ------------------------
    # ------------------------ sanitize/check user input company name start ------------------------
    if len(ui_company_name) < 2 or len(ui_company_name) > 50:
      create_account_error_statement = 'Company name needs to be 2-20 characters.'
    ui_company_name_cleaned = sanitize_create_account_text_inputs_function(ui_company_name)
    if ui_company_name_cleaned == False:
      create_account_error_statement = 'Company name needs to be 2-20 characters. No special characters.'
    # ------------------------ sanitize/check user input company name end ------------------------
    # ------------------------ sanitize/check user inputs end ------------------------
    # ------------------------ if user input error start ------------------------
    if create_account_error_statement != '':
      localhost_print_function(' ------------------------ signup_function end ------------------------ ')
      return render_template('candidates_page_templates/not_logged_in_page_templates/create_account_templates/index.html',
                              user = current_user,
                              error_message_to_html = create_account_error_statement,
                              redirect_var_email = ui_email,
                              redirect_var_password = ui_password,
                              redirect_var_first_name = ui_name,
                              redirect_var_company_name = ui_company_name)
    # ------------------------ if user input error end ------------------------
    # ------------------------ check if user email already exists in db start ------------------------
    user = CandidatesUserObj.query.filter_by(email=ui_email).first()
    if user:
      create_account_error_statement = 'Account already created for email.'
      localhost_print_function(' ------------------------ signup_function end ------------------------ ')
      return render_template('candidates_page_templates/not_logged_in_page_templates/create_account_templates/index.html',
                              user = current_user,
                              error_message_to_html = create_account_error_statement,
                              redirect_var_email = ui_email,
                              redirect_var_password = ui_password,
                              redirect_var_first_name = ui_name,
                              redirect_var_company_name = ui_company_name)
    # ------------------------ check if user email already exists in db start ------------------------
    else:
      # ------------------------ create new user in db start ------------------------
      new_user = CandidatesUserObj(
        id=create_uuid_function('user_'),
        created_timestamp=create_timestamp_function(),
        email=ui_email,
        password=generate_password_hash(ui_password, method="sha256"),
        name = ui_name,
        company_name = ui_company_name
      )
      db.session.add(new_user)
      db.session.commit()
      # ------------------------ create new user in db end ------------------------
      # ------------------------ keep user logged in start ------------------------
      login_user(new_user, remember=True)
      # ------------------------ keep user logged in end ------------------------
      # ------------------------ email self start ------------------------
      try:
        output_to_email = os.environ.get('TRIVIAFY_NOTIFICATIONS_EMAIL')
        output_subject = f'Triviafy - Signup - {ui_email}'
        output_body = f"Hi there,\n\nNew user signed up: {ui_email} \n\nBest,\nTriviafy"
        send_email_template_function(output_to_email, output_subject, output_body)
      except:
        pass
      # ------------------------ email self end ------------------------
      localhost_print_function(' ------------------------ signup_function end ------------------------ ')
      return redirect(url_for('views.dashboard_test_login_page_function'))
    # ------------------------ post method hit #2 - full sign up end ------------------------
    """

  localhost_print_function(' ------------------------ signup_function end ------------------------ ')
  return render_template('not_signed_in/sign_up/index.html',user=current_user,error_message_to_html=create_account_error_statement)
# ------------------------ individual route end ------------------------