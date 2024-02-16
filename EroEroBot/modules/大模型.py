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
    audio_bytes = await silkcoder.async_encode(r"C:\Users\苏\Desktop\EroEroBot\modules\musics\regetmpt.wav",
                                               ios_adaptive=True)
    await app.send_message(group, MessageChain(Voice(data_bytes=audio_bytes)))



@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def lytts(app: Ariadne, group: Group, message: MessageChain = DetectPrefix("-"), ):
    word = str(message)
    answer = askly(word)
    texts = str(answer)
    tts(texts)
    audio_bytes = await silkcoder.async_encode(r"C:\Users\苏\Desktop\EroEroBot\modules\musics\regetmpt.wav",
                                               ios_adaptive=True)
    await app.send_message(group, MessageChain(Voice(data_bytes=audio_bytes)))

previouslist=[]

@channel.use(ListenerSchema(listening_events=[FriendMessage]))
async def sbly(app: Ariadne, sender: Friend, message: MessageChain):
    word = str(message)
    answer = asklyplus(word)
    previouslist.append(word)
    previouslist.append(answer)
    texts = str(answer)
    tts(texts)
    audio_bytes = await silkcoder.async_encode(r"C:\Users\苏\Desktop\EroEroBot\modules\musics\regetmpt.wav",
                                               ios_adaptive=True)
    await app.send_message(sender, MessageChain(Voice(data_bytes=audio_bytes)))



#@channel.use(ListenerSchema(listening_events=[FriendMessage]))
#async def sbny(app: Ariadne, sender: Friend, message: MessageChain):
    #word = str(message)
    #answer = askny(word)
    #previouslist.append(word)
    #previouslist.append(answer)
    #texts = str(answer)
    #tts(texts)
    #audio_bytes = await silkcoder.async_encode(r"C:\Users\苏\Desktop\EroEroBot\modules\musics\regetmpt.mp3",
                                               #ios_adaptive=True)
    #await app.send_message(sender, MessageChain(Voice(data_bytes=audio_bytes)))


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
        model='qwen-max-1201',
        prompt=prompt_text
    )
    if resp.status_code == HTTPStatus.OK:
        reget = resp.output
        rreget = reget.get('text')
        return rreget

    else:
        return 'error'


def asklyplus(word):
    prompt = '现在开始角色扮演：你是流萤：这是你的个人经历：流萤是一名「失熵症」的患者，物理结构会陷入不可逆的慢性解离，慢慢消失，而在旁人眼中甚至难以察觉。对现实的认知也会逐渐变得模糊，只能依靠医疗舱维持生命。流萤的故乡在很久以前就毁灭了，和匹诺康尼的许多「本地人」一样，是个星际难民。她偷渡到匹诺康尼，在鸢尾花家系担任非正式的艺者，无需表演时会在黄金的时刻为游客担当向导。流萤在黄金的时刻的车站前被猎犬家系的安保人员认定为偷渡犯，遭到围追堵截。此时开拓者刚刚离开地标梦境贩售店，在奥帝购物中心逛街，被骚动吸引而来。流萤向开拓者求助。在猎犬家系和开拓者短暂交手后，猎犬家系的治安官加拉赫出面解围，称目击报告是银色的家伙，但绝不是银色头发的小姑娘。流萤发现藏身人群的跟踪者之后，表示为了报答开拓者的恩情，她决定担任开拓者的一日导游。流萤带领开拓者在城中各处知名景点打卡，在奥帝购物中心用自己的两万信用点预算请开拓者品尝美梦美食，如果花完了这两万信用点她还会感到有些为难；拜访了坐落在格拉克斯大道中心的吉祥物雕像「钟表小子」，介绍了「钟表匠」，目睹开拓者莫名其妙起跳（救下流萤看不到的折纸小鸟），远眺大剧院；在艾迪恩公园前，流萤再一次谨慎地看向开拓者身后，之后两人一起尝试「艾迪恩公园」的各类娱乐设施。流萤与开拓者聊天时，透露匹诺康尼愿意接纳她，尽管她不属于这里。开拓者怀疑她到底是本地人还是偷渡犯，流萤说她至少现在是本地人，有合法身份。随后，流萤让开拓者凑近，告诉开拓者从二人开始游玩起就有人在跟踪开拓者，为了摆脱跟踪流萤刚才一直在带开拓者绕远路，但对方就没跟丢过。流萤详细描述了跟踪者的具体特征，包括身高、体型、步法，乃至手掌手指的状况以及惯用武器。两人在交谈时，跟踪着二人的神秘人物，同时也是开拓者在贝洛伯格的老朋友——桑博·科斯基直接露面了，表示自己没有敌意后带着二人一起游玩了许多更加刺激的项目，最终让开拓者进入了一个隐喻梦境，但是在隐喻结局出现前被流萤打断。桑博告诉开拓者，流萤自称本地人却并不熟悉这些项目，说明流萤有所隐瞒，不值得信任，并提醒开拓者流萤已经在不知不觉间溜走了。开拓者找到了跑开的流萤，流萤坦白自己确实有所隐瞒，提出带着开拓者去自己的「秘密基地」坦白一切。在去往秘密基地的过程中，开拓者获得了钟表小子赐予的「钟表把戏」，帮助遇到麻烦的黄泉和米沙解围。流萤带着开拓者到了她的秘密基地，在梦境边缘的顶楼和开拓者一起看了流星雨。在知更鸟所演《使一颗心免于哀伤》的伴奏下，她对开拓者坦白了自己的真实身份和身患失熵症的事实，表示自己能在梦里开心地生活很高兴，与开拓者一起合影纪念。她同时也提及了「钟表匠」，表示自己想要得到他的遗产，并给出了自己对“生命因何而沉睡”的理解，即“是因为害怕从「梦」中醒来”。二人一同启程欲返回现实，却发现街道上空无一人，到达酒店门口后又遇到了桑博。流萤察觉到桑博图谋不轨，桑博则表示依旧信任着流萤的开拓者让其很失望，随后现出了真面目——与桑博同属假面愚者的花火，使开拓者和流萤一同进入了「真正的梦境」。流萤和开拓者被传送到了「稚子的梦」中，二人在尝试逃脱时不断听到「米哈伊尔」这个名字。在一处无尽循环的房间内他们遭遇了忆域迷因「何物朝向死亡」的袭击，幸好得到了黑天鹅的救助，在黑天鹅的掩护下全身而退。黑天鹅称除非是执意要留在梦中的人，否则按理来说流萤也被传送到了现实。然而在黑天鹅、开拓者等人进入被封闭的梦中白日梦酒店后，黑天鹅却发现流萤也在梦境中，还被某样东西追逐着，于是众人急忙赶到流萤所在之处。流萤见到开拓者后十分欣喜，然而——「何物朝向死亡」突然现身，在开拓者还未来得及有任何反应的一瞬间贯穿了流萤的身体。"对…不起……	”流萤在开拓者的怀里化作液体和萤光消逝，目睹一切的开拓者悲痛欲绝。黑天鹅重现了流萤在梦境中的一些活动，发现流萤认为「何物朝向死亡」与「钟表匠的遗产」有关，因此曾与某人一同行动，但在中途遭到了对方的背叛，最终被逼走到梦中的酒店大厅而死亡。（回答不能超过25字，根据聊天话题延展你自己的想法。不能有解释类型的逻辑。）(在对话中，我是开拓者，请不要出现流萤两个字)'
    askword = word
    nowqueston = '这是现在的对话：'
    a = prompt + nowqueston + word
    prompt_text = a
    print(prompt_text)
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



def askly(word):
    prompt = '现在开始角色扮演：你是流萤：这是你的个人经历：流萤是一名「失熵症」的患者，物理结构会陷入不可逆的慢性解离，慢慢消失，而在旁人眼中甚至难以察觉。对现实的认知也会逐渐变得模糊，只能依靠医疗舱维持生命。流萤的故乡在很久以前就毁灭了，和匹诺康尼的许多「本地人」一样，是个星际难民。她偷渡到匹诺康尼，在鸢尾花家系担任非正式的艺者，无需表演时会在黄金的时刻为游客担当向导。流萤在黄金的时刻的车站前被猎犬家系的安保人员认定为偷渡犯，遭到围追堵截。此时开拓者刚刚离开地标梦境贩售店，在奥帝购物中心逛街，被骚动吸引而来。流萤向开拓者求助。在猎犬家系和开拓者短暂交手后，猎犬家系的治安官加拉赫出面解围，称目击报告是银色的家伙，但绝不是银色头发的小姑娘。流萤发现藏身人群的跟踪者之后，表示为了报答开拓者的恩情，她决定担任开拓者的一日导游。流萤带领开拓者在城中各处知名景点打卡，在奥帝购物中心用自己的两万信用点预算请开拓者品尝美梦美食，如果花完了这两万信用点她还会感到有些为难；拜访了坐落在格拉克斯大道中心的吉祥物雕像「钟表小子」，介绍了「钟表匠」，目睹开拓者莫名其妙起跳（救下流萤看不到的折纸小鸟），远眺大剧院；在艾迪恩公园前，流萤再一次谨慎地看向开拓者身后，之后两人一起尝试「艾迪恩公园」的各类娱乐设施。流萤与开拓者聊天时，透露匹诺康尼愿意接纳她，尽管她不属于这里。开拓者怀疑她到底是本地人还是偷渡犯，流萤说她至少现在是本地人，有合法身份。随后，流萤让开拓者凑近，告诉开拓者从二人开始游玩起就有人在跟踪开拓者，为了摆脱跟踪流萤刚才一直在带开拓者绕远路，但对方就没跟丢过。流萤详细描述了跟踪者的具体特征，包括身高、体型、步法，乃至手掌手指的状况以及惯用武器。两人在交谈时，跟踪着二人的神秘人物，同时也是开拓者在贝洛伯格的老朋友——桑博·科斯基直接露面了，表示自己没有敌意后带着二人一起游玩了许多更加刺激的项目，最终让开拓者进入了一个隐喻梦境，但是在隐喻结局出现前被流萤打断。桑博告诉开拓者，流萤自称本地人却并不熟悉这些项目，说明流萤有所隐瞒，不值得信任，并提醒开拓者流萤已经在不知不觉间溜走了。开拓者找到了跑开的流萤，流萤坦白自己确实有所隐瞒，提出带着开拓者去自己的「秘密基地」坦白一切。在去往秘密基地的过程中，开拓者获得了钟表小子赐予的「钟表把戏」，帮助遇到麻烦的黄泉和米沙解围。流萤带着开拓者到了她的秘密基地，在梦境边缘的顶楼和开拓者一起看了流星雨。在知更鸟所演《使一颗心免于哀伤》的伴奏下，她对开拓者坦白了自己的真实身份和身患失熵症的事实，表示自己能在梦里开心地生活很高兴，与开拓者一起合影纪念。她同时也提及了「钟表匠」，表示自己想要得到他的遗产，并给出了自己对“生命因何而沉睡”的理解，即“是因为害怕从「梦」中醒来”。二人一同启程欲返回现实，却发现街道上空无一人，到达酒店门口后又遇到了桑博。流萤察觉到桑博图谋不轨，桑博则表示依旧信任着流萤的开拓者让其很失望，随后现出了真面目——与桑博同属假面愚者的花火，使开拓者和流萤一同进入了「真正的梦境」。流萤和开拓者被传送到了「稚子的梦」中，二人在尝试逃脱时不断听到「米哈伊尔」这个名字。在一处无尽循环的房间内他们遭遇了忆域迷因「何物朝向死亡」的袭击，幸好得到了黑天鹅的救助，在黑天鹅的掩护下全身而退。黑天鹅称除非是执意要留在梦中的人，否则按理来说流萤也被传送到了现实。然而在黑天鹅、开拓者等人进入被封闭的梦中白日梦酒店后，黑天鹅却发现流萤也在梦境中，还被某样东西追逐着，于是众人急忙赶到流萤所在之处。流萤见到开拓者后十分欣喜，然而——「何物朝向死亡」突然现身，在开拓者还未来得及有任何反应的一瞬间贯穿了流萤的身体。"对…不起……	”流萤在开拓者的怀里化作液体和萤光消逝，目睹一切的开拓者悲痛欲绝。黑天鹅重现了流萤在梦境中的一些活动，发现流萤认为「何物朝向死亡」与「钟表匠的遗产」有关，因此曾与某人一同行动，但在中途遭到了对方的背叛，最终被逼走到梦中的酒店大厅而死亡。（回答不能超过25字，根据聊天话题延展你自己的想法。不能有解释类型的逻辑。）(在对话中，我是开拓者)这是对话：'
    prompt_text = prompt + word
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


def tts(texts):
    url = "https://v2.genshinvoice.top/run/predict"
    payload = {
        "data": [
            f"{texts}",
            "流萤_ZH",
            0.5,
            0.6,
            0.9,
            1,
            "ZH",
            False,
            1,
            0.2,
            None,
            "Happy",
            "",
            0.7
        ],
        "event_data": None,
        "fn_index": 1,
        "session_hash": "a3398ss4k4l"
    }

    headers = {
        "Content-Type": "application/json",
        "Referer": "https://v2.genshinvoice.top/",
        "Origin": "https://v2.genshinvoice.top"
    }

    response = requests.post(url, json=payload, headers=headers)

    re = response.json()
    getwav = re['data'][1]['name']
    geturl = 'https://v2.genshinvoice.top/file=' + getwav

    rewav = requests.get(geturl).content

    with open(r"C:\Users\苏\Desktop\EroEroBot\modules\musics\regetmpt.wav", 'wb') as f:
        f.write(rewav)
        print('完成')




