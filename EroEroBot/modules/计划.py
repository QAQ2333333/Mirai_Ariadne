from creart import create
from graia.scheduler import timers
from graia.scheduler.saya import SchedulerSchema
from graia.ariadne.message import Source
from graia.ariadne.message.parser.base import Mention, MatchTemplate, ContainKeyword
from graiax import silkcoder
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At, Voice, Image
from graia.ariadne.model import Friend, Group, Member
from graia.saya import Channel, Saya
from graia.saya.builtins.broadcast import ListenerSchema
from graia.ariadne.message.element import At, Plain, Image, Forward, ForwardNode
from graia.scheduler import GraiaScheduler

channel = Channel.current()
saya = create(Saya)


@channel.use(ListenerSchema(listening_events=[GroupMessage], decorators=[ContainKeyword(keyword="龙王")]))
@channel.use(SchedulerSchema(timers.every_minute()))
async def every_minute_speaking(app: Ariadne, group: Group):
    await app.send_message(group, MessageChain("我又来了"))
