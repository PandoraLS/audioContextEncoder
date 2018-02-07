import pandas as pd
import numpy as np

__author__ = 'Andres'


class EvaluationWriter(object):
    def __init__(self, excelFileName):
        self._writer = pd.ExcelWriter(excelFileName)
        self._index = 0

    def evaluate(self, reconstructed, original_gaps, step):
        fake_a = (reconstructed - 0.5) * 2
        gap = (original_gaps - 0.5) * 2

        SNRs = np.zeros((len(fake_a),))
        for index, signal in enumerate(fake_a):
            SNRs[index] = self._pavlovs_SNR(gap[index], fake_a[index])

        norm_orig = self._euclideanNorm(gap)
        error = gap - fake_a
        reconstruction_loss = 0.5 * np.sum(np.square(error), axis=1) * (1 + 1 / norm_orig)

        df = pd.DataFrame({'SNRs ' + str(step): SNRs, 'reconstruction_loss ' + str(step): reconstruction_loss})
        df.describe().to_excel(self._writer, sheet_name='general', startcol=self._index, index=not self._index)
        self._index += 3

    def _pavlovs_SNR(self, y_orig, y_inp):
        norm_y_orig = np.linalg.norm(y_orig) + 1e-10
        norm_y_orig_minus_y_inp = np.linalg.norm(y_orig - y_inp)
        return 10 * np.log10((abs(norm_y_orig ** 2)) / abs((norm_y_orig_minus_y_inp ** 2)))

    def _euclideanNorm(self, vector):
        squared = np.square(vector)
        summed = np.sum(squared, axis=1)
        return np.sqrt(summed + 1e-10)

    def save(self):
        self._writer.save()