#-*-coding:utf-8-*-
"""
"""

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print self.request
	#raise tornado.web.HTTPError(400)
	#self.redirect('/some',permanent=False)
        if not self.get_cookie("mycookie"):
	    self.set_cookie("mycookie","myvalue")
	    self.write("your cookie was not set")
	else:
            self.write("You cookie was set:%s" % self.get_cookie("mycookie"))		
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
    def post(self):
        self.set_header("Content-Tpye","text/plain")
	self.write("You wrote" + self.get_argument("message"))
    def some(self):
        self.write("hello...")

class Some(tornado.web.RequestHandler):
    def get(self):
        items = ["item1","item2","item3"]
	self.render("template.html",title="My title",items=items)
        self.write("some...")

class StoryHandler(tornado.web.RequestHandler):
    def get(self,story_id):
        self.write("you requested the story"+story_id)
application = tornado.web.Application([
    (r'/',MainHandler),
    (r'/some',Some), 
    (r'/story/([0-9]+)',StoryHandler),
    ],
    cookie_secret = "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")


if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
