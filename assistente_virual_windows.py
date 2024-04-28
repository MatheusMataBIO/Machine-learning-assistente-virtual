import speech_recognition as sr
import os

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = r.listen(source)
    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {query}")
        return query.lower()
    except Exception as e:
        print("Não foi possível reconhecer. Por favor tentar novamente.")
        return ""

def open_application(application_name):
    if "word" in application_name:
        os.system("start winword")
    elif "excel" in application_name:
        os.system("start excel")
    elif "calculadora" in application_name:
        os.system("start calc")

def main():
    while True:
        query = listen()
        if "abrir" in query:
            open_application(query)
        elif "sair" in query:
            print("Encerrando o assistente.")
            break
        else:
            print("Comando não reconhecido.")

if __name__ == "__main__":
    main()
