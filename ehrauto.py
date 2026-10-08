import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


def standardizenames(df, col):
    df[col]=df[col].str.replace('[^a-zA-Z]', ' ', regex=True)
    df[col]=df[col].str.strip()
    return df


