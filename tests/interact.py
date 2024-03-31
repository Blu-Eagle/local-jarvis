import speech_recognition as sr
import ollama
import time

client = ollama.Client(host='http://localhost:11434')

def listen():
    r = sr.Recognizer()
    m = sr.Microphone()
    print("noise check - start")
    with m as source:
        a=r.adjust_for_ambient_noise(source, 2)  # we only need to calibrate once, before we start listening
    print("noise check - end")

    with m as source:
        print("Listening...")
        while True:
            try:
                audio = r.listen(source, phrase_time_limit=5) # set timeout to 5 seconds

                text = r.recognize_google(audio, language='it-IT') #it-IT #en-in

                if text:
                    print(f"You said: {text}")
                if text =="exit" or text =="Exit":
                    exit(0)

                stream = ollama.chat(
                    model='mistral',
                    messages=[{'role': 'user', 'content': text}],
                    stream=True,
                )
                for chunk in stream:
                    print(chunk['message']['content'], end='', flush=True)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {}".format(e))
            except KeyboardInterrupt:
                break
            except Exception as e:
                print("An error occurred: {}".format(e))
            time.sleep(0.1) # add a small delay before the next iteration

if __name__ == "__main__":
    listen()