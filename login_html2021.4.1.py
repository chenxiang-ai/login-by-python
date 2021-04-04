# coding: utf-8

from tornado import web, ioloop, httpserver
import os


# 請求處理
class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):   # 响应操作函数
        self.render('login.html')

    def post(self):                 # 注册后返回登录界面，由该函数处理
        new_account = self.get_argument('account')
        new_password = self.get_argument('password')
        new_repassword = self.get_argument('repassword')
        if new_password != new_repassword:
            self.write('密码与再次输入的密码不同，请重试')  # 密码不一致
            self.render('register.html')
        elif new_account in massage:
            self.write('账户名已被注册，请重试')            # 账户明已被注册
            self.render('register.html')
        else:
            massage[new_account] = new_password
            self.render('login.html')


class SubmitHandler(web.RequestHandler):
    def post(self):
        account = self.get_argument('account')      # 提取login中用户输入的account
        password = self.get_argument('password')    # 提取password中用户输入的password
        if account not in massage:
            self.write('账户名不存在，请重新输入')
            self.render('login.html')
        elif massage[account] != password:
            self.write('密码输入错误，请重新输入')
            self.render('login.html')
        else:
            self.render('poem.html')


class RigesterHandler(web.RequestHandler):
    def post(self):
        self.render('register.html')                # 渲染注册界面


massage = {}
# 设置路由
app = web.Application(
    [(r"/login", LoginHandler), (r'/poem', SubmitHandler), (r'/register', RigesterHandler)],
    template_path=os.path.join(os.path.dirname(__file__), "template")
    )

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(app)  # http接受请求并传给路由
    http_server.listen(8888)                  # 监听端口
    ioloop.IOLoop.current().start()
