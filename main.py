from google.cloud import speech_v1
import os
#setting Google credential
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= 'google_secret_key1.json'

def sample_long_running_recognize():
    # Create a client
    client = speech_v1.SpeechClient()

    # Initialize request argument(s)
    config = speech_v1.RecognitionConfig(
        encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
        audio_channel_count=2,
        enable_separate_recognition_per_channel=True,
    )
    audio = speech_v1.RecognitionAudio()
    with open("harvard.wav", "rb") as audio_file:
        audio.content = audio_file.read()
    request = speech_v1.LongRunningRecognizeRequest(
        config=config,
        audio=audio,
    )
    # Make the request
    operation = client.long_running_recognize(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

sample_long_running_recognize()



