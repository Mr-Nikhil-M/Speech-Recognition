import pyttsx3
txt_sp=pyttsx3.init()
text=input("enter the text...\n")
txt_sp.say(text)
txt_sp.runAndWait()
