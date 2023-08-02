
import streamlit as st
import pandas as pd
import io
import os
import xlsxwriter
from datetime import datetime
import pickle
from Rain import *




def main():
    
    data = read_file()
    st.dataframe(data)
    if data.isnull().any().any():
        st.write("Dados nulos na tabela")  
        if st.button("Visualizar dados nulos"):
            fig = plot_null(data)
            st.plotly_chart(fig)



    if st.button("Process"):
        
        rain = Rain(data)
        rain.transform()
        rain.calculate()
        
        data_rain = rain.x.copy()
        st.dataframe(data_rain)
        fig = rain.plot()
        st.plotly_chart(fig)
        
    
        data_xlsx = excel_download(data_rain)
        st.download_button(label="Baixar dados processados", data=data_xlsx, file_name='Dados_Processados.xlsx')

    


def read_file():
    arquivo = st.file_uploader("Escolha um arquivo excel")
    df = pd.DataFrame()
    if arquivo is not None:
        df = pd.read_csv(arquivo)
    return df


def excel_download(data):
    escreve = io.BytesIO()

    #dia = datetime.today().strftime('%Y-%m-%d') 
    #nome_arquivo = '../data/compiled-' + str(dia) + '.xlsx'
    #writer = pd.ExcelWriter(nome_arquivo, engine = 'xlsxwriter')

    writer = pd.ExcelWriter(escreve, engine='xlsxwriter')   
    #with pd.ExcelWriter(escreve, engine='xlsxwriter') as writer
    data.to_excel(writer, index=False, header=True, sheet_name='Sensor Measurement Interpreted')
    #data.to_excel(writer, index=False, header=True, engine='xlsxwriter')
    writer.close()
    dado_processado = escreve
    return  dado_processado


if __name__ == "__main__":
    #from ..model import Rain.pkl
    main()


