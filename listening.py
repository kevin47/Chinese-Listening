#!/usr/bin/env python3

import random, sys, os
from gtts import gTTS
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
from pygame import mixer

if len(sys.argv) <= 1:
    words = open('file.txt', 'r').read().strip().split()
else:
    words = []
    for f in sys.argv[1:]:
        words += open(f, 'r').read().strip().split()
#print(words)

random.shuffle(words)

for w in words:
    tts = gTTS(w, lang='zh-tw')
    tts.save('tmp.mp3')

    mixer.init()
    mixer.music.load('tmp.mp3')
    mixer.music.play()
    input('下一個請按Enter...')

os.remove('tmp.mp3')
