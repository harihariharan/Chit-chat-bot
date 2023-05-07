import sys
import time
import pandas as pd
import re
import speech_recognition as sr
import pyttsx3
import nltk
import smtplib
import imaplib
import email
import requests
import bs4
import datetime as dt
import random
import sys
# nltk.download('vader_lexicon') #use this for first time installation alone

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
#from accounts import patients, doctors
#
#from rooms import *

from intents_responses_copy import *
from chitchat import chit_chat
from email.message import EmailMessage





def voice_output(msg):
    engine = pyttsx3.init()
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 0.7)
    engine.say(str(msg))
    engine.runAndWait()



def match_room(msg, room_pattern):
    msg = msg.lower()
    matched_intent = None
    for intent, pattern in room_pattern.items():
        if re.search(pattern, msg):
            matched_intent = intent

    return matched_intent


def match_intent(msg, patterns):
    msg = msg.lower()
    matched_intent = None
    for intent, pattern in patterns.items():
        if re.search(pattern, msg):
            matched_intent = intent

    return matched_intent


def details():
    # global username, password
    username, password=0,0
    room_number = speech_input(listen=3)
    room_number = match_room(room_number, room_pattern)
    if room_number in patients.keys():
        username = patients[room_number][0]
        password = patients[room_number][1]
    else:
        voice_output('Sry your not a registered user.')
        print('Assistant : Sry your not a registered user.')
        details()

    return username, password, room_number


def respond(msg):
    response_intent = match_intent(msg, patterns)
    keys = 'default'
    if response_intent == 'stop':
        keys = 'stop'
    elif response_intent in responses:
        keys = response_intent

    return keys


def mail():
    #     if p_id != 0:
    voice_output('Please wait I am processing your message to send')
    # msg = 'Hi therre'
    SUBJECT = "Hello!"


    TEXT = "This message was sent with Python's smtplib."
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.starttls()
    mailServer.login('fridayabc12@gmail.com', '1@34567890')
    mailServer.sendmail('fridayabc12@gmail.com','pradeepsuresh625@gmail.com', msg)
    voice_output('Message sent to Hariharan  successfully')
    print('Assistant : Message sent Hariharn successfully')



def indian_news():

    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])
    print('Assistant : Here are the top' + str(len(results)) + ' headlines from Times of India')
    voice_output('Here are the top' + str(len(results)) + ' headlines from Times of India')
    for line in results:
        print(line)
        voice_output(line)

def weather():

    
    query_params = {
        "source": "open-weather",
        "sortBy": "top",
        "apiKey": "09b81f89d3b957565acc677ba4a8a4cc"
    }
    main_url = "https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=09b81f89d3b957565acc677ba4a8a4cc"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_weather_page= res.json()

    # getting all articles in a string article
    article = open_weather_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all data
        print(i + 1, results[i])
    print('Assistant : Here are the top' + str(len(results)) + ' weather data from OpenWeather')
    voice_output('Here are the top' + str(len(results)) + ' weather data from OpenWeather')
    for line in results:
        print(line)
        voice_output(line)


def ask_dt(key):
    now = dt.datetime.now()
    if key == 'time':
        dt_string = now.strftime("%H:%M:%S")
        print("Assistant : The time is {} ".format(dt_string))
        voice_output("The time is:{}" .format(dt_string))
    else:
        dt_string = now.strftime("%d/%m/%Y")
        print("Assistant : The date is {} ".format(dt_string))
        voice_output("The date is:{} ".format(dt_string))





def speech_input(listen):
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print('Listening')
        input_audio = r.record(src, duration=listen)
        converted_text = ''
        try:
            converted_text = r.recognize_google(input_audio)
            print('Speaker : {}'.format(converted_text))
        except:
            print('Going sleep for 3 secs')

    return converted_text




def room(room_number):
    print("Your room number is: {}".format(room_number))
    voice_output("Your room number is: {}".format(room_number))

def remainder():
    print("Hello, You have your Robotics assignment to be submitted next week and also you need to review your open elective ")
    voice_output("Hello, You have your Robotics assignement to be submitted next week and also you need to review your open elective ")




def self_intro():
    print("Hi, I am your personal assistant bot created by Robotics and Automation Club .")

    voice_output('Hi, I am your personal assistant bot created by Robotics and Automation Club .')


def process_msg(msg):

    gfg = TextBlob(msg)
    gfg = str(gfg.correct())
    a = word_tokenize(gfg)
    lem = WordNetLemmatizer()
    b = []
    for w in a:
        b.append(lem.lemmatize(w))
    c = TreebankWordDetokenizer().detokenize(b)

    return c


print("Please tell the wake up word to start the robot.")
voice_output("Please tell the wake up word to start the robot")
x=1
while True:

    WAKE = "Friday"
    #strt = input()
    strt = speech_input(3)
    if strt.count(WAKE) > 0.5:
        speaker = []
        assistant = []
        # sentiment = []
        patient_chat = {}
        print('Welcome, I am your personal assistant Friday ')
        voice_output('Welcome, I am your personal assistant Friday')
        print('Assistant : To chat with me tell Name')
        voice_output('To chat with me tell your Name')
        # username, password, room_number = details()
        # room_no=room_number
        print("You can chat with me now")
        voice_output('You can chat with me now')
        msg = speech_input(listen=5)
        preprocess_msg = process_msg(msg)
        if preprocess_msg != None:
            key = respond(preprocess_msg)

        while key!="stop":
            msg = speech_input(listen=5)
            preprocess_msg = process_msg(msg)

            if msg!=["bye","quit","exit",'']:
                if preprocess_msg != None:
                    key = respond(preprocess_msg)
                    if key == 'stop':
                        break

                    elif key == 'intro':
                        self_intro()
                    elif key == 'mail':
                        mail()
                    elif key == 'news':
                        indian_news()
                    elif key == 'weather':
                        weather()

                    elif key == 'remainder':
                        remainder()

                    elif (key == 'time') or (key == 'date'):
                        ask_dt(key)
                    elif key == 'self intro':
                        self_intro()
                    elif key == 'default':
                        reply = chit_chat(msg)
                        speaker.append(preprocess_msg)
                        assistant.append(reply)
                        # sentiment.append(sentiment_analyse(msg))
                    else:
                        response_speech = random.choice(responses[key])
                        print('Assistant : {}'.format(response_speech))
                        voice_output(response_speech)
                        speaker.append(msg)
                        assistant.append(response_speech)

            elif key == 'stop':

                voice_output("bye")
                print("Bye")
                break

                patient_chat['assistant'] = assistant
                patient_chat['speaker'] = speaker


                chat = pd.DataFrame(patient_chat)
                filename = username.split('@')[0] + '_' + room_number + '.csv'
                chat.to_csv(filename)
        print("Good bye. See you again")
        voice_output("Good bye. See you again")
        break
