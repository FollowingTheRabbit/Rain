
import streamlit as st
from PIL import Image

import pandas as pd
import io
import os
import xlsxwriter
from datetime import datetime
import pickle
from Rain import *




def main():
    
    #image_path = './img/data_input.png'
    #st.write('Escolha um arquivo semelhante \
    #    ao mostrado na imagem, para ser analizado.')
    #image_formato_arquivo = Image.open(image_path)
    #st.image(image_formato_arquivo)


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

    writer = pd.ExcelWriter(escreve, engine='xlsxwriter')   
    data.to_excel(writer, index=False, header=True, sheet_name='Sensor Measurement Interpreted')
    writer.close()
    dado_processado = escreve
    return  dado_processado


if __name__ == "__main__":
    main()


