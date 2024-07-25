import torch
from ChatTTS import Chat
from IPython.display import Audio

# 初始化 ChatTTS
chat = Chat()
chat.load_models()

# 定义要转换为语音的文本
texts = ["你好，欢迎使用 ChatTTS！"]

# 生成语音
wavs = chat.infer(texts, use_decoder=True)

# 播放生成的音频
audio = Audio(wavs[0], rate=24000, autoplay=True)
display(audio)
