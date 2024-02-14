from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.message.parser.base import ContainKeyword, DetectPrefix
from graia.ariadne.model import Group, Member
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
import random
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

class User:
    def __init__(self,uuid):
        self.uid=uuid
        self.point=0

    def add_p (self,points):
        self.point+=points

    def jian_p(self,points):
        self.point-=points

class Usermanager:
    def __init__(self):
        self.users={}

    def creat_u(self,uuid):
        user=User(uuid)
        self.users[uuid] = user
        return user

    def find_u(self,uuid):
        return self.users.get(uuid)

    def get_p(self,uuid):
        user = self.find_u(uuid)
        return user.point

user_m = Usermanager()
inc = create(InterruptControl)
saya = Saya.current()
channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage],decorators=[ContainKeyword(keyword="开始冒险")],))
async def kaihao(app: Ariadne, group: Group,member:Member):
    if user_m.find_u(int(member.id)):
        await app.send_message(group, MessageChain(At(target=member), '你已经有账号了,不要反复重开哦'))
    else:
        user=user_m.creat_u(int(member.id))
        x=random.randint(1,100000)
        user.add_p(x)
        r=user_m.get_p(int(member.id))
        await app.send_message(group,MessageChain(At(target=member),f'这是你的猫粮：{r}'))


@channel.use(ListenerSchema(listening_events=[GroupMessage],decorators=[ContainKeyword(keyword="114514")],))
async def getmaoliang(app: Ariadne, group: Group,member:Member):
    try:
        user=user_m.find_u(int(member.id))
        user.add_p(10000)
        r=user_m.get_p(int(member.id))
        await app.send_message(group,MessageChain(At(target=member),f'好臭恭喜你触发隐藏奖励，现在你的猫粮是：{r}'))
    except:
        await app.send_message(group,MessageChain(At(target=member),'失败了,是不是你没开始冒险？'))



@channel.use(ListenerSchema(listening_events=[GroupMessage],decorators=[DetectPrefix("商店")]))
async def getmaoliang1(app: Ariadne, group: Group,member:Member):
    await app.send_message(group,MessageChain('1.禁言卡！！！：猫粮：50000\n回答y/n'))

    @Waiter.create_using_function([GroupMessage])
    async def reda(g: Group, m: Member, msg: MessageChain):
        if group.id == g.id and member.id == m.id:
            return msg

    try:
        remsg = await inc.wait(reda, timeout=10)
        if str(remsg) == 'y':
            if user_m.get_p(int(member.id)) >=50000:
                await app.send_message(group,MessageChain('请发送要禁言的人QQ号（30秒），群主和管理禁不了，别试了'))

                @Waiter.create_using_function([GroupMessage])
                async def reda2(gr: Group, me: Member, msgc: MessageChain):
                    if group.id == gr.id and member.id == me.id:
                        return msgc

                remsgc = await inc.wait(reda2,timeout=30)
                tar = str(remsgc)
                await app.mute_member(group,tar,60)
                uur=user_m.find_u(int(member.id))
                uur.jian_p(50000)
                r=user_m.get_p(int(member.id))
                await app.send_message(group,MessageChain(f'完成啦，现在你有{r}份猫粮'))


    except:
        await app.send_message(group,MessageChain('出错了,私密马赛'))
















