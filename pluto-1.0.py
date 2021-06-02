import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wp
import smtplib as smtp
import webbrowser as wb
import psutil
import pyjokes
import pyautogui
import getpass
import uuid
import json
import requests
from urllib.request import urlopen
import time
import os
from tabulate import tabulate

engine = pyttsx3.init()

def speak(audio):
    engine.setProperty('rate', 145)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.say(audio)
    engine.runAndWait()

def time_():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(time)

def date_():
    date = datetime.datetime.now().strftime("%d %B %Y")
    speak("The current date is")
    speak(date)

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("Welcome back " + getpass.getuser())
    #time_()
    #date_()
    speak("Pluto at your service. Please tell me how can i help you today?")

def sendEmail(to, content):
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('plutoai1.0@gmail.com', 'Deva@123')
    server.sendmail('plutoai1.0@gmail.com', to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Pluto: listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Pluto: Recognizing...')
        query = r.recognize_google(audio, language = "en-in")
        print(getpass.getuser() + ': ' + query)
    
    except Exception as e:
        print(e)
        print("Pluto: Sorry! Can you please say that again")
        return "None"
    return query

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU usage is " + usage)

    battery = psutil.sensors_battery()
    speak('Battery is at ')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

def whatCanIDo():
    actions = [["Tell date", "Tell me current date"],
    ["Tell time", "Tell me current time"],
    ["Wikipedia Search", "wikipedia 'Search term'"],
    ["Google Search", "Search in google"],
    ["Youtube Search", "Search in Youtube"],
    ["CPU & Battery Status", "What is the CPU status"],
    ["Tell Joke", "tell me a joke"],
    ["Shutdown", "go offline"],
    ["send email", "send a mail"],
    ["Get help", "What can you do?"],
    ["Take screenshot", "Take a screenshot"],
    ["Set reminder", "Remind me"],
    ["Show reminder", "Show reminders"],
    ["Tell news", "tell me some news"],
    ["Location search", "Where is London"],
    ["Stop Listening", "Stop Listening"],
    ["Log out System", "Log out"],
    ["Restart System", "Restart"],
    ["Shutdown system", "Shutdown"],
    ]
    print(tabulate(actions, headers=['Actions', 'Commands'], tablefmt='orgtbl'))

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/' + getpass.getuser() + '/Pictures/screenshot_' + str(uuid.uuid1()) + '.png')

def latestNews():
    try:
        jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=in&apiKey=a924755fa92942cf859520c4af8c69e0')
        data = json.load(jsonObj)
        i = 1
        speak('Here are some top headlines in our country')
        print('========================Top Headlines========================' + '\n')
        for item in data['articles']:
            print(str(i) + '.' + item['title'] + '\n')
            speak(item['title'])
            print(item['description'] + '\n')
            if i == 5:
                break
            i += 1
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    screenshot()
    wishme()
    whatCanIDo()
    while True:
        query = takeCommand().lower()
        if 'date' in query:
            date_()
        if 'time' in query:
            time_()
        elif 'wikipedia' in query:
            try:
                speak(" Searching..")
                query = query.replace('wikipedia', '')
                result = wp.summary(query, sentences=3)
                speak(" According to Wikipedia")
                print(result)
                speak(result)
            except Exception as e:
                speak('Please be more specific')
        elif 'send email' in query or 'send a mail' in query:
            try:
                speak(" What should i say ?")
                content = takeCommand()
                speak(" Who is the reciever?")
                reciever = input("Enter reviever's email: ")
                sendEmail(reciever, content)
                speak(content)
                speak('Email has been sent.')
            except Exception as e:
                print(e)
                speak('unable to send the email')
        elif 'search in google' in query or 'google' in query:
            speak('what should i search?')
            chromePath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            search = search.split(" ")
            speak('Here we go to Chrome!')
            url = 'https://www.google.com/search?q=' + '+'.join(search)
            wb.get(chromePath).open_new_tab(url)
        elif 'search in youtube' in query or 'youtube' in query:
            speak('what should i search?')
            chromePath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            search = search.split(" ")
            speak('Here we go to youtube!')
            url = 'https://www.youtube.com/results?search_query=' + '+'.join(search)
            wb.get(chromePath).open_new_tab(url)
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            joke()
        elif 'go offline' in query or 'offline' in query:
            speak('Going Offline')
            quit()
        elif 'what can you do' in query:
            whatCanIDo()
        elif 'screenshot' in query:
            screenshot()
            speak('Screenshot stored in Picture folder')
        elif 'remind me' in query:
            speak("What's the reminder? ")
            memory = takeCommand()
            speak('You asked me to remind that ' + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()
        elif 'show reminder' in query:
            remember = open('memory.txt', 'r')
            speak('You asked me to remind that ' + remember.read())
        elif 'news' in query:
            latestNews()
        elif 'where is' in query:
            query = query.replace('where is', '')
            location = query
            speak('user asked to locate ' + location)
            wb.open_new_tab('https://www.google.com/maps/place/' + location)
        elif 'stop listening' in query:
            speak('How many seconds do you want me to stop listening to your commands?')
            ans = takeCommand().lower()
            while ans == 'none':
                ans = takeCommand().lower()
            seconds = int(ans.replace('seconds', '').replace('second', ''))
            print('Pluto: Shutting down for ' + ans)
            time.sleep(seconds)
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
        elif 'log out' in query:
            os.system('shutdown -l')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
