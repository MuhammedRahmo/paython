from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import googletrans
from googletrans import Translator

translator = Translator()
print(googletrans.LANGUAGES)
r = sr.Recognizer()
with sr.Microphone() as src:
    print("Say something......")
    audio = r.listen(src)
try:
    t = r.recognize_google(audio, language='ar-AR')
    lg = 'en'
    translation = translator.translate(t, dest=lg)
    print(translation.origin)
    print(translation.text)
    obj = gTTS(text=translation.text, lang=lg, slow=False)
    obj.save('text.mp3')
    playsound('text.mp3')
except sr.UnknownValueError as U:
    print(U)
except sr.RequestError as R:
    print(R)
