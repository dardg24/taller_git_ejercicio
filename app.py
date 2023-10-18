import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Cargamos los datos
'''
train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')