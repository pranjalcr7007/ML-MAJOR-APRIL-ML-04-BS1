import streamlit as st
import joblib 
model=joblib.load('sentiment_analyzer_model')
st.title('Sentiment Analyzer')
ip = st.text_input("Enter the Review")
op = model.predict([ip])
if st.button('Predict'):
  st.write('RESULT:')
  st.title('Predicted Sentiment : '+op[0])
  
