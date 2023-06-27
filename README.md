# G16-Asistentevirtual

Proceso: 
openai: Es el módulo openai que se importa al principio del código.
api_data: Es una variable importada del módulo apikey que contiene la clave de la API para OpenAI.
pyttsx3: Es el módulo pyttsx3 que se importa al principio del código.
speech_recognition: Es el módulo speech_recognition que se importa con el alias sr.
webbrowser: Es el módulo webbrowser que se importa al principio del código.
Variables dentro de la función Reply():
question: Es un parámetro de entrada que representa la pregunta a enviar a OpenAI.
Variables dentro de la función speak():
text: Es un parámetro de entrada que representa el texto que se desea convertir en habla.
Variables dentro de la función takeCommand():
r: Es un objeto Recognizer de la biblioteca speech_recognition.
audio: Es una variable que almacena el audio capturado por el micrófono.
Variables en el bloque principal:
engine: Es un objeto inicializado de la biblioteca pyttsx3 para la síntesis de voz.
voices: Es una lista de voces disponibles en el sistema.
query: Es una variable que almacena el comando de voz capturado y convertido en texto.
ans: Es una variable que almacena la respuesta generada por la función Reply().

Implementa una interacción de voz a texto con una IA basada en el modelo de OpenAI. La IA responde a las preguntas del usuario utilizando el modelo y se utiliza la síntesis de voz para que la IA hable las respuestas. Además, se proporcionan comandos para abrir sitios web específicos como YouTube y Google. El programa se ejecuta en un bucle infinito hasta que el usuario diga "finalizar" para salir del programa.
