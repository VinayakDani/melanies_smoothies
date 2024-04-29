import streamlit as st

# Title widget
st.title('This is a title')

# Plain text widget
st.text("This is some text")

# Code widget example
code = '''def hello():
            print("Hello, Streamlit!")'''
st.code(code, language='python')

# Latex widget example
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)
''')
