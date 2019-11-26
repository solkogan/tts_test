import pyttsx3

tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Irina':
        tts.setProperty('voice', voice.id)

tts.say('Привет, мир! Какой прекрасный сегодня день!')

tts.runAndWait()
