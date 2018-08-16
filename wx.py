# -*- coding: utf-8 -*-
import tornado
from wechat_sdk.messages import *
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from auto_reply import TulingAutoReply
from image import img
from image2 import image2
import random
conf = WechatConf(
    token='weixintoken',
    appid='wx1ed711720d6937a9',
    appsecret='Angel84562',
    encrypt_mode='normal',
    encoding_aes_key='z1TVUN3oA5MMEWd2h49aQAwBQEwimrPMTl1oKwcAaxf'
)

wechat = WechatBasic(conf=conf)
auto_reply = TulingAutoReply('691514c677c141d9b779c5f29be17b13', 'http://www.tuling123.com/openapi/api')


class WX(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        signature = self.get_argument('signature', 'default')
        timestamp = self.get_argument('timestamp', 'default')
        nonce = self.get_argument('nonce', 'default')
        echostr = self.get_argument('echostr', 'default')
        if signature != 'default' and timestamp != 'default' and nonce != 'default' and echostr != 'default' \
                and wechat.check_signature(signature, timestamp, nonce):
            self.write(echostr)
        else:
            self.write('Not Open')

    def wx_proc_msg(self, body):
        try:
            wechat.parse_data(body)
        except ParseError:
            print
            'Invalid Body Text'
            return
        # 消息是文本消息
        if isinstance(wechat.message, TextMessage):
            content = wechat.message.content
            if content == "我的专属情话":
                return wechat.response_text(content=self.get_sentence())
            else:
                reply = auto_reply.reply(content)
                if reply is not None:
                    return wechat.response_text(content=reply)
                else:
                    return wechat.response_text(content=u"我不是很懂你在说什么~")
                return wechat.response_text(content=u"知道了")
        # 消息是声音消息
        elif isinstance(wechat.message, VoiceMessage):
            # media_id = wechat.message.media_id  # MediaId
            # format = wechat.message.format  # Format
            recognition = wechat.message.recognition  # 语音识别结果
            reply = auto_reply.reply(recognition)
            if reply is not None:
                return wechat.response_text(content=reply)
            else:
                return wechat.response_text(content=u"我听不懂你在说什么~")
        # 消息是图像消息
        elif isinstance(wechat.message, ImageMessage):
            picurl = wechat.message.picurl  # PicUrld
            print("照片URL是：", picurl)
            # data = img(picurl)
            data = image2(picurl)
            # media_id = wechat.message.media_id  # MediaId
            if picurl is not None:
                return wechat.response_text(content=data['content']['text'])
        # 关注动作
        elif isinstance(wechat.message, EventMessage):
            if wechat.message.type == 'subscribe':  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
                return wechat.response_text(content=u"欢迎关注Lcccc的公众号~")
        else:
            return wechat.response_text(content=u"啦啦啦啦~")

    def get_sentence(self):
        with open('/wx/note.txt', encoding='utf8') as f:
            lines = f.readlines()
            index = random.randint(0, len(lines))
            return lines[index]

    def post(self):
        signature = self.get_argument('signature', 'default')
        timestamp = self.get_argument('timestamp', 'default')
        nonce = self.get_argument('nonce', 'default')
        if signature != 'default' and timestamp != 'default' and nonce != 'default' \
                and wechat.check_signature(signature, timestamp, nonce):
            body = self.request.body.decode('utf-8')
            try:
                result = self.wx_proc_msg(body)
                if result is not None:
                    self.write(result)
            except IOError as e:
                return



