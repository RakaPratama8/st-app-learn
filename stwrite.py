import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

def load_content():
    st.write("""
            This is my first Streamlit app!
            """)

    st.write('Hello, *World!* :sunglasses:')

    st.write(1234)

    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })

    st.write(df)

    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

    df2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

    c = alt.Chart(df2).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.write(c)

    st.markdown("# 1st Header")
    st.markdown("## 2nd Header")
    st.markdown("### 3rd Header")

    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')

    md = st.text_area('Type in your markdown string (without outer quotes)',
                    "")


    st.code(f"""
    import streamlit as st

    st.markdown('''{md}''')
    """)

    st.markdown(f'''{md}''')

    st.latex("(a^2 + b^2 = c^2)")
    
sidebar = st.sidebar.selectbox("Choose a page", ("Homepage", "Data Analysis"))

if sidebar == "Homepage":
    st.title("Homepage")
    st.write("Welcome to the homepage!")
else:
    st.title("Data Analysis")
    st.write("Welcome to the data analysis page!")
    load_content()