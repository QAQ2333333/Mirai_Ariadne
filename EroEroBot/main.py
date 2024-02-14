import pkgutil

from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    HttpClientConfig,
    WebsocketClientConfig,
    config,
)
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.saya import Saya

saya = create(Saya)
app = Ariadne(
    connection=config(
        3697368870,
        "GraiaXVerifyKey",
        HttpClientConfig(host="http://localhost:8082"),
        WebsocketClientConfig(host="http://localhost:8082"),
    ),
)

with saya.module_context():
    saya.require("modules.关键字回复（文字）")
    # saya.require("modules.戳一戳")
    saya.require("modules.帮助文档")
    saya.require("modules.关键字回复（图片，音频）")
    saya.require("modules.抽奖系统")
    saya.require("modules.撤回相关")
    #saya.require("modules.计划")
    saya.require("modules.禁言相关")
    saya.require("modules.娱乐系统")
    saya.require("modules.涩图模块")
    saya.require("modules.便民功能")
    saya.require("modules.大模型")

app.launch_blocking()
