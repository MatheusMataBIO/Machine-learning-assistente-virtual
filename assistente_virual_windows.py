import speech_recognition as sr
import os

# Função que vai permitir a captura de voz do usuário
def listen():
    r = sr.Recognizer() # Permiti reconhecer a fala
    with sr.Microphone() as source: # Abre o microfone
        print("Diga algo...")
        audio = r.listen(source) # Capta o áudio e armazena na váriavel áudio
    try: # Vai tratar erros e erros
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR') # Converte o áudio texto usando o serviço do google speech recognition
        # Especifica que o reconhecimento deve ser feito em português
        print(f"Você disse: {query}")
        return query.lower()
    except Exception as e:
        print("Não foi possível reconhecer. Por favor tentar novamente.")
        return ""

# Função que define quais aplicações serão abertas segundo o comando do usuário. Nesse caso (word, excel e calculadora)
def open_application(application_name):
    if "word" in application_name:
        os.system("start winword")
    elif "excel" in application_name:
        os.system("start excel")
    elif "calculadora" in application_name:
        os.system("start calc")

# Função que define a função principal do programa e reconhece o comando de abrir e sair da aplicação
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
