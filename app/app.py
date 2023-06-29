#app.py
# export FLASK_APP=app/app.py

from flask import Flask,session,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import logging

from app.views.user_controller import UserController
from app.database.database import db



app = Flask(__name__)

# 配置日志记录
app.logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
app.logger.addHandler(stream_handler)

app.debug=True
app.config['SECRET_KEY'] = '1234567890.'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost:3306/myblog'



# db = SQLAlchemy(app)
db.init_app(app)

user_controller=UserController(app)

if __name__=='__main__':
    app.run()