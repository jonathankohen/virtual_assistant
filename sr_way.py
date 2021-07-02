import pyaudio
import speech_recognition as sr
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print(f"Google Speech Recognition thinks you said {r.recognize_google(audio)}")
    if r.recognize_google(audio) == "rabbit":
        webbrowser.open("http://docs.python.org/lib/module-webbrowser.html")
        web.find_element_by_xpath('//*[@id="searchInput"]')
        # loginInput.send_keys(username)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition server. {e}")
