#app/database/database.py
# Desc: 数据库配置文件
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 创建 SQLAlchemy 实例
db = SQLAlchemy()

# 将 SQLAlchemy 实例与 Flask 应用进行关联
# db.init_app(app)
