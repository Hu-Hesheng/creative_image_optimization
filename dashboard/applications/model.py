

from numpy.core.records import array
import streamlit as st
from pickle import load
import numpy as np
import sys


def app():

    # Load Saved Results Data
    model = load(filename='models/07-11-2022-07-33-52-3.07%.pkl')

    st.title("KPI Model")

    st.header("To calculate KPI, enter values below.")

    session_count = st.number_input('Enter sessions', key='a')
    total_time = st.number_input('Enter total time', key='b')
    total_data = st.number_input('Enter total data', key='c')
    total_retransmission = st.number_input('Enter tcp retransmission', key='d')
    average_delay = st.number_input('Enter average delay', key='e')
    total_throughput = st.number_input('Enter average throughput', key='f')

    if st.button('KPI prediction'):
        array = [session_count, total_time, total_data,
                 total_retransmission, average_delay, total_throughput]
        val = model.predict([array])
        KPI = [i[0] for i in val][0]
        st.write(
            "The estimated KPI is: {:.3f}".format(KPI))