import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

b_notch, a_notch = signal.iircomb(60, 35, 10, ftype='notch', fs=600)
b_peak, a_peak = signal.iircomb(60, 35, 10, ftype='peak', fs=600)
w_notch, h_notch = signal.freqz(b_notch, a_notch, fs=600)
w_peak, h_peak = signal.freqz(b_peak, a_peak, fs=600)

h_combined = h_notch + h_peak
plt.plot(w_notch, 20 * np.log10(abs(h_combined)))
plt.show()
