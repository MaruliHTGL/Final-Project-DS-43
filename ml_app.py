import streamlit as st
import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# import ml package
import joblib
import os   

lemmatizer = WordNetLemmatizer()

# Defining a function to clean up the text
def clean(Text):
    sms = re.sub('[^a-zA-Z]', ' ', Text) #Replacing all non-alphabetic characters with a space
    sms = sms.lower() #converting to lowecase 
    sms = word_tokenize(sms)
    sms = [lemmatizer.lemmatize(word, pos ='v') for word in sms if not word in stopwords.words("english")]
    sms = ' '.join(sms)
    return sms
        
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), 'rb'))
    return loaded_model

def load_vectorization(vectorization_file):
    loaded_vectorization = joblib.load(open(os.path.join(vectorization_file), 'rb'))
    return loaded_vectorization

def run_ml_app():
    st.markdown("<h2 style = 'text-align: center;'> Input Your News </h2>", unsafe_allow_html=True)
    title = st.text_input('Enter the news title:', 'The news title')
    text = st.text_area('Enter the news content:', 'The news content')

    with st.expander("Your Selected Options"):
        result = {
            'Title': title,
            'Text':text,
        }

    # dataframe
    df_cp = pd.DataFrame({'title': [title], 'text': [text]})

    # combine title and text column
    df_cp['news'] = df_cp['title'] + ' ' + df_cp['text']

    # clean text
    df_cp["clean_news"] = df_cp["news"].apply(clean)

    st.markdown("<h2 style = 'text-align: center;'> Your News </h2>", unsafe_allow_html=True)

    vectorization = load_vectorization("vectorization (7).pkl")
    vectorization_array = vectorization.transform(df_cp["clean_news"])

    st.subheader(title)
    st.write(text)

    # prediction section
    st.markdown("<h2 style = 'text-align: center;'> Prediction Result </h2>", unsafe_allow_html=True)

    model = load_model("model_lr (4).pkl")  
    prediction = model.predict(vectorization_array)
    pred_proba = model.predict_proba(vectorization_array)

    pred_probability_score = {'FAKE':round(pred_proba[0][0]*100,4),
                              'REAL':round(pred_proba[0][1]*100,4)}
    
    if prediction == 'FAKE':
        st.warning("Beware this news is fake")
        st.write(pred_probability_score)
    else:
        st.success('This news is real')
        st.write(pred_probability_score)