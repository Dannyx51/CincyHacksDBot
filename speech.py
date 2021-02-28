import speech_recognition as sr

r = sr.Recognizer()
mc = sr.Microphone()

def callback(recog,audio):
    global sent  
    try:
        sent = r.recognize_google(audio)
        print(sent)
    except sr.UnknownValueError:
        print( "Could not understand")
    except sr.RequestError as e:
        print("Could not request Google Api; {0}".format(e))

with mc as source:
    r.adjust_for_ambient_noise(mc)

stop_listening = r.listen_in_background(mc, callback)

#stop_listening(wait_for_stop=False) < ---- stops audio recall