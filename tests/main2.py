import speech_recognition as sr
import time

def noise(r):
    print(f"en.thr.: {r.energy_threshold}  din.en.thr.: {r.dynamic_energy_threshold}\n \
        di.en.ratio: {r.dynamic_energy_ratio}  din.en.adj.damp.: {r.dynamic_energy_adjustment_damping} \n\
        n.sp.dur.: {r.non_speaking_duration} ope.timout: {r.operation_timeout}\n \
        pause.thr: {r.pause_threshold}  phrase.thr: {r.phrase_threshold}")
    r.energy_threshold *=2
    print(f"en.thr.: {r.energy_threshold}  din.en.thr.: {r.dynamic_energy_threshold}\n \
        di.en.ratio: {r.dynamic_energy_ratio}  din.en.adj.damp.: {r.dynamic_energy_adjustment_damping} \n\
        n.sp.dur.: {r.non_speaking_duration} ope.timout: {r.operation_timeout}\n \
        pause.thr: {r.pause_threshold}  phrase.thr: {r.phrase_threshold}")




def listen():
    r = sr.Recognizer()
    m = sr.Microphone()
    print("noise check - start")
    with m as source:
        a=r.adjust_for_ambient_noise(source, 2)  # we only need to calibrate once, before we start listening
    print("noise check - end")
    r.energy_threshold *=2
    r.dynamic_energy_ratio = 2

    with m as source:
        print("Listening...")
        while True:
            try:
                audio = r.listen(source)#, phrase_time_limit=5) # set timeout to 5 seconds

                text = r.recognize_google(audio, language='en-in') #it-IT #en-in

                if text:
                    print(f"You said: {text}")
                if text =="exit" or text =="Exit":
                    exit(0)
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