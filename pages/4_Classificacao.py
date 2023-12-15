import pandas as pd
import plotly.express as px
import streamlit as st
import pickle
import numpy as np

import os
from utils.build import build_header
from sklearn.naive_bayes import GaussianNB
