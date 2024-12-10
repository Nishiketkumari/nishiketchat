import speech_recognition as sr
import os
import pyttsx3
import win32com.client
import webbrowser
import openai
import datetime


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
       return "some error occured.sorry !"
    

if __name__ == '__main__':

   engine = pyttsx3.init()
   engine.say("Hello Learners")
   engine.runAndWait()
   while True:
    print("Listening...")
    query = takeCommand()
    
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
    for site in sites:
     if f"Open {site[0]}".lower() in query.lower():
        engine.say(f"opeinig {site[0]}...")
        webbrowser.open(site[1])
    if "open music" in query:
       musicpath = r"C:/Users/DELL/Downloads/song.mp3"  # Provide the full path to the file
       os.startfile(musicpath)

    if "the time" in query:
       musicpath = r"C:/Users/DELL/Downloads/song.mp3"  # Provide the full path to the file
       strfTime = datetime.datetime.now().strftime("%H:%M:%S")
       engine.say(f"the time is {strfTime}")
    
    if "open code app" in query:
       os.system(f"C:/Users/DELL/OneDrive/Desktop/Dev-C++.lnk")
      

       #engine.say("query")
       engine.runAndWait()
       

 