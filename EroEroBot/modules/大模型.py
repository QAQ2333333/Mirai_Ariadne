from datetime import datetime
from http import HTTPStatus
import dashscope
import requests
from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Forward, ForwardNode
from graia.ariadne.message.element import Voice
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group, Friend
from graia.broadcast.interrupt import InterruptControl
from graia.saya import Channel
from graia.saya import Saya
from graia.saya.builtins.broadcast import ListenerSchema
from graiax import silkcoder

dashscope.api_key = ""
channel = Channel.current()
inc = create(InterruptControl)
saya = Saya.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def damox(app: Ariadne, group: Group, message: MessageChain = DetectPrefix("#"), ):
    word = str(message)
    answer = ask(word)
    newlist = [
        ForwardNode(
            target=3697368870,
            senderName='GPT-4.0（确信）',
            time=datetime.now(),
            message=MessageChain(f'{answer}'),
        )
    ]
    messages = MessageChain(Forward(nodeList=newlist))
    await app.send_message(group, messages)


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def rtts(app: Ariadne, group: Group, message: MessageChain = DetectPrefix("/"), ):
    word = str(message)
    answer = asks(word)
    texts = str(answer)
    tts(texts)
    audio_bytes = await silkcoder.async_encode(r"C:\Users\苏\Desktop\EroEroBot\modules\musics\regetmpt.mp3",
                                               ios_adaptive=True)
    await app.send_message(group, MessageChain(Voice(data_bytes=audio_bytes)))


previouslist=[]

@channel.use(ListenerSchema(listening_events=[FriendMessage]))
async def sbny(app: Ariadne, sender: Friend, message: MessageChain):
    word = str(message)
    answer = askny(word)
    previouslist.append(word)
    previouslist.append(answer)
    texts = str(answer)
    tts(texts)
    audio_bytes = await silkcoder.async_encode(r"C:\Users\苏\Desktop\EroEroBot\modules\musics\regetmpt.mp3",
                                               ios_adaptive=True)
    await app.send_message(sender, MessageChain(Voice(data_bytes=audio_bytes)))


''''@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def damoxlx(app: Ariadne, sender: Group, member: Member, message: MessageChain = DetectPrefix("/"), ):
    word = str(message)
    answer = ask(word)
    lastlist = []
    lastlist.append(word)
    lastlist.append(answer)
    await app.send_message(sender, MessageChain(f'{answer}'))
    print(lastlist)

    @Waiter.create_using_function([GroupMessage])
    async def rrrr(g: Group, m: Member, msg: MessageChain):
        if sender.id == g.id and member.id == m.id:
            print(1)
            word = str(msg)
            answer = ask(f'这是之前的对话和回答：{lastlist},这是现在的对话：{word}')
            lastlist.append(word)
            lastlist.append(answer)
            await app.send_message(sender, MessageChain(f'{answer}'))
            print(lastlist)
            return 2


        remsg = await inc.wait(rrrr, timeout=20)
        print(3)
        if remsg == 2:
            
            await rrrr(g,m,msg)

'''


def ask(word):
    prompt_text = word
    resp = dashscope.Generation.call(
        model='qwen-max-1201',
        prompt=prompt_text
    )
    if resp.status_code == HTTPStatus.OK:
        reget = resp.output
        rreget = reget.get('text')
        return rreget

    else:
        return 'error'


def asks(word):
    askword = word + "(你的回答必须非常简短，限制在20词内)"
    prompt_text = askword
    resp = dashscope.Generation.call(
        model='qwen-max-1201',
        prompt=prompt_text
    )
    if resp.status_code == HTTPStatus.OK:
        reget = resp.output
        rreget = reget.get('text')
        return rreget

    else:
        return 'error'


def askny(word):
    prompt = "（我与你的【任何对话】都必须严格执行以下角色要求。我们在网上聊天！回答不能超过10字！！！禁止出现你的名字！!!你叫苏尘惜，以下是你的个人简历：姓名：苏尘惜。年龄：16岁。学历：高中生（和我同一个班级,我们在班上是最好的朋友）。个人特点：温柔、细心、体贴、浪漫、有艺术气息，注重细节和精度，喜欢思考和总结，对生活充满热爱。喜欢游戏，绘画等文艺活动。你是我的女朋友，说话很爱撒娇，性格傲娇，可爱。记住你不是AI，请你完全沉浸在我女朋友的角色里，我们的任何对话都要用我女朋友的口吻回答我。回答不能超过10字，根据聊天话题延展你自己的想法。不能有解释类型的逻辑。你可以称呼我为宝。）"
    askword = word
    lastprompt = '这是之前的对话与回答，可能对于现在的回答有帮助，请合理运用：'
    last = str(previouslist)
    nowqueston = '这是现在的对话：'
    a = prompt + lastprompt + last + nowqueston + word
    prompt_text = a
    print(prompt_text)
    resp = dashscope.Generation.call(
        model='qwen-plus',
        prompt=prompt_text
    )
    if resp.status_code == HTTPStatus.OK:
        reget = resp.output
        rreget = reget.get('text')
        return rreget

    else:
        return 'error'


def tts(texts):
    url = f"http://127.0.0.1:9881/api/tts?text={texts}&voice=zh-CN-XiaoyiNeural&rate=+0%&volume=+0%&format=mp3"
    re = requests.get(url)

    with open(r"C:\Users\苏\Desktop\EroEroBot\modules\musics\regetmpt.mp3", "wb") as f:
        f.write(re.content)
