

from numpy.core.records import array
import streamlit as st
from pickle import load
import numpy as np
import sys
import sklearn


def app():

    # Load Saved Results Data
    pickled_model = load(open('models/07-11-2022-07-33-52-3.07%.pkl', 'rb'))
    #model = load(filename='models/07-11-2022-07-33-52-3.07%.pkl')

    st.title("KPI Model")

    st.header("To calculate KPI, enter values below.")

    st.header("")
    no_of_unique_objects = st.number_input('unique objects', key='a')
    eng_width = st.number_input('width of engagement button', key='b')
    eng_height = st.number_input('height of engagement button', key='c')
    #total_retransmission = st.number_input('Enter tcp retransmission', key='d')
    #average_delay = st.number_input('Enter average delay', key='e')
    #total_throughput = st.number_input('Enter average throughput', key='f')
    eng_height1 = 0.2
    eng_height2 = 0.3
    eng_height3 = 0.5
    eng_height4 = 0.4
    eng_height5 = 5
    eng_height6 = 9
    eng_height7 = 0.8
    eng_height8 = 0.1
    eng_height9 = 0.2
    eng_height10 = 0.4444444444444444444
    eng_height11 = 0.009
    eng_height12 = 0.4
    eng_height13 = 8.2

    if st.button('KPI prediction'):
        array = [no_of_unique_objects, eng_width, eng_height,eng_height1,eng_height2,eng_height3,eng_height4,eng_height5,
        eng_height6,eng_height7,eng_height8,eng_height9,eng_height10,eng_height11,eng_height12,eng_height13]
        val = pickled_model.predict([array])
        KPI = [i[0] for i in val][0]
        st.write(
            "The estimated KPI is: {:.3f}".format(KPI))