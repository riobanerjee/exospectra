import pandas as pd

class Planet:

    def __init__(self, pname, datadir='data/transitspec.csv'):
        self.pname = pname
        self.datadir = datadir
        self.df = pd.read_csv('data/transitspec.csv', skiprows=26)
        self.df = self.df[self.df['instrument']=='Wide Field Camera 3']
        self.df = self.df[self.df['plntname']==pname]
        self.df = self.df.drop_duplicates(subset=['centralwavelng'])
        self.df = self.df.sort_values(by='centralwavelng')

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
        tde = self.df['plntransdeperr1']
        tde = 2*tde.fillna(200*self.df['plnratror']*self.df['plnratrorerr1'])
        
        return td, tde

