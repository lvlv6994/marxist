from gtts import gTTS
import os

# 要转换为语音的文本
text = "你好,欢迎来到马上风的频道"

# 创建一个 gTTS 对象，并指定语言为英文
tts = gTTS(text=text, lang='zh-cn')

# 将语音保存为音频文件
tts.save("output.mp3")

# 播放语音
os.system("mpv output.mp3")
