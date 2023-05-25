import streamlit as st
import numpy as np
import joblib

def run_app_ml():
    st.subheader('자동차 금액 예측')

    # 성별, 나이, 연봉, 카드빛, 자산을 유저한테 입력받는다.
    gender = st.radio('성별 선택',['남자','여자'])
    if gender == '남자' :
        gender = 0
    else:
        gender = 1
    age = st.number_input('나이 입력',18,100)
    salary = st.number_input('연봉 입력', 5000, 1000000)
    debt = st.number_input('카드빛 입력',0,1000000)
    worth = st.number_input('자산 입력',1000,10000000)
    # 왜 이항목만 입력받냐 인공지능 만들때 이항목으로 만들었으니까
    # 입력받은 후 버튼을 누르면 예측한 금액을 표시한다.
    if st.button('금액 예측') :
        new_data = np.array([gender, age, salary, debt, worth])
        new_data = new_data.reshape(1,5)
        regressor = joblib.load('model/regressor.pkl')
        y_pred = regressor.predict(new_data)
        print(y_pred)
        # my_car = int(y_pred)
        my_car = int(y_pred[0])
        print(my_car)
        st.text(str(my_car)+'달러짜리 차를 사실 수 있습니다.')
        # print('f'{price}달러짜리!')
        # print('{}달러짜리 ~'.format(price))
