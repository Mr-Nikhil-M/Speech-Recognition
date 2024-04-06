#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr

def speeech_recog():
    r=sr.Recognizer()
    mic=sr.Microphone()

    with mic as source:
        print("Speak....")
        r.energy_threshold=700 # this is not required and next one also because it is just to adjust the voice
        # r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

        try:
            text=r.recognize_google(audio)
            print("You said..",text)
        except:
            print("Didn't hear. Speak again..")

speeech_recog()
