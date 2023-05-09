import win32com.client as wincom

if  __name__ == '__main__':
    print("Wellcome to RoboSpeaker Created by Dibyajyoti")
    speak = wincom.Dispatch("SAPI.SpVoice")
    while True:
        x = input("Enter what you want to say: ")
        if x =='q':
            text = 'thanks for using robospeaker bye bye'
            speak.Speak(text)
            break
        text = f'{x}'
        speak.Speak(text)
