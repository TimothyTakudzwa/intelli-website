import os 

basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY DATABASE CONFIGURATIONS
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'intelli.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SECRET_KEY="powerful secretkey"
WTF_CSRF_SECRET_KEY="a csrf secret key"


# # EMAIL SETTINGS
# MAIL_SERVER='smtp.gmail.com'
# MAIL_PORT=465
# MAIL_USE_SSL=True
# MAIL_USERNAME='pambenidevelopers@gmail.com'
# MAIL_PASSWORD='P@mb3n12018'