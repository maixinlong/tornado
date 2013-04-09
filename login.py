#-*-coding:utf-8 -*-
import tornado.ioloop
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        print self.request
        if not self.current_user:
	    self.redirect("/login")
	    return
	name = tornado.escape.xhtml_escape(self.current_user)
	self.write("hello" + name)
class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
	    'Name: <input type="text" name="name">'
	    '<input type="submit" value="Sign in">'
	    '</form></body></html>')
    def post(self):
        if not self.request.headers.get("Cookies"):
	    print 'cookies is not'
	    self.render("template.html",title="test",items={})
        self.set_secure_cookie("user",self.get_argument("name"),30)
	self.redirect("/")
settings = {
	    "cookie_secret": "maixinlong",
	        "login_url": "/login",
}
application = tornado.web.Application([
    (r"/",MainHandler),
    (r"/login",LoginHandler)
],**settings)



if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
