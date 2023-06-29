#views/user_controller.py

import json
from flask import flash, render_template, request, redirect, url_for, session, current_app
from app.services.user_service import UserService

class UserController:
    def __init__(self,app):
        self.app=app
        self.user_service=UserService()
        #路由注册
        self.app.add_url_rule('/',view_func=self.index)
        
        self.app.add_url_rule('/login',view_func=self.login,methods=['GET','POST'])
        self.app.add_url_rule('/logout',view_func=self.logout,methods=['GET','POST'])
        
    def index(self):
        if 'user' in session:
            user=json.loads(session['user'])
            current_app.logger.debug("user={}".format(user))
            return render_template('index.html',user=user)
        return render_template('login.html')
    
    def login(self):
        if request.method=='POST':
            username=request.form['username']
            password=request.form['password']
            # current_app.logger.debug("username={}".format(username))
            # current_app.logger.debug("password={}".format(password))
            user=self.user_service.login(username,password)
            current_app.logger.debug("password={}".format(json.dumps(user.to_json()))) 
            if user:
                session['user']=json.dumps(user.to_json())
                return redirect(url_for('index'))
            else:
                #用户登录失败，显示错误信息
                error='Invalid username or password'
                current_app.logger.debug("error={}".format(error))
                flash(error)
                return render_template('login.html',error=error)
            
        return render_template('login.html')
    
    def logout(self):
        if request.method=='POST':
            self.user_service.logout()
            return redirect(url_for('index'))
        return render_template('login.html')

    def register(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            result=self.user_service.register(username=username, password=password)
            if result:
                # 注册成功，重定向到登录页面
                flash('注册成功，请登录')
                return redirect(url_for('login'))  # 假设登录路由为 'login'
            else:
                # 注册失败，显示错误提示
                flash('注册失败，请重试')
        return render_template('register.html')  # 假设注册页面为 'register.html'

