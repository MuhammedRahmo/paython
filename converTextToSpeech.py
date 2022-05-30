import pyttsx3
textSpeech =pyttsx3.init()

ans = input("what")

textSpeech.say(ans)
textSpeech.runAndWait()