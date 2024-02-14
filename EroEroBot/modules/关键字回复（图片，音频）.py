from graiax import silkcoder
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At, Voice, Image
from graia.ariadne.model import Friend, Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
from creart import create


channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage, FriendMessage]))        #监听群好友消息from graia.ariadne.event.message import GroupMessage, FriendMessage
async def yuying(app: Ariadne, sender: Group | Friend, message: MessageChain):       #函数定义app: Ariadne,对象：Group | Friend,（message: MessageChain）看不懂
    if '钱' in str(message):
        audio_bytes = await silkcoder.async_encode(r"C:\Users\苏\Desktop\EroEroBot\modules\musics\zl.wav", ios_adaptive=True)
        await app.send_message(sender, MessageChain(Voice(data_bytes=audio_bytes)))



@channel.use(ListenerSchema(listening_events=[GroupMessage, FriendMessage]))
async def tupian(app: Ariadne, sender: Group | Friend, message: MessageChain):
    if '累' in str(message):
        await app.send_message(sender, MessageChain(Image(path=r"C:\Users\苏\Desktop\EroEroBot\modules\musics\hcds.jpg")))