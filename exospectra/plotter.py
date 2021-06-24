import pandas as pd
import seaborn as sns
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
        td, tdp, tdm = self.planet.transit_depth()
        fac = self.planet.facility()
        inst = self.planet.instrument()

        d = {'wav': wav, 'bw': bw, 'td': td, 'tdp': tdp,
            'tdm': tdm, 'fac':fac, 'inst':inst}
        df = pd.DataFrame(data=d)
        fig, ax = plt.subplots()
        # ax = sns.pointplot(x='wav', y='td',
        #            data=df, markers='.')
        plt.plot(wav, td)
        ax.set_xlim([0,4])
        ax.set_xlabel('Wavelength (microns)')
        ax.set_ylabel('Transit Depth (percentage)')
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.linspace(0, end, 10))
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
        print(max(wav))
        plt.savefig(f'{self.planet.pname}.png')

Spectrum('HD 189733 b').plot_spectrum()