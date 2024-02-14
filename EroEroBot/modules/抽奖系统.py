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

channel = Channel.current()

num=3

@channel.use(ListenerSchema( listening_events=[GroupMessage],decorators=[ContainKeyword(keyword="卷")]))
async def create_forward(app: Ariadne, group: Group, member: Member,message: MessageChain):

    newlist = [
        ForwardNode(
            target=3697368870,
            senderName='可爱的琳妮特',
            time=datetime.now(),
            message=MessageChain('让我看看谁在内卷'),
        )
    ]
    member_list = await app.get_member_list(group)

    for _ in range(num):
        suiji: Member = random.choice(member_list)
        newlist.append(
            ForwardNode(
                target=suiji,
                time=datetime.now(),
                message=MessageChain("我在内卷"),
            )
        )
    message = MessageChain(Forward(nodeList=newlist))
    await app.send_message(group, message)