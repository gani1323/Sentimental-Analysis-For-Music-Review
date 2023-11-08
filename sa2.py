#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pickle
import streamlit as st

model=pickle.load(open('sentiment_analysis_model.p','rb'))

st.title(' Sentiment Analysis Model ')

st.write('Enter text for sentiment analysis:')
message = st.text_area("","Type Here ...")
if st.button('PREDICT'):
    if message.strip():
        disp=" "
        a = model.predict([message])[0]
        if(a == 'pos'):
            disp = "Positive Sentiment!"
        elif(a == 'neg'):
            disp = "Negative Sentiment!"
    else:
        st.write('Please enter text before clicking "PREDICT"')
    
st.write('The sentiment of given text is:', disp)
    
