# encoding: utf-8
# Author: Cai Chenyi

import win32com.client
from time import sleep
from pygame import mixer

import os
import random


def txetSpeak(message, loop_time=1):
    for i in range(loop_time):
        speak = win32com.client.Dispatch('SAPI.SPVOICE')
        speak.Speak(message)


def playMusic(music_path, loop_time=1):
    for i in range(loop_time):
        mixer.init()
        music_name = os.listdir(music_path)[random.randrange(len(os.listdir(music_path)))]
        mixer.music.load(music_path + '{}'.format(music_name))
        mixer.music.play()
        while mixer.music.get_busy():
            sleep(3)
        mixer.quit()
        # os.remove(music_path + '{}'.format(music_name))