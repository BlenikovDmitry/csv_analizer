import streamlit as st
import statistics
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io


#функция отрисовки гистограммы и код для отправки графика на скачивание пользователю
#Аргументы:
#data - отрисовываемые данные
#name - название гистограммы
#color - цвет гистограммы
def single_field_hist(data, name, color):
    fig, ax = plt.subplots(figsize=(10, 10))
    
    ax.set_title(name)
    ax.set_xlabel("Виды значений")
    ax.set_ylabel("Число значений")



    ax.hist(data, bins=30, linewidth=2, color=color, edgecolor="black", rwidth=0.9)
    ax.grid(True)

    st.pyplot(fig)

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    st.download_button(
        label="Скачать график как PNG",
        data=buf,
        file_name=name+ ".png",
        mime="image/png"
    )



st.header("Статистический анализ датасета")

uploaded_file = st.file_uploader("Выберите CSV файл", type="csv")
#через выбор приколачиваем кодировку
#позволит перебором анализировать разные файлы с разными кодировками
user_enc = st.radio("Кодировка:", ["utf-8", "cp1251"], horizontal=True)
#если удалось прочитать файл, то есть он не битый, едем дальше
if uploaded_file is not None:
    #пробуем прочитать файл в выбранной пользователем кодировке
    #если получается - едем дальше
    #если нет - выдаем исключение UnicodeDecodeError и позволяем пользователю изменить выбор
    try:
        df =  pd.read_csv(uploaded_file, sep=None, engine='python', encoding=user_enc)
        st.dataframe(df)
        #выбор столбца и рассчитываемой статистики
        st.header("Расчет базовых статистик")
        select_column = st.selectbox('Выберите столбец:',(df.columns))
        select_statistic = st.selectbox('Выберите статистику:',('среднее значение', 'медиана', 'среднеквадратичное отклонение'))
        df_tmp = df.astype(str)
        #при нажатии на кнопку "Рассчитать" все данные заранее приведены к строке
        #пробуем перевести в числовые данные
        #если получается - значит считаем статистики и строим распределение
        #если нет - выдаем ошибку и даем пользователю поменять поле
        if st.button("Рассчитать"):
            if select_statistic == 'среднее значение':
                    df_tmp[select_column] = pd.to_numeric(df_tmp[select_column].str.replace(',', '.'), errors = 'coerce')
                    result = round(df_tmp[select_column].mean(),2)
                    if np.isnan(result) == False:
                        st.write(f'Среднее значение: {round(df_tmp[select_column].mean(),2)}')
                        single_field_hist(df_tmp[select_column], 'Распределение столбца ' + select_column, 'blue')
                    else:
                        st.write('Выбран не числовой столбец')
            if select_statistic == 'медиана':
                    df_tmp[select_column] = pd.to_numeric(df_tmp[select_column].str.replace(',', '.'), errors = 'coerce')
                    result = round(df_tmp[select_column].mean(),2)
                    if np.isnan(result) == False:
                        st.write(f'Медиана: {round(df_tmp[select_column].median(),2)}')
                        single_field_hist(df_tmp[select_column], 'Распределение столбца ' + select_column, 'blue')
                    else:
                        st.write('Выбран не числовой столбец')
            if select_statistic == 'среднеквадратичное отклонение':
                    df_tmp[select_column] = pd.to_numeric(df_tmp[select_column].str.replace(',', '.'), errors = 'coerce')
                    result = round(df_tmp[select_column].mean(),2)
                    if np.isnan(result) == False:
                        st.write(f'Среднеквадратичное отклонение: {round(df_tmp[select_column].std(),2)}')
                        single_field_hist(df_tmp[select_column], 'Распределение столбца ' + select_column, 'blue')
                    else:
                        st.write('Выбран не числовой столбец')
    

            
                
        st.header("Графики для пар столбцов")
        selected_columns = st.multiselect('Выберите колонки для графика:', df.columns.tolist())
        select_graphics = st.selectbox('Выберите график:',('Линейный', 'Диаграмма рассеяния'))

        if st.button("Построить график"):

        #здесь отрисовываем графики после активируем кнопку экспорта
        #то есть тянем методы из класса graphics
            st.button("Экспортировать график")

    except UnicodeDecodeError:
        st.write('Некорректная кодировка')




        

    


   

