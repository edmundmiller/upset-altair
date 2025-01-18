import json
import re
import altair as alt
import pandas as pd
from pathlib import Path
from altair_upset import UpSetAltair
from altair_saver import save

def load_test_data():
    """Load the COVID symptoms data"""
    data = pd.read_csv("https://ndownloader.figshare.com/files/22339791")
    return data