import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from get_data import Planet
class Spectrum:

    def __init__(self, pname):
        self.planet = Planet(pname)

    def plot_spectrum(self):
        """
        Function to plot transmissions spectrum
        """
        wav, bw = self.planet.wavelength()
        td, tde = self.planet.transit_depth()
        fig, ax = plt.subplots()

        lines={'linestyle': 'None'}
        plt.rc('lines', **lines)
        plt.plot(wav, td, 'g-', markersize=3)
        plt.plot(wav, td, 'ro', markersize=3)
        plt.errorbar(wav, td, xerr=bw, yerr=tde, ecolor='red')
        
        plt.xlim(min(wav),max(wav))
        ax.set_xlabel('Wavelength (microns)')
        ax.set_ylabel('Transit Depth (percentage)')
        ax.set_title(f'Transmission Spectrum for {self.planet.pname}')
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.linspace(start, end, 4))
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
    
        plt.savefig(f'{self.planet.pname}.png')

Spectrum('WASP-43 b').plot_spectrum()