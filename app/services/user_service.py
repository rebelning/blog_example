#service/user_service.py

from flask import session
from app.dao.user_dao import UserDao
from app.models.user import User
# 

class UserService:
    def __init__(self):
        self.user_dao=UserDao()
        
    def login(self,username,password):
        user=self.user_dao.get_user_by_username(username)
        if user and user.password==password:
            return user
        else:
            return None   
    def logout(self):
        session.pop('user',None)
    
    def register(self,username,password): 
        user=self.user_dao.get_user_by_username(username)
        if user:
            return None 
        new_user=User(username=username,password=password)
        self.user_dao.add_user(new_user)
    
        return new_user
    
