import pandas as pd


class DataLoader:
    def __init__(self, pathname):
        self.path = pathname
    
    def load_data(self):
        data = pd.read_csv(self.path)
        return data