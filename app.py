import streamlit as st
import statistics
import datetime
import pandas as pd
import numpy as np

    

st.header("Статистический анализ датасета")

uploaded_file = st.file_uploader("Выберите CSV файл", type="csv")
#через выбор приколачиваем кодировку
#позволит перебором анализировать разные файлы с разными кодировками
user_enc = st.radio("Кодировка:", ["utf-8", "cp1251"], horizontal=True)

if uploaded_file is not None:
    # Чтение данных по умолчанию указал utf-8 а вообще нужно учесть самые популярные, судя по всему
    # и разделитель
    try:
        df =  pd.read_csv(uploaded_file, sep=None, engine='python', encoding=user_enc)
        st.dataframe(df)
        #выбор столбца и рассчитываемой статистики
        select_column = st.selectbox('Выберите столбец:',(df.columns))
        select_statistic = st.selectbox('Выберите статистику:',('среднее значение', 'медиана', 'среднеквадратичное отклонение'))
        df_tmp = df.astype(str)
        
        if st.button("Рассчитать"):
            if select_statistic == 'среднее значение':
                    df_tmp[select_column] = pd.to_numeric(df_tmp[select_column].str.replace(',', '.'), errors = 'coerce')
                    result = round(df_tmp[select_column].mean(),2)
                    if np.isnan(result) == False:
                        st.write(f'Среднее значение: {round(df_tmp[select_column].mean(),2)}')
                    else:
                        st.write('Выбран не числовой столбец')
            if select_statistic == 'медиана':
                    df_tmp[select_column] = pd.to_numeric(df_tmp[select_column].str.replace(',', '.'), errors = 'coerce')
                    result = round(df_tmp[select_column].mean(),2)
                    if np.isnan(result) == False:
                        st.write(f'Медиана: {round(df_tmp[select_column].median(),2)}')
                    else:
                        st.write('Выбран не числовой столбец')
            if select_statistic == 'среднеквадратичное отклонение':
                    df_tmp[select_column] = pd.to_numeric(df_tmp[select_column].str.replace(',', '.'), errors = 'coerce')
                    result = round(df_tmp[select_column].mean(),2)
                    if np.isnan(result) == False:
                        st.write(f'Среднеквадратичное отклонение: {round(df_tmp[select_column].std(),2)}')
                    else:
                        st.write('Выбран не числовой столбец')
    

            
                

            #сюда тянем методы из класса analyze

        selected_columns = st.multiselect('Выберите колонки для графика:', df.columns.tolist())
        select_graphics = st.selectbox('Выберите график:',('Линейный', 'Диаграмма рассеяния'))

        if st.button("Построить график"):

        #здесь отрисовываем графики после активируем кнопку экспорта
        #то есть тянем методы из класса graphics
            st.button("Экспортировать график")

    except UnicodeDecodeError:
        st.write('Некорректная кодировка')




        

    


   

