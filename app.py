import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from app_home import run_app_home
from app_eda import run_app_eda
from app_ml import run_app_ml

def main(): # 유저가 눌렀을 때 화면은 main이 처리
    st.title('자동차 가격 예측 앱')
    menu = ['Home','EDA','ML']
    choice = st.sidebar.selectbox('메뉴',menu)
    if choice == menu[0]:
        run_app_home()
    elif choice == menu[1]:
        run_app_eda()
    else:
        run_app_ml()

    # df = pd.read_csv('data/Car_Purchasing_Data.csv',encoding = 'ISO-8859-1')
    # print(df)
    # 위에 두줄은 main에 하지않고 다른파일에 한다?

if __name__ == '__main__':
    main()