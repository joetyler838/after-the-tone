import pyaudio
import wave

filename = 'drums.wav'

mainLoop = True
# Set chunk size of 1024 samples per data frame
chunk = 1024 
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = 4

p = pyaudio.PyAudio()

def record(input_index, user_count):
    print('Recording Audio')

    input_stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                input_device_index = int(input_index),
                frames_per_buffer=chunk,
                input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = input_stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    input_stream.stop_stream()
    input_stream.close()
    # Terminate the PortAudio interface

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open('recording_' + str(user_count) + '.wav', 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

## Play Wave File
def play():
    print('Playing Prompt')

    # Open the sound file
    filename = 'drums.wav' 
    sound = wave.open(filename, 'rb')
    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    output_stream = p.open(format = p.get_format_from_width(sound.getsampwidth()),
                    channels = sound.getnchannels(),
                    rate = sound.getframerate(),
                    output = True)

    # Read data in chunks
    data = sound.readframes(chunk)

    # Play the sound by writing the audio data to the stream
    while len(data) > 0:
        output_stream.write(data)
        data = sound.readframes(chunk)

    output_stream.stop_stream()
    output_stream.close()

def get_mic_list():
    print("----------------------record device list---------------------")
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

    print("-------------------------------------------------------------")

#Get input list
get_mic_list()
input_index = input("Input Mic index to use: ")
#count to icrement for audio file naming
user_count = 0
while (True):
    # Wait to do anything till someone picks up the phone
    input("Waiting for user to pick up the phone")

    play()

    record(input_index, user_count)
    user_count+=1

    #done with current user
    print('Saved audio file. Onto the next one')
