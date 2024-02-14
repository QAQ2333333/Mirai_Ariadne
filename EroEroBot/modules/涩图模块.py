from graia.ariadne.message.element import At, Plain, Image, Forward, ForwardNode
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


@channel.use(ListenerSchema(listening_events=[GroupMessage],decorators=[MatchContent('来一份16+涩图')]))
async def asksetu(app:Ariadne, sender: Group,member:Member):
    await app.send_message(sender, MessageChain(At(target=member),"你想要什么tag的涩图"))

    @Waiter.create_using_function([GroupMessage])
    async def resetu(g: Group, m: Member, msg: MessageChain):
        if sender.id == g.id and member.id == m.id:
            return msg

    try:
        remeg = await inc.wait(resetu,timeout=20)
        try:
            await app.send_message(sender, MessageChain('正在从P站下载涩图\n你说得对，但是在这之后所有人大概都要等30秒后才能调用这函数'))
            getsetu(str(remeg))
            await app.send_message(sender,MessageChain(f'标题：{title}\n标签：{tags}\n发送图片中...'))
            leiqie = await app.send_message(sender,MessageChain(Image(path=r"C:\Users\苏\Desktop\EroEroBot\modules\musics\newget.jpg")))
            time.sleep(10)
            await app.recall_message(leiqie)
        except:
            await app.send_message(sender,MessageChain('出现了错误，但是我懒得写except，你可以过一分钟再试试\n你看看你是不是乱输标签！！！'))

    except asyncio.TimeoutError:
        await app.send_message(sender, MessageChain("超时取消对话，私密马赛"))



def getsetu(remsg):
    url = "https://api.lolicon.app/setu/v2"

    ac = {
        "r18": 0,
        "tag": [remsg],
        "num": 1
    }

    re = requests.get(url, params=ac)
    data = re.json()
    rre = data['data'][0]

    global title,tags
    title = rre['title']
    tags = rre['tags']
    urls = rre['urls']["original"]

    reimage = requests.get(urls)
    image = reimage.content

    with open(r"C:\Users\苏\Desktop\EroEroBot\modules\musics\newget.jpg","wb") as f:
        f.write(image)



@channel.use(ListenerSchema(listening_events=[GroupMessage],decorators=[MatchContent('来一份涩图')]))
async def aircr(app:Ariadne, sender: Group,message:MessageChain,member:Member):
    await app.send_message(sender, MessageChain("你想要什么涩图"))

    @Waiter.create_using_function([GroupMessage])
    async def rep(g: Group, m: Member, msg: MessageChain):
        if sender.id == g.id and member.id == m.id:
            return msg

    try:
        remsg = await inc.wait(rep, timeout=23)
        await app.send_message(sender, MessageChain(f"原来你喜欢{remsg}这种类型的,我懂，我都懂"))
        await app.send_message(sender, MessageChain('这是你的涩图'))
        hhr=await app.send_message(sender, MessageChain(Image(path=r"C:\Users\苏\Desktop\EroEroBot\modules\musics\hh.png")))
        time.sleep(30)
        await app.recall_message(hhr)
        await app.send_message(sender, MessageChain('好涩，还好撤回了'))

    except asyncio.TimeoutError:
        await app.send_message(sender, MessageChain("你说话了吗？"))













