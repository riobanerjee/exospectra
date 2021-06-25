import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pylab as pl
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
        wav = np.array(wav)
        td = np.array(td)
        tdp = np.array(tdp)
        tdm = np.array(abs(tdm))
       

        wav1 =[]
        td1 =[]
        tdp1 =[]
        tdm1 =[]
        yerr = []
        for i in range(len(wav)):
            if wav[i] != wav[i-1]:
                wav1.append(wav[i])
                td1.append(td[i])
                tdp1.append(tdp[i])
                tdm1.append(tdm[i])
                yerr.append((tdm[i], tdp[i]))
                
            else:
                continue
        
        yerr1 = np.array(yerr).T
                
          
        fig, ax = plt.subplots()

        lines={'linestyle': 'None'}
        plt.rc('lines', **lines)
        pl.plot(wav1, td1, 'go', markersize=6)
        el = pl.errorbar(wav1, td1, yerr=yerr1, fmt='b', ecolor='red')
        
        plt.xlim(0,5)
        ax.set_ylim([2.38,2.5])
        ax.set_xlabel('Wavelength (microns)')
        ax.set_ylabel('Transit Depth (percentage)')
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.linspace(0, end, 4))
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
    
        plt.savefig(f'{self.planet.pname}.png')

Spectrum('HD 189733 b').plot_spectrum()