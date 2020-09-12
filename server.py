import tornado.ioloop ##Simple webserver framework
import tornado.web

class MainHandler(tornado.web.RequestHandler): ##Handler to respond with a simple hello world
    def get(self):
        self.write("Hello, world\n")
        print(self.request) ##Log handler to view them at Stackdriver


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888) ##App listening at port 8888
    tornado.ioloop.IOLoop.current().start() 
