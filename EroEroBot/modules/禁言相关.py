from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group, Member
from graia.ariadne.util import ariadne_api
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def airc(app: Ariadne, g: Group, msg: MessageChain, mem: Member):
    if 'op' in str(msg):
        try:
            await app.mute_member(g,mem,60)
            await app.send_message(g,MessageChain('本bot反对o神'))
        except:
            await app.send_message(g,MessageChain('我怎么能禁言可爱的群主和管理员（可能我不是管理）'))


