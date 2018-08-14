# coding:utf-8
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import hashlib
from tornado.web import RequestHandler
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from tornado.options import options, define


define("port", default=80, type=int, help="")

conf = WechatConf(
    token='weixintoken',
    appid='wx1ed711720d6937a9',
    appsecret='Angel84562',
    encrypt_mode='normal',
    encoding_aes_key='z1TVUN3oA5MMEWd2h49aQAwBQEwimrPMTl1oKwcAaxf'
)
wechat = WechatBasic(conf=conf)

class WeChatHandler(RequestHandler):
    def get(self):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')
        echostr = self.get_argument('echostr')
        if wechat.check_signature(signature, timestamp, nonce):
            self.write(echostr)
        else:
            self.write('Not Open')


def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r"/wechat80", WeChatHandler),
        ], debug = True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
