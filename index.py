import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 入門')

st.write('Display Image')

img = Image.open('cat2.jpg')

st.image(img, caption='cat', use_column_width=True)
# df = pd.DataFrame( 
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )
# df
# # st.dataframe(df.style.highlight_max(axis=0))

# # """
# # # markdown
# # """
# st.map(df) # 折れ線グラフ
