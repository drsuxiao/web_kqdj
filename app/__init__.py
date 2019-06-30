from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
# 导入指定的配置对象
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, api