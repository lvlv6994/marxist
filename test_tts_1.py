from gtts import gTTS
text = """
萨米尔阿明有一个观点是资本主义就是帝国主义，这是比较狠的。也就是现在的中国强调，咱们是种地的民族，没有侵略的基因，似乎自能哄一下自己人而已（当年的韬光养晦，某种程度上是在哄自己）。中国的姓资姓社这个问题不单纯是国内政治问题，也可能是国际问题了。 
"""
tts = gTTS(text = text, lang='zh')
tts.save("output.mp3")