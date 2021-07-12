SECRET_KEY = "SERECT-KEY-IS-SECRET"

#---------Database------------
DATABASE_NAME = "bookstoredb"
USERNAME = "root"
DATABASE_PASSWORD = "Password123@"
DATABASE_HOST = "localhost"
DATABASE_PORT = "5000"
##dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + USERNAME + ":" + DATABASE_PASSWORD +"@"+DATABASE_HOST +"/"+DATABASE_NAME
SQLALCHEMY_TRACK_MODIFICATIONS = True

#-----------MAIL--------------
MAIL_SERVER = 'smp.googlemail.com'
MAIL_USERNAME = "shinichi24567@gmail.com" ##Tài khoản gmail dùng để gửi email
MAIL_PASSWORD = "**************"  ##Mật khẩu gmail dùng để gửi email

#-----------CLOUDINARY-----------
## Dùng api của Cloudinary để chứa, lưu trữ hình ảnh
## https://cloudinary.com/users/login
## https://cloudinary.com/console/c-fd1e54ad1b53ed47e1420a55c69e75
## Account name: shinichi24567@gmail.com
## Password: **************
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]
CLOUD_NAME = 'dra7ojfcd'
API_KEY = '651393896724639'
API_SECRET = 'x--KfG2S4tUnsUi-VZWOZOi-3Zs'

#-----------PAYPAL-----------
PAYPAL_WEBSITE = 'https://sandbox.paypal.com/developer/accounts/'
PERSIONAL_EMAIL_PAYPAL = 'shinichi24567@gmail.com'
BUSINESS_EMAIL_PAYPAL = 'business-shinichi24567@gmail.com'
BUSINESS_and_PERSONAL_PASSWORD_PAYPAL = 'paypal123'

#-----------GOOGLE_CLOUD-----------
#https://console.cloud.google.com/
## Account name: shinichi24567@gmail.com
## Password: **************
GOOGLE_CLIENT_ID = '258914989074-2rkptjvoc5mv1biv91pg4hhqd1igc9fs.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '1DtIDHTRYgVUQtdiGB_FNdXh'
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
