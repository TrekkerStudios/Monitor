"""
Monitor

©2017 Trekker Studios/Tyler Backer

"""

#Import libraries
import pyaudio
pA = pyaudio.PyAudio()
import time
import sys

#Device setup
devCt = pA.get_device_count()
devArray = []
for i in range(devCt):
    devArray.append(pA.get_device_info_by_index(i))

for i, dev in enumerate(devArray):
    print("%d - %s" % (i, dev['name']))

if len(sys.argv) < 3:
    input_device_read = input('Choose Input: ')
    output_device_read = input('Choose Output: ')
    input_device_index = int(input_device_read)
    output_device_index = int(output_device_read)
else:
    input_device_index = int(sys.argv[1])
    output_device_index = int(sys.argv[2])

print("Input: " + str(devArray[input_device_index]))
print("Output: " + str(devArray[output_device_index]))

#PyAudio setup

pyAudioWidth = 2
pyAudioChannels = 2
pyAudioRate = 44100
def pyAudioCallback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)
pyAudioIn = pA.open(format=pA.get_format_from_width(pyAudioWidth),
              channels=pyAudioChannels,
              rate=pyAudioRate,
              input=True,
              input_device_index = input_device_index,
              stream_callback=pyAudioCallback)
pyAudioOut = pA.open(format=pA.get_format_from_width(pyAudioWidth),
              channels=pyAudioChannels,
              rate=pyAudioRate,
              output=True,
              output_device_index = output_device_index,
              stream_callback=pyAudioCallback)

#Run audio stream
pyAudioIn.start_stream()
pyAudioOut.start_stream()
while pyAudioIn.is_active():
    time.sleep(0.1)
pyAudioIn.stop_stream()
pyAudioOut.stop_stream()
pyAudioIn.close()
pyAudioOut.close()
pA.terminate()
