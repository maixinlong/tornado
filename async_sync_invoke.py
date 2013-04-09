#-*-coding:utf-*-

import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        for i in range(1,100000):
	    print "kill time%d" % i
	self.write("hello")
	self.flush()

settings = {"debug":True,
          }


application = tornado.web.Application([(r'/async-sync-test/',MainHandler),],**settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8084)
    tornado.ioloop.IOLoop.instance().start()
