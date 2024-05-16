# ------------------------ imports start ------------------------
import os
from website.backend.utils.printing import localhost_print_function
import boto3
# ------------------------ imports end ------------------------

print(' ------------------------ __init__ aws_s3 start ------------------------')
# ------------------------ individual function start ------------------------
def change_uploaded_image_filename_function(image, uploaded_image_uuid):
  print(' ------------------------ change_uploaded_image_filename_function start ------------------------')
  # Get the filename
  filename = image.filename
  # Split the filename by '.'
  filename_parts_arr = filename.split('.')
  # Replace the first part of the filename
  filename_parts_arr[0] = uploaded_image_uuid
  # Join it back together
  filename = ".".join(filename_parts_arr)
  # Assign to the image filename
  image.filename = filename
  print(' ------------------------ change_uploaded_image_filename_function end ------------------------')
  return image
# ------------------------ individual function end ------------------------

# ------------------------ individual function start ------------------------
def allowed_image_filesize_function(filesize, max_image_filesize_value):
  print(' ------------------------ allowed_image_filesize_function start ------------------------')
  if int(filesize) <= max_image_filesize_value:
    print(' ------------------------ allowed_image_filesize_function end ------------------------')
    return True
  else:
    print(' ------------------------ allowed_image_filesize_function end ------------------------')
    return False
# ------------------------ individual function end ------------------------

# ------------------------ individual function start ------------------------
def allowed_images_function(filename, allowed_image_extensions_arr):
  print(' ------------------------ allowed_images_function start ------------------------')
  # We only want files with a . in the filename
  if not "." in filename:
    print(' ------------------------ allowed_images_function end ------------------------')
    return False
  # Split the extension from the filename
  ext = filename.rsplit(".", 1)[1]
  # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
  if ext.upper() in allowed_image_extensions_arr:
    print(' ------------------------ allowed_images_function end ------------------------')
    return True
  else:
    print(' ------------------------ allowed_images_function end ------------------------')
    return False
# ------------------------ individual function end ------------------------

# ------------------------ individual function start ------------------------
def upload_image_aws_s3_function(image_obj):
  print(' ------------------------ upload_image_aws_s3_function start ------------------------')
  # Env variables
  aws_s3_bucket = os.environ.get('AWS_CHANGEFUNDERS_BUCKET_NAME')
  aws_s3_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
  aws_s3_key_secret = os.environ.get('AWS_SECRET_ACCESS_KEY')
  
  s3 = boto3.client("s3",
                    aws_access_key_id = aws_s3_key_id,
                    aws_secret_access_key = aws_s3_key_secret)

  # Try the upload to AWS s3 bucket
  try:
    s3.upload_fileobj(image_obj, aws_s3_bucket, image_obj.filename, ExtraArgs={"ContentType": image_obj.content_type})
    print('image stored in aws s3!')
    print(' ------------------------ upload_image_aws_s3_function end ------------------------')
  except Exception as e:
    # This is a catch all exception, edit this part to fit your needs.
    print('Something Happened: ', e)
    print(' ------------------------ upload_image_aws_s3_function end ------------------------')
    return e
# ------------------------ individual function end ------------------------

# ------------------------ individual function start ------------------------
def user_upload_image_checks_aws_s3_function(image, file_size):
  print(' ------------------------ user_upload_image_checks_aws_s3_function start ------------------------')
  # Set the parameters for accepting image upload
  allowed_image_extensions_arr = ["JPEG", "JPG", "PNG"]
  max_image_filesize_value = 50 * 1024 * 1024
  # Ensuring the filesize is allowed
  if not allowed_image_filesize_function(file_size, max_image_filesize_value):
    localhost_print_function('Filesize exceeded maximum limit (50 MB)')
    print(' ------------------------ user_upload_image_checks_aws_s3_function end ------------------------')
    return False
  # Ensuring the file has a name
  if image.filename == "":
    localhost_print_function('No filename')
    print(' ------------------------ user_upload_image_checks_aws_s3_function end ------------------------')
    return False
  # Ensuring the file type is allowed
  if allowed_images_function(image.filename, allowed_image_extensions_arr):
    # werkzeug.secure_filename not working when uploading to AWS
    # filename = secure_filename(image.filename)
    # Put the image object in aws s3
    aws_upload = upload_image_aws_s3_function(image)
    print(' ------------------------ user_upload_image_checks_aws_s3_function end ------------------------')
    return True
  else:
    localhost_print_function('That file extension is not allowed')
    print(' ------------------------ user_upload_image_checks_aws_s3_function end ------------------------')
    return False
# ------------------------ individual function end ------------------------
print(' ------------------------ __init__ aws_s3 end ------------------------')