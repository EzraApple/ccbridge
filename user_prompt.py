import os
import csv
import azure.cognitiveservices.speech as speechsdk

def recognize_from_microphone():
    recognized_text = ""
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language="en-US"
    
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        recognized_text = speech_recognition_result.text
        print(format(recognized_text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return recognized_text

def name_validate(text):
    while True:
        text = recognize_from_microphone()
        text = text[:-1]
        if text in nlist:
            print('Success! Welcome', text, '!')
            break
        else if text == "Exit":
            print('Thank you for calling Totally Legit Travel Agency.')
        else:
            print('Name not found, please try again.')

nlist = []
with open('ccb_user_data.txt', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        fname = row['FirstName']
        lname = row['LastName']
        name = f"{fname} {lname}"
        nlist.append(name)

text = ""
name_validate(text)
