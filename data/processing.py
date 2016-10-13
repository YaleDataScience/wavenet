import wave
import numpy as np
import struct
import audioop
import sys

SAMPLE_RATE = 24000     # Output/test data sample rate
Q_FACTOR = 1            # Additional linear quantization (for testing only)
LIMIT = 20              # Number of files
MIN_DURATION = 4.0      # Minimum duration in seconds

def preprocess(oldFileName):
	#preprocess takes in the name of a .wav file (oldFileName) and returns
	#u-law downsampled version of the file

	file = wave.open(filename, "rb")

	num_channels = file.getnchannels()
	sample_rate = file.getframerate()
	sample_width = file.getsampwidth()
	num_frames = file.getnframes()


	#Grab the bytes from our WAV file
	raw_frames = file.readframes(num_frames)
	file.close()

	total_samples = num_frames * num_channels

	if sample_rate != SAMPLE_RATE:
		u_law = audioop.ratecv(raw_frames, sample_width, num_channels, sample_rate, SAMPLE_RATE, None)
		u_law = audioop.lin2ulaw(u_law[0], sample_width)

	else:
		u_law = audioop.lin2ulaw(raw_frames, sample_width)

	u_law = list(u_law)
	u_law = [ord(x)//Q_FACTOR for x in u_law]

	return np.asarray(u_law)

def postprocess(data, newFileName, oldFileName):

	#postprocess converts a numpy array of a u-law quantized .wav file
	#into an actual file
	#parameters are the data array, the name for the output file, and the original file name

    # data is the u-law quantized sample
    u_law = data
    u_law = [chr(x) for x in u_law]
    u_law = ''.join(u_law)

    inputFile = wave.open(oldFileName, "rb")
    sample_width = inputFile.getsampwidth()
    num_channels = inputFile.getnchannels()
    inputFile.close()

    original = audioop.ulaw2lin(u_law, sample_width)
    print "output data size: " + str(len(original))

    output = wave.open(newFileName,'w')
    output.setparams((num_channels, sample_width, SAMPLE_RATE, 0, 'NONE', 'not compressed'))
    output.writeframes(original)
    output.close()


if __name__ == "__main__":
	if len(sys.argv) <= 1:
		print "Must supply WAV path"
		exit(-1)

	wavfile_path = sys.argv[1]
	data = preprocess(wavfile_path)
	save_output(data, wavfile_path, 'test')
