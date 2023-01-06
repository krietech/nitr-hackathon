import speech_recognition as sr
# #Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
# r = sr.Recognizer()
# # Reading Audio file as source
# #  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
# with sr.AudioFile('video1.3gp') as source:
#     audio_text = r.listen(source)
# # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
#     try:
#         # using google speech recognition
#         text = r.recognize_google(audio_text)
#         print('Converting audio transcripts into text ...')
#         print(text)
#     except:
#          print('Sorry.. run again...')



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"{statement}\n")

        except Exception as e:
            # speak("Pardon me, please say that again")
            return "None"
        return statement

# speak('Loading your personal assistant')
takeCommand()