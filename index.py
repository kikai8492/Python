import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 入門')

st.write('DataFrame')

df = pd.DataFrame( 
    np.random.rand(100,2),
    columns=['lat','lon']
)
# df
# st.dataframe(df.style.highlight_max(axis=0))

# """
# # markdown
# """
st.bar_chart(df) # 折れ線グラフ
