import streamlit as st
import pickle
import time

import nltk
nltk.download('stopwords')

# load the model
model = pickle.load(open('sentiment_model.pkl', 'rb'))

st.title('Sentiment Analysis :) ')

tweet = st.text_input('Enter your Comments or Tweet')

submit = st.button('Predict')

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction time taken: ', round(end-start, 2), 'seconds')
    
    #print(prediction[0])
    # st.write(prediction[0])
    if prediction[0] == 'Positive':
        st.success('Positive Comment  :) ')
    elif prediction[0] == 'Negative':
        st.warning('Negative Comment    :( ')
    elif prediction[0] == 'Neutral':
        st.info('Neutral Comment  :| ')

