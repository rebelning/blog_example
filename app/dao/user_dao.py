#dao/user_dao.py 

# from app.app import db
from app.database.database import db
from app.models.user import User

class UserDao: 
    
    def get_user_by_username(self,username):
        #查询数据库获取用户信息
        return User.query.filter_by(username=username).first()


    def add_user(self,user):
        db.session.add(user)
        db.session.commit()
        