# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:56:24 2021

@author: Pruthvi
"""


from gtts import gTTS
import os

mytext = 'unplaced universe'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")
