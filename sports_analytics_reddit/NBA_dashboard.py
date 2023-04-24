from ast import Import
from asyncore import write
from email import header
from tkinter import font
from turtle import position, width
from urllib.request import urlopen
import streamlit as st


import numpy as np
from PIL import Image
import pandas as pd
import os



st.set_page_config(layout="wide")

st.title("NBA Dashboard of Reddit posts")



data1 = pd.read_csv(r'C:\Users\gurmo\OneDrive\Desktop\Sait 2022\Capstone Project Anooka Health\python\sports\controNBA.csv')


data2 = pd.read_csv(r"C:\Users\gurmo\OneDrive\Desktop\Sait 2022\Capstone Project Anooka Health\python\sports\hotNBA.csv")


data3 = pd.read_csv(r"C:\Users\gurmo\OneDrive\Desktop\Sait 2022\Capstone Project Anooka Health\python\sports\risingNBA.csv")


data4 = pd.read_csv(r"C:\Users\gurmo\OneDrive\Desktop\Sait 2022\Capstone Project Anooka Health\python\sports\topNBA.csv")

col10, col20 = st.columns([2,8])

col1, col2 = st.columns([6,4])

col1.title("Controversial NBA posts")
col1.table(data1)


col2.title("Hot NBA posts")
col2.table(data2)


col3, col4, col5 = st.columns([3,3,4])

col3.title("Rising NBA posts")
col3.table(data3)

col4.title("Top NBA posts")
col4.table(data4)



import streamlit as st
import plotly.graph_objects as go
