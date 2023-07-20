import speech_recognition as sr
import pyttsx3
from pynput.keyboard import Key, Controller
import time





# Initialize the recognizer
r = sr.Recognizer()



def SpeakText(command):


    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()




while(1):


    try:


        with sr.Microphone() as source2:


            r.adjust_for_ambient_noise(source2, duration=0.1)


            audio2 = r.listen(source2)


            MyText = r.recognize_google(audio2, language = 'bn-Bd')
            MyText = MyText.lower()

            keyboard = Controller()


            def split(words):
                return [char for char in words]

            for i in split(MyText + ". "):
                keyboard.type(i)
                time.sleep(.05)
            print("Saying.... " + MyText)
            SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
        print("Could not recognize")