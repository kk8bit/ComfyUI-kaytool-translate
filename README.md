# ComfyUI-kaytool-translate

[KayTool](https://github.com/kk8bit/kaytool) 的三个翻译节点，自 KayTool 0.71.1 起移出核心包，在这里单独维护。
The three translation nodes from [KayTool](https://github.com/kk8bit/kaytool), moved out of the core package as of KayTool 0.71.1.

- `𝙆 AIO Translater` — 自动识别源语言，翻译到目标语言（腾讯翻译）
- `𝙆 Tencent Translater` — 指定源/目标语言（腾讯翻译）
- `𝙆 Baidu Translater` — 百度翻译 API，需要自备 App ID / App Key（[申请地址](https://fanyi-api.baidu.com/)）

节点标识与旧版 KayTool 完全相同，装上本包后，原来含这些节点的工作流无需任何修改即可继续使用。
Node identifiers are unchanged, so existing workflows that use them work again as soon as this package is installed.

## 为什么拆出来 / Why a separate package

Comfy Registry 的安全扫描会把任何发起网络请求的节点标记为需要人工审核。翻译节点的全部功能就是发请求，无法避免；而 KayTool 其余二十多个节点与网络无关。拆开后核心包可以正常自动发布，翻译节点在这里以 Git 方式安装，不经 Registry。

The Comfy Registry's security scan flags any node that makes network requests for manual review. Translation is nothing but a network request, so the flag is unavoidable; the rest of KayTool never touches the network. Splitting lets the core package publish normally, while these nodes install from Git and skip the Registry.

## 安装 / Install

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/kk8bit/ComfyUI-kaytool-translate.git
pip install -r ComfyUI-kaytool-translate/requirements.txt
```

重启 ComfyUI。也可以在 ComfyUI-Manager 中通过 Git URL 安装。
Restart ComfyUI. Installing via Git URL in ComfyUI-Manager also works.

## 注意 / Notes

- 腾讯翻译走的是 `transmart.qq.com` 的网页接口，并非官方开放 API，随时可能失效。
  The Tencent nodes use the `transmart.qq.com` web endpoint, not an official API; it may stop working without notice.
- 所有请求均设有超时（连接 10 秒、读取 30 秒），不会卡住工作流。
  All requests time out (10s connect, 30s read) and cannot stall a workflow.
- 需要更多翻译服务可参考 [ComfyUI_Custom_Nodes_AlekPet](https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet)。
  For more translation providers see [ComfyUI_Custom_Nodes_AlekPet](https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet).

## License

GPL-3.0, same as KayTool.
