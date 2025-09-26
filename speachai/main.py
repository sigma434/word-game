import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from deep_translator import GoogleTranslator
import random
import time


duration = 3  # секунды записи
sample_rate = 44100



words_by_level = {
    "easy": ["кот", "собака", "яблоко", "молоко", "солнце"],
    "medium": ["банан", "школа", "друг", "окно", "жёлтый"],
    "hard": ["технология", "университет", "информация", "произношение", "воображение"]
}
lvl=input("Выбери сложность, есть 3 на выбор: easy, medium, hard: " )
print("Вам дадут 3 слова которые вам нужно превести на английский язык.")

p=0

for i in range(3) :

    word=random.choice(words_by_level[lvl], )
    print(word)
    print("У тебя есть 2 секунды на размышление, время пошло: 😃")
    time.sleep(2)

    print("Говори...")
    recording = sd.rec(
    int(duration * sample_rate), # длительность записи в сэмплах
    samplerate=sample_rate,      # частота дискретизации
    channels=1,                  # 1 — это моно
    dtype="int16")               # формат аудиоданных
    sd.wait()  # ждём завершения записи


    wav.write("output.wav", sample_rate, recording)
    print("Запись завершена, теперь распознаём...")
    


    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)


    try:
        text = recognizer.recognize_google(audio, language="en-Ru")
        print("Ты сказал:", text)


    except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
        print("Не удалось распознать речь.")
    except sr.RequestError as e:             # - если нет интернета или API недоступен
        print(f"Ошибка сервиса: {e}")


    translated = GoogleTranslator(source= 'auto', target= 'ru').translate(text)
    if translated.lower() == word :
        print("Правильно")
        p+=1
    else:
        print("Неправильно")

if p <= 1 :
    print("Ваше знание английского языка плохое, советуем вам его подтянуть.")

elif p == 2:
    print("Вы неплохо знаете английский язык.")

else:
    print("Вы хорошо знаете английский язык!")