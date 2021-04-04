# coding: utf-8


from tornado import web, ioloop, httpserver
import os


# 登录事件处理
class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # 渲染登录页面
        self.render('login.html')

    def post(self):
        # 登录各种情况处理
        account = self.get_argument('account')
        password = self.get_argument('password')
        if account not in massage:
            self.write('账户名不存在，请重新输入')
            # 渲染登录页面
            self.render('login.html')
        elif massage[account] != password:
            self.write('密码输入错误，请重新输入')
            # 渲染登录页面
            self.render('login.html')
        else:
            # 登录成功跳转至创建会议页面
            self.redirect('/create')


# 注册事件处理
class RigesterHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # 渲染注册页面
        self.render('register.html')

    def post(self):
        # 设置账户名和密码
        new_account = self.get_argument('account')
        new_password = self.get_argument('password')
        new_repassword = self.get_argument('repassword')

        # 处理注册信息
        if new_password != new_repassword:
            self.write('密码与再次输入的密码不同，请重试')
            self.render('register.html')
        elif new_account in massage:
            self.write('账户名已被注册，请重试')
            self.render('register.html')
        else:
            massage[new_account] = new_password
            # 回到登录页面
            self.redirect('/login')


# 处理登录事件
class CreateHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('create.html')


# 处理会议事件
class ConferenceHandler(web.RequestHandler):
    def get(self):
        confer_id = self.get_argument('conference_id')
        self.render('conference.html', number=confer_id)


# 设置字典记录account和password
massage = {}

# 设置路由
app = web.Application(
    [(r"/login", LoginHandler), (r'/register', RigesterHandler),
     (r'/create', CreateHandler), (r'/conference', ConferenceHandler)],
    template_path=os.path.join(os.path.dirname(__file__), "template")
    )

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(app)  # http接受请求并传给路由
    http_server.listen(8888)                  # 监听端口
    ioloop.IOLoop.current().start()
