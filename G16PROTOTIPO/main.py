import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser

openai.api_key=api_data

completion=openai.Completion()

def Reply(question):
    prompt=f'Chando: {question}\n IA: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Respuesta'], max_tokens=800)
    answer=response.choices[0].text.strip()
    return answer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hola, que puedo servir?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Escuchando....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Analizando.....")
        query=r.recognize_google(audio, language='es-MX')
        print("Chando Said: {} \n".format(query))
    except Exception as e:
        print("Dime de nuevo....")
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query=takeCommand().lower()
        ans=Reply(query)
        print(ans)
        speak(ans)
        if 'abrir youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'abri google' in query:
            webbrowser.open("www.google.com")
        if 'finalizar' in query:
            break



