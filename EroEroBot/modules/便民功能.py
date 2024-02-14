from graia.ariadne.message.element import At, Plain, Image, Forward, ForwardNode, AtAll
import asyncio
import time
from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group, Member
from graia.broadcast.interrupt import InterruptControl
from graia.broadcast.interrupt.waiter import Waiter
from graia.saya import Channel, Saya
from graia.saya.builtins.broadcast import ListenerSchema
import requests

inc = create(InterruptControl)
saya = Saya.current()
channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage],decorators=[MatchContent('发公告')]))
async def gonggao(app:Ariadne, sender: Group,member:Member):
    await app.send_message(sender, MessageChain("你的下一条消息要全部输完公告（不支持图片等）（120秒）"))

    @Waiter.create_using_function([GroupMessage])
    async def regonggao(g: Group, m: Member, msg: MessageChain):
        if sender.id == g.id and member.id == m.id:
            return msg

    try:
        remsg = await inc.wait(regonggao, timeout=120)
        restrmsg = str(remsg)
        await app.publish_announcement(
            sender,
            restrmsg
        )

    except asyncio.TimeoutError:
        await app.send_message(sender, MessageChain(At(tatget=member),"超时退出，或者没管理，或者出现错误了"))



@channel.use(ListenerSchema(listening_events=[GroupMessage],decorators=[MatchContent('@全体成员')]))
async def ata(app:Ariadne, sender: Group,member:Member,msg:MessageChain):
    await app.send_message(sender, MessageChain(AtAll()))
    await app.send_message(sender, MessageChain(At(target=member),f'她@你们的，可能出了什么事。\n原消息：{msg}'))






    































