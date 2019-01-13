from __future__ import print_function
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt

fs_rate, signal = wavfile.read("Piano.wav")
l_audio = len(signal.shape)
if l_audio == 2:
    signal = signal.sum(axis=1) / 2
N = signal.shape[0]
secs = N / float(fs_rate)
Ts = 1.0/fs_rate
t = scipy.arange(0, secs, Ts)
FFT = abs(scipy.fft(signal))
FFT_side = FFT[range(N//2)]
freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
fft_freqs = np.array(freqs)
freqs_side = freqs[range(N//2)]
fft_freqs_side = np.array(freqs_side)
with open('sound2','w') as f:
	for i in range(0,len(FFT_side),100):
		print(FFT_side[i], freqs_side[i], file=f)