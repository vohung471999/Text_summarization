import streamlit as st
import requests
# from transformers import BartForConditionalGeneration, BartTokenizer
#
# tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
# model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn", forced_bos_token_id=0)

st.set_page_config(page_title='Text summarization', layout='wide', initial_sidebar_state='expanded')
st.title("Text Summarization")
text = st.text_area("Enter text:",height=None,max_chars=None,key=None,help="Enter your text here")

if st.button('Summarize text'):
    if text == "":
        st.warning('Please **enter text** for translation')
    else:
        text = {"text": text}
        # inputs = tokenizer([text], max_length=1024, return_tensors='pt')
        # summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=142, early_stopping=True)
        # summary_text = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
        response = requests.request("POST", "http://127.0.0.1:5000/predict", data=text)
        summary_text = response.json().get('summary')
        st.info(str(summary_text))
else:
    pass