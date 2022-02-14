import numpy as np
from scipy.signal import find_peaks

class points():

    def __init__(self, data_ecg, data_icg, fs):
        self.data_ecg = data_ecg
        self.data_icg = data_icg
        self.fs = fs

    def R_peak_detection(self):
        data_pt = self.data_ecg
        peaks = find_peaks(data_pt, distance=150)[0]
        values = data_pt[np.array(peaks)]
        maksimum = np.sort(values)[-2:]
        thr = 0.8 * np.mean(maksimum)
        peaks_thr = np.where(values>thr)
        peaks_thr2 = peaks[peaks_thr]

        '''plt.plot(np.arange(len(data_pt)), data_pt)
        plt.scatter(peaks_thr2, data_pt[peaks_thr2])
        plt.axhline(thr)
        plt.show()'''

        return peaks_thr2