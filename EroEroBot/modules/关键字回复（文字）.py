from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.message.parser.base import Mention
from graia.ariadne.model import Group, Member
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()



@channel.use(ListenerSchema(listening_events=[GroupMessage], decorators=[Mention(target=3697368870)]))
async def aircc1(app: Ariadne, sendder: Group, member: Member):
    await app.send_message(sendder, MessageChain(At(target=member), '\nMirai在这里哦\n有什么需要帮助的吗，发送help查看帮助'))


@channel.use(ListenerSchema(listening_events=[GroupMessage], decorators=[Mention(target=2198694220)]))
async def aircc2(app: Ariadne, sendder: Group, member: Member):
    await app.send_message(sendder, MessageChain(At(target=member), ' 找我麻麻干嘛'))


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def setu(app: Ariadne, group: Group, message: MessageChain):
    if str(message) == "原神":
         await app.send_message(
            group,
            MessageChain("启动！"),
         )

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def setu1(app: Ariadne, group: Group, message: MessageChain):
    if str(message) == "6":
         await app.send_message(
            group,
            MessageChain("6"),
         )

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def airc2(app:Ariadne,sendder:Group,message: MessageChain):
    if '原' in str(message):
        await app.send_message(sendder, MessageChain('原？哪里有原神？'))


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def airc3(app:Ariadne,sendder:Group,message: MessageChain):
    if('刻晴' in str(message)):
        await app.send_message(sendder, MessageChain('刻晴！我的刻晴'))