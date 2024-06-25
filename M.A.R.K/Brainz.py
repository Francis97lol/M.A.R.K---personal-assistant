import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import requests, json
import random
import subprocess
import webbrowser
import sys
import os
import pyautogui
import cv2
import time
import re
import psutil
import rotatescreen
import keyboard
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from playsound import playsound 


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume)) 


#interaction responses

#Response 1 

wiishMe_morning_respList = {
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net).mp3": 1,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (2).mp3": 2,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (3).mp3": 3,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (4).mp3": 4,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (5).mp3": 5,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (6).mp3": 6,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (7).mp3": 7,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (8).mp3": 8,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (9).mp3": 9,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (10).mp3": 10,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (11).mp3": 11,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (12).mp3": 12,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (13).mp3": 13,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (14).mp3": 14,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (15).mp3": 15,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (16).mp3": 16,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (17).mp3": 17,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (18).mp3": 18,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Wish me\Routine\morning\Voice\Morning (mp3cut.net) (19).mp3": 19,
}





listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    time = datetime.datetime.now().strftime('%I %M %p')
    search = "temperature"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_="BNeawe").text

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=11:
        morning_response = random.choice(list(wiishMe_morning_respList.keys()))
        playsound(morning_response)


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mark' in command :
                print(command)
    except:
        pass
    return command

#interaction responses

#Response 1 

interaction_responses_list1 = {
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus1.mp3": 1,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus2.mp3": 2 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus3.mp3": 3 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus4.mp3": 4 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus5.mp3": 5 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus6.mp3": 6 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus7.mp3": 7 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus8.mp3": 8 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus9.mp3": 9 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus10.mp3": 10 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus11.mp3": 11 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus12.mp3": 12 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus13.mp3": 13 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus14.mp3": 14 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus15.mp3": 15 ,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response1\Voice\Marcus16.mp3": 16 ,
    
}

#Response 2

interaction_responses_list2 = {
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus2.mp3": 1,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus3.mp3": 2,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus3.mp3": 3,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus4.mp3": 4,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus5.mp3": 5,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus6.mp3": 6,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus7.mp3": 7,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus8.mp3": 8,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus9.mp3": 9,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus10.mp3": 10,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus11.mp3": 11,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response2\Voice\Marcus12.mp3": 12,

}

interaction_responses_list3 = {
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus1.mp3": 1,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus2.mp3": 2,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus3.mp3": 3,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus4.mp3": 4,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus5.mp3": 5,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus6.mp3": 6,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus7.mp3": 7,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus8.mp3": 8,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus9.mp3": 9,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus10.mp3": 10,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus11.mp3": 11,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response3\Voice\Marcus12.mp3": 12,

}

interaction_responses_list4 = {
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus1.mp3": 1,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus2.mp3": 2,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus3.mp3": 3,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus4.mp3": 4,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus5.mp3": 5,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus6.mp3": 6,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus7.mp3": 7,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus8.mp3": 8,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus9.mp3": 9,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus10.mp3": 10,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus11.mp3": 11,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus12.mp3": 12,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus13.mp3": 13,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus14.mp3": 14,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus15.mp3": 15,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus16.mp3": 16,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus17.mp3": 17,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus18.mp3": 18,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus19.mp3": 19,
fr"C:\Users\Franek\Desktop\M.A.R.K\interaction-responses\Response4\Voice\Marcus20.mp3": 20,
}



#Func responses
jokes = {
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus1.mp3": 1,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus2.mp3": 2,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus3.mp3": 3,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus4.mp3": 4,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus5.mp3": 5,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus6.mp3": 6,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus7.mp3": 7,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus8.mp3": 8,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus9.mp3": 9,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus10.mp3": 10,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus11.mp3": 11,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus12.mp3": 12,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus13.mp3": 13,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus14.mp3": 14,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus15.mp3": 15,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus16.mp3": 16,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus17.mp3": 17,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus18.mp3": 18,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus19.mp3": 19,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus20.mp3": 20,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus21.mp3": 21,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus22.mp3": 22,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus23.mp3": 23,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus24.mp3": 24,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus25.mp3": 25,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus26.mp3": 26,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus27.mp3": 27,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus28.mp3": 28,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus29.mp3": 29,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus30.mp3": 30,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus31.mp3": 31,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus32.mp3": 32,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus33.mp3": 33,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus34.mp3": 34,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus35.mp3": 35,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus36.mp3": 36,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus37.mp3": 37,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus38.mp3": 38,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus39.mp3": 39,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus40.mp3": 40,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus41.mp3": 41,
fr"C:\Users\Franek\Desktop\M.A.R.K\Func-responses\Jokes\Voice\Marcus42.mp3": 42,

}

command = ""
def run_marcus():
    command = ""
    command = take_command()
    print(command)


    #funcional things 

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M: %p')
        talk('Current time is ' + time)


    elif 'joke' in command or "another" in command:
        joke = random.choice(list(jokes.keys()))
        playsound(joke)
        


    
    elif "shut down" in command:
        talk("Ok, goodbye")
        sys.exit()

    elif "screenshot" in command:
        talk("Nice picture brother")
        myScreenshot = pyautogui.screenshot() 
        myScreenshot.save(r"C:\Users\Franek\Pictures\Saved Pictures\snoop-screenshots.png")     

    elif "how am i looking" in command:
        talk("Here you go!")
        # define a video capture object
        vid = cv2.VideoCapture(0)
  
        while vid.isOpened() :
            
                                                    # Capture the video frame
                                                    # by frame
            ret, frame = vid.read()
                                                    # the 'q' button is set as the
                                                    # quitting button you may use any
                                                    # desired button of your choice 
            if cv2.waitKey(10) == ord("q"):
                break
            # Display the resulting frame
            cv2.imshow("MyPYCamera", frame)
                 
        #Chrome

    elif "chrome" in command and "exit" not in command:
        talk("Opening chrome")
        browser = webdriver.Chrome(executable_path= "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        browser.get("https://google.com")


    elif "exit" in command and "chrome":
        subprocess.call("TASKKILL /F /IM chromedriver.exe", shell=True)

        #minecraft

    elif "minecraft" in command and "exit" not in command:
        talk("opening minecraft")
        program = "C:\Program Files (x86)\Minecraft\MinecraftLauncher.exe"
        subprocess.Popen([program])

    elif "exit" in command and "minecraft":
        subprocess.call("TASKKILL /F /IM MinecraftLauncher.exe", shell=True)

        #youtube

    elif "youtube" in command and "youtube music" not in command and "exit" not in command:
        talk("opening youtube")
        webbrowser.open("https://www.youtube.com/")

    elif "exit" in command and "youtube":
        keyboard.press_and_release('ctrl+w')

        #notepad

    elif "notepad" in command and "exit" not in command:
        program = fr"C:\WINDOWS\system32\notepad.exe"
        subprocess.Popen([program])
    
    elif "exit" in command and "notepad":
        subprocess.call("TASKKILL /F /IM notepad.exe", shell=True)

        #youtube music

    elif "youtube music" in command: 
        talk("Opening youtube music")
        webbrowser.open("https://music.youtube.com/")

    elif "exit" in command and "youtube music":
        keyboard.press_and_release('ctrl+w')

        #udemy

    elif "udemy" in command:
        talk("Opening Udemy courses")
        webbrowser.open("https://www.udemy.com/")

        #brilliant

    elif "brilliant" in command:
        talk("Opening Brilliant")
        webbrowser.open("https://brilliant.org/")

    elif "stack" in command or "stock" in command:
        talk("Opening Stack overflow")
        webbrowser.open("https://stackoverflow.com/")

    elif "github" in command:
        talk("Opening Git hub")
        webbrowser.open("https://github.com/")

    elif "vinted" in command or "vintage" in command:
        talk("Opening Vinted")
        webbrowser.open("https://vinted.pl/")

    elif "hosting" in command:
        talk("Opening prv free hosting")
        webbrowser.open("https://www.prv.pl/hosting")

    elif "schools" in command or "w3schools" in command:
        talk("Opening w three schools")
        webbrowser.open("https://www.w3schools.com/")

    elif "netflix" in command:
        talk("Opening Netflix")
        webbrowser.open("https://netflix.com/")

    elif "mail" in command:
        talk("Opening Gmail")
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl")

    elif "vscode" in command or "visual studio" in command and "exit" not in command:
        program = fr"C:\Users\Franek\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        subprocess.Popen([program])

    elif "exit" in command and "visual studio" in command or "exit" in command and "vscode" in command:
        subprocess.call("TASKKILL /F /IM Code.exe", shell=True)







        #Special Protocols



    elif "volume" in command:

        if "mute" in command and "un" not in command:
            volume.SetMute(1, None)
            print("muted")
        elif "unmute" in command:
            volume.SetMute(0, None)
            print("Unmuted")
        elif "set the volume" in command and "mute" not in command and "decrease" not in command:
            current = int(re.search(r'\d+', command).group())
            if current == 100 :
                finalResult = current - 99 
                print(finalResult)
                volume.SetMasterVolumeLevelScalar(finalResult,None)

            elif current <=9 : 
                result = str(current) 
                result = "0.0" + result 
                finalResult = float(result)  
                print(finalResult) 
                volume.SetMasterVolumeLevelScalar(finalResult,None) 

            elif current>=10 and current<100: 
                result = str(current) 
                result = "0." + result 
                finalResult = float(result) 
                print(finalResult)
                volume.SetMasterVolumeLevelScalar(finalResult,None)

            else: 
                talk("I have no power to boost the percentage beyond 100%")



        elif "decrease" in command and "by" in command:
            current = int(re.search(r'\d+', command).group())
            currentVolume = volume.GetMasterVolumeLevelScalar() 

            if current>=10 and current<100: 
                result = str(current) 
                result = "0." + result
                finalResult = float(result) 
                decreasedVolume = currentVolume - finalResult
                print(decreasedVolume)
                volume.SetMasterVolumeLevelScalar(decreasedVolume,None)

            
            elif current <=9:
                result = str(current) 
                result = "0.0" + result 
                finalResult = float(result)  
                decreasedVolume = currentVolume - finalResult
                print(decreasedVolume) 
                volume.SetMasterVolumeLevelScalar(decreasedVolume,None)

            elif current == 100 :
                finalResult = current - 99 
                decreasedVolume = currentVolume - finalResult
                print(decreasedVolume) 
                volume.SetMasterVolumeLevelScalar(decreasedVolume,None)

            

        elif "increase" in command and "by" in command:
            current = int(re.search(r'\d+', command).group())
            currentVolume = volume.GetMasterVolumeLevelScalar() 

            if current>=10 and current<100: 
                result = str(current) 
                result = "0." + result 
                finalResult = float(result) 
                increasedVolume = currentVolume + finalResult 
                print(increasedVolume)
                if increasedVolume >= 1 :
                    volume.SetMasterVolumeLevelScalar(1,None)
                else:
                    volume.SetMasterVolumeLevelScalar(increasedVolume,None)



            
            elif current <=9: 
                result = str(current)  
                result = "0.0" + result 
                finalResult = float(result)  
                increasedVolume = currentVolume + finalResult
                print(increasedVolume) 
                if increasedVolume >= 1 :
                    volume.SetMasterVolumeLevelScalar(1,None)
                else:
                    volume.SetMasterVolumeLevelScalar(increasedVolume,None)



            elif current == 100 :
                finalResult = current - 99 
                increasedVolume = currentVolume + finalResult
                print(increasedVolume) 
                if increasedVolume >= 1 :
                    volume.SetMasterVolumeLevelScalar(1,None)
                else:
                    volume.SetMasterVolumeLevelScalar(increasedVolume,None)



        elif "max" in command :
            volume.SetMasterVolumeLevelScalar(1,None)
        elif "half the" in command or "half of" in command:
            if volume.GetMasterVolumeLevelScalar() == 0:
                talk("Can't divide by a zero like u")
            else:
                halfedVolume = volume.GetMasterVolumeLevelScalar() / 2
                volume.SetMasterVolumeLevelScalar(halfedVolume,None)


    elif "flip" in command:
        screen = rotatescreen.get_primary_display()
        for i  in range(5):
            screen.rotate_to(i*90 % 360)






    #Iteraction with a Marcus

    elif 'how you doing' in command:
        response1 = random.choice(list(interaction_responses_list1.keys()))
        playsound(response1)

    elif 'alexa' in command or 'siri' in command:
        response2 = random.choice(list(interaction_responses_list2.keys()))
        playsound(response2)

    elif 'what is your name' in command:
        response3 = random.choice(list(interaction_responses_list3.keys()))
        playsound(response3)


    elif "you in a relationship" in command:
        response4 = random.choice(list(interaction_responses_list4.keys()))
        playsound(response4)
    
    

    elif "doing great" in command and "doing good":
        response5 = random.choices(list(interaction_responses_list5.keys()))


    

    

    


    


    else:
        talk("")



while True:
    run_marcus()
    time = datetime.datetime.now().strftime('%I:%M: %p')