import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("D:\Data Science_Personal_Projects\Internship Projects\Main Project/prosperLoanData.csv")
# pr = df.profile_report()

# st_profile_report(pr)

from pandas_profiling import ProfileReport
profile = ProfileReport(df)
profile