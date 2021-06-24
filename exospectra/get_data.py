import pandas as pd

class Planet:

    def __init__(self, pname, datadir='data/transitspec.csv'):
        self.pname = pname
        self.datadir = datadir
        self.df = pd.read_csv('data/transitspec.csv', skiprows=26)
        self.df = df[df['plntname']==pname]

    def wavelength(self):
        """
        Function to return the central wavelength
        and bandwidth of the wavelength bin
        """
        return self.df['centralwavelng'],self.df['bandwidth']

    def transit_depth(self):
        """
        Function to return the transit depth in percentage
        and transit depth errors
        """
        td = self.df['plntransdep']
        td = td.fillna(100*self.df['plnratror']**2)
        tde_plus = self.df['plntransdeperr1']
        tde_plus = tde_plus.fillna(200*self.df['plnratror']*self.df['plntransdeperr1'])
        tde_minus = self.df['plntransdeperr2']
        tde_minus = tde_minus.fillna(200*self.df['plnratror']*self.df['plntransdeperr2'])

        return td, tde_plus, tde_minus

    def facility(self):
        """
        Function to return the facility used for
        observations
        """
        return self.df['facility']

    def instrument(self):
        """
        Function to return the instrument used for
        observations
        """
        return self.df['instrument']