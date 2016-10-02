"""
preprocess.py
    download and process wav files
"""

import numpy as np
from pydub import AudioSegment

def process_wav(wavfile_path):
    audio = AudioSegment.from_wav(wavfile_path).set_channels(1)
    raw_data = audio.get_array_of_samples()
    if audio.frame_width > 1:
        raw_data = map(ulaw, raw_data)


def ulaw(x):
    u = 255 # converts into 8 bits
    return np.sign(x) * (np.log(1 + u * np.abs(x)) / np.log(1 + u))
