# -*- coding:utf-8 -*-
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define,options


define("port",default=8083,help="run server port",type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info("**Request to MainHandler")
	self.write("hello logging....")

settings = {"debug":True,}

application = tornado.web.Application([
    (r"/",MainHandler),
],)

if __name__ == "__main__":
    print 'mmmmmmmmmmmmmmmmmmmmmmm'
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
