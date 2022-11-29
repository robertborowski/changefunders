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
# ------------------------ imports end ------------------------


# ------------------------ function start ------------------------
blog = Blueprint('blog', __name__)
# ------------------------ function end ------------------------

# ------------------------ individual route start ------------------------
@blog.route('/test2')
def landing_index_page_function():
  localhost_print_function(' ------------------------- landing_index_page_function start -------------------------')
  localhost_print_function(' ------------------------- landing_index_page_function end -------------------------')
  return render_template('not_signed_in/landing/index.html', user=current_user)
# ------------------------ individual route end ------------------------