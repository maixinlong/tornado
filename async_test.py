# -*- coding:utf-8 -*-


import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
	print '----------------'
	logging.info("log...........")
        http = tornado.httpclient.AsyncHTTPClient()
	http.fetch("http://localhost:8084/async-sync-test/",callback=self._test_callback)
        self.write("hello to the Tornado llll")
	self.flush()

    def _test_callback(self,response):
        self.write(response.body)
	self.flush()

settings = {
	"debug":True,
	}

application = tornado.web.Application([
    (r'/',MainHandler),
],**settings)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8083)
    tornado.ioloop.IOLoop.instance().start()


