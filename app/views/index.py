#views/index.py

import json
from flask import render_template, request, redirect, url_for, session, current_app
from flask.views import MethodView

class IndexView(MethodView):
    def get(self):
        user = session['user']
        user_dict=json.loads(user)
        return render_template('index.html',user=user_dict)
    
    def post(self):
        if request.form.get('logout'):  # 如果用户点击了退出按钮
            # 执行退出操作，比如清除 session 数据或其他必要的操作
            current_app.logger.debug("logout")
            session.clear()  # 清除当前用户的 session 数据
            return redirect(url_for('login'))  # 重定向到登录页面
        else:
            return render_template('login.html')