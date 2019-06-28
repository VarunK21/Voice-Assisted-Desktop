from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/' + sub
        webbrowser.open(url)
        print('Done!')
    if 'open youtube' in command:
        reg_ex = re.search('open youtube (.*)', command)
        url = 'https://www.youtube.com/'
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/' + sub
        webbrowser.open(url)
        print('Done!')
    if 'open gmail' in command:
        reg_ex = re.search('open gmail (.*)', command)
        url = 'https://www.gmail.com/'
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/' + su
        webbrowser.open(url)
        print('Done!')
    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')
    elif 'Hii, how are you' in command:
        talkToMe('I am great , how are you')
    elif "What's your name" in command:
        talkToMe('My name is Erica')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())


