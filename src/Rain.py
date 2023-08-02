import pandas as pd
from datetime import datetime
import pickle
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go



class Rain():
    Classifier = pickle.load(open('./model/Rain_Clas.pkl', 'rb'))
    Regressor = pickle.load(open('./model/Rain_Reg.pkl', 'rb'))
    def __init__(self, x):
        self.x = x.copy()
        
    def transform(self):
        self.x['data'] = pd.to_datetime(self.x['Datetime – utc'], format='mixed')
        self.x['data'] = self.x.data.astype(str).str.split('+',expand=True)[0]
        self.x['dif_charge'] = self.x.groupby('num_of_resets').piezo_charge.diff(-1).shift(-2)
   
        self.x.dropna(inplace=True)
 
        self.x['dif_temp'] = self.x['air_temperature_100'] - self.x['piezo_temperature'].astype(float)
        self.x['dq/dT'] = (self.x.dif_charge/self.x.dif_temp)

    def calculate(self, shft=True):
        self.x['precp'] = self.Classifier.predict(self.x[self.Classifier.feature_names_in_])
        if shft == True:
            self.x['precp'] = self.x['precp'].shift(-1)
        self.x.loc[self.x['precp'].eq(1),'chuva'] = self.Regressor.predict(self.x.loc[self.x['precp'].eq(1), self.Regressor.feature_names_in_])
        self.x.chuva.fillna(0,inplace=True) 
        self.x.dropna(inplace=True)

    def plot(self):
        
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Rain - No-Rain", "Quantity of rain [mm]"))
    
        fig.add_trace(go.Scatter(x=self.x.data, y=self.x.precp, mode="markers"),row=1, col=1)
        fig.add_trace(go.Scatter(x=self.x.data, y=self.x.chuva),row=1, col=2)

        return fig


def plot_null(data):
    """Grafico de calor dos dados fornecidos"""
    fig =  px.imshow(data.isnull(), text_auto=True)
    #fig.show()
    return fig

