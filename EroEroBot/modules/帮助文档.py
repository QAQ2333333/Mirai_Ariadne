from pydoc import plain
import random
from datetime import datetime
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.element import Forward, ForwardNode
from graia.ariadne.message.parser.base import ContainKeyword
from graia.ariadne.model import Group, Member
from graia.saya import channel, Channel
from graia.saya.builtins.broadcast import ListenerSchema
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.model import Friend, Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()



@channel.use(ListenerSchema(listening_events=[GroupMessage, FriendMessage],decorators=[ContainKeyword(keyword="help")]))        #监听群好友消息from graia.ariadne.event.message import GroupMessage, FriendMessage
async def hello(app: Ariadne, sender: Group | Friend, message: MessageChain):       #函数定义app: Ariadne,对象：Group | Friend,（message: MessageChain）看不懂

    helplist = [
        ForwardNode(
            target=2198694220,
            senderName='呜呜呜我的流萤',
            time=datetime.now(),
            message=MessageChain('你终于找到我了，等你好久了'),
        )
    ]

    helplist.append(
        ForwardNode(
            target=3697368870,
            senderName='我爱的流萤',
            time=datetime.now(),
            message=MessageChain("本bot的功能：\n1.奇奇怪怪的图片生成（pet查看帮助）\n2.重点！！！涩图功能：指令：\n假涩图：来一份涩图 \n真涩图：来一份16+涩图（真的有点涩）\n3.抽奖系统，关键字：卷，看看都是谁在内卷 \n4.娱乐系统（没开发完），这是删档测试：输入开始冒险即可开始娱乐系统，输入商店购买禁言卡（真的可以禁言别人，要bot有管理）（（试试114514））\n5.关键字回复（这个你们就自己探索吧....\n6.关键字禁言，撤回（这个还是不要探索比较好 \n7.便民功能（原来我是好人）指令：发公告\n指令：@全体成员\n8.调用大模型，对话开头加上# 或者开头加上/，我会用语音回答你哦"),
        )
    )

    message = MessageChain(Forward(nodeList=helplist))
    await app.send_message(sender, message)
















