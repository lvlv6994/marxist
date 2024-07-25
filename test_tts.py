from gtts import gTTS
from pydub import AudioSegment
import playsound

# 生成语音
text = """
你遇到的错误提示表明模型的初始化存在问题。具体来说，`AssertionError` 表示模型在使用之前没有正确初始化或配置。以下是一些排查步骤：

1. **检查模型初始化**：确保所有模型组件（如 `vocos`、`gpt`、`tokenizer`、`dvae`、`decoder`）在使用之前已正确初始化。警告信息表明这些组件没有被初始化。

2. **验证依赖项**：确认所有必要的库和依赖项都已正确安装并且是最新的。有时缺少或过时的包会导致初始化问题。

3. **检查代码**：查看 `chattts_test.py` 脚本和 `core.py` 文件中的 `ChatTTS` 类实现，确保所有必要的参数和配置都已正确设置。

4. **模型路径**：验证模型文件或检查点的路径是否正确，并确保这些文件可以访问。

5. **CPU 与 GPU**：由于脚本使用了 CPU，确保 CPU 配置与模型兼容。如果需要 GPU 支持，确保 CUDA 和相关 GPU 驱动程序已正确安装。

6. **查看文档**：查阅 `ChatTTS` 库的文档或 README 文件，以了解初始化和使用的具体说明。

如果以上步骤没有解决问题，可以提供更多关于 `ChatTTS` 库和你的设置的细节，以便进一步诊断问题。
"""
tts = gTTS(text=text, lang='zh')
tts.save("output.mp3")

# # 加载音频文件
# audio = AudioSegment.from_file("output.mp3")

# # 调整音色（例如，改变音调）
# # 提升一度（八度）
# octaves = 1.0
# new_sample_rate = int(audio.frame_rate * (2.0 ** octaves))

# # 使用新的采样率重新生成音频
# audio_high_pitch = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})
# audio_high_pitch = audio_high_pitch.set_frame_rate(44100)

# # 保存调整后的音频
# audio_high_pitch.export("output_high_pitch.mp3", format="mp3")

# # 播放调整后的音频
# playsound.playsound("output_high_pitch.mp3")
