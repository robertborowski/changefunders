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
from website.backend.redis import redis_connect_to_database_function, redis_check_if_cookie_exists_function
from website.backend.utils.browser import browser_response_set_cookie_function
import os
from website.backend.utils.uuid_and_timestamp import create_uuid_function
from website.backend.utils.aws_s3 import change_uploaded_image_filename_function, user_upload_image_checks_aws_s3_function
# ------------------------ imports end ------------------------


# ------------------------ function start ------------------------
views_si = Blueprint('views_si', __name__)
# ------------------------ function end ------------------------
# ------------------------ connect to redis start ------------------------
redis_connection = redis_connect_to_database_function()
# ------------------------ connect to redis end ------------------------

# ------------------------ individual route start ------------------------
@views_si.route('/dashboard')
@login_required
def dashboard_page_function():
  localhost_print_function(' ------------------------ dashboard_page_function start ------------------------')
  template_location_url = 'signed_in/dashboard/index.html'
  # ------------------------ auto set cookie start ------------------------
  get_cookie_value_from_browser = redis_check_if_cookie_exists_function()
  if get_cookie_value_from_browser != None:
    redis_connection.set(get_cookie_value_from_browser, current_user.id.encode('utf-8'))
    localhost_print_function(' ------------------------ dashboard_page_function end ------------------------')
    return render_template(template_location_url, user=current_user)
  else:
    browser_response = browser_response_set_cookie_function(current_user, template_location_url)
    localhost_print_function(' ------------------------ dashboard_page_function end ------------------------')
    return browser_response
  # ------------------------ auto set cookie end ------------------------
# ------------------------ individual route end ------------------------

# ------------------------ individual route start ------------------------
@views_si.route('/account', methods=['GET', 'POST'])
@login_required
def account_page_function():
  localhost_print_function(' ------------------------ account_page_function start ------------------------')
  if request.method == 'POST':
    # ------------------------ ui uploaded image start ------------------------
    # ------------------------ define variable for insert start ------------------------
    final_id = create_uuid_function('profile_img_')
    # ------------------------ define variable for insert end ------------------------
    uploaded_image_aws_url = ''
    uploaded_image_uuid = ''
    try:
      if request.files:
        if "filesize" in request.cookies:
          # ------------------------ ui file start ------------------------
          image = request.files["uiImageUpload"]
          # ------------------------ ui file end ------------------------
          # ------------------------ if no image attached start ------------------------
          if image.filename == '' or image.filename == ' ' or image.filename == None:
            ui_question_error_statement = 'Question must contain an image.'
            localhost_print_function(' ------------------------ account_page_function end ------------------------')
            return render_template('signed_in/account/index.html', user=current_user)
          # ------------------------ if no image attached end ------------------------
          # ------------------------ if image attached start ------------------------
          else:
            # Keep track of the original filename that someone is uploading
            upload_image_original_filename = image.filename
            # Create image uuid to store in aws
            uploaded_image_uuid = '_user_uploaded_image_' + final_id
            # Change the name of the image from whatever the user uploaded to the question uuid as name
            image = change_uploaded_image_filename_function(image, uploaded_image_uuid)
            # Get image filesize
            file_size = request.cookies["filesize"]
            # Check and upload the user file image
            user_image_upload_status = user_upload_image_checks_aws_s3_function(image, file_size)
            # ------------------------ if image checks fail start ------------------------
            if user_image_upload_status == False:
              localhost_print_function(' ------------------------ account_page_function end ------------------------')
              return render_template('signed_in/account/index.html', user=current_user)
            # ------------------------ if image checks fail end ------------------------
            # Finalize image variables
            uploaded_image_aws_url = 'https://' + os.environ.get('AWS_CHANGEFUNDERS_BUCKET_NAME') + '.s3.' + os.environ.get('AWS_TRIVIAFY_REGION') + '.amazonaws.com/' + image.filename
          # ------------------------ if image attached end ------------------------
    except:
      localhost_print_function('did not upload img')
      pass
    # ------------------------ ui uploaded image end ------------------------
  localhost_print_function(' ------------------------ account_page_function end ------------------------')
  return render_template('signed_in/account/index.html', user=current_user)
# ------------------------ individual route end ------------------------