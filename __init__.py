from .nodes.aio_translater import AIOTranslater
from .nodes.tencent_translater import TencentTranslater
from .nodes.baidu_translater import BaiduTranslater

# 节点标识与 KayTool 0.71.0 及更早版本完全一致，旧工作流装上本包即可直接恢复。
NODE_CLASS_MAPPINGS = {
    "AIO_Translater": AIOTranslater,
    "Tencent_Translater": TencentTranslater,
    "Baidu_Translater": BaiduTranslater,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AIO_Translater": "𝙆 AIO Translater",
    "Tencent_Translater": "𝙆 Tencent Translater",
    "Baidu_Translater": "𝙆 Baidu Translater",
}
