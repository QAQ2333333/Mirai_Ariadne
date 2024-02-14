from graia.ariadne.message import Source
from graia.ariadne.message.parser.base import Mention, MatchTemplate, ContainKeyword
from graiax import silkcoder
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At, Voice, Image
from graia.ariadne.model import Friend, Group, Member
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
from graia.ariadne.message.element import At, Plain, Image, Forward, ForwardNode

channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage],decorators=[ContainKeyword(keyword="流萤")]))
async def test(app: Ariadne, source: Source,sender:Group,member: Member):
    try:
        await app.recall_message(source)
        await app.send_message(sender, MessageChain(At(target=member),'我梦见一片焦土，一株破土而生的新蕊，它迎着朝阳绽放，向我低语，呢喃\n流萤已经死了，阳光穿过秋天的枫叶，留下一张张独特的风景，如此灿烂，如此艳丽'))
    except:
        await app.send_message(sender,MessageChain('我怎么能撤可爱的群主和管理员（可能我不是管理）'))




