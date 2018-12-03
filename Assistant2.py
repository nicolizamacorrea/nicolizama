import pyttsx3
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather

def talkToMe(audio):
    "speaks audio passed as argument"
    print(audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

    #  use the system's inbuilt say command instead of mpg123
     # text_to_speech = gTTS(text=audio, lang='en')
     # text_to_speech.save('audio.mp3')
     # os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listo')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='es-ES').lower()
        print('Tu dices: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print(talkToMe('No pude escucharte, Repiteme '))
        command = myCommand();

    return command




def assistant(command):
    "if statements for executing commands"

    if 'abrir reddit' in command:
        reg_ex = re.search('abrir reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
        
    elif 'abrir gmail' in command:
        reg_ex = re.search('abrir gmail (.+)', command)
        url = 'https://www.gmail.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print(talkToMe('Hecho!'))
        
    elif 'escuchar primus' in command:
        reg_ex = re.search('escuchar primus (.*)', command)
        url = 'https://www.youtube.com/watch?v=R7jnhTDg4mk'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
        
    elif 'facebook' in command:
        reg_ex = re.search('facebook (.*)', command)
        url = 'https://www.facebook.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

   # elif 'abrir' in command:
    #    reg_ex = re.search('abrir (.+)', command)
     #   if reg_ex:
      #      domain = reg_ex.group(1)
       #     url = 'https://www.' + domain
        #    url.replace("", "%20")
         #   webbrowser.open(url)
          #  print('Listo!')
       # else:
        #    pass

    elif 'feliz' in command:
        talkToMe(' muy feliz mostacero ')
        
    elif 'aloja' in command:
        talkToMe('yo bien y tu papa ')
        
    elif 'broma' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    
    
    elif 'email' in command:
        talkToMe('Quien es el destinatario?')
        recipient = myCommand()

        if 'John' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('nicolas.lizama', 'sypuq245')

            #send message
            mail.sendmail('John Fisher', 'JARVIS2.0@protonmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        else:
            talkToMe('No se lo que dices!')


talkToMe('Hola Comanechi Estoy oyendo tus ordenes')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
    
