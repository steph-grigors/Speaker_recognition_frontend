import streamlit as st
import requests
import wave
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import time


with st.container():
    st.markdown("<h1 style='text-align: center; color: black;'>Who dis ?</h1>", unsafe_allow_html=True)

left_co, cent_co,last_co = st.columns(3)
image = Image.open('images/who_dis_cut.png')
image_chloe = Image.open('images/Chloe.jpg')
image_parul = Image.open('images/Parul.jpg')

with left_co:
    st.image(image,width=685, caption='Andrew, Maximilian, Parul, Mike, Arya, Henry, Chloe, Laura, Samuel, Krish, Jim, Alex, Kalindi, Elena, Walter White, Jules, Pascaline, Kamilla')

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h2 style='text-align: center; color: black;'>Chloe</h2>", unsafe_allow_html=True)
    st.image(image_chloe,width=343)
    #### audio
    audio_file_chloe = open('Audios/Chloe_arctic_a0024.wav', 'rb')
    audio_bytes_chloe = audio_file_chloe.read()
    st.audio(audio_bytes_chloe, format='audio/ogg')

with col2:
    st.markdown("<h2 style='text-align: center; color: black;'>Parul</h2>", unsafe_allow_html=True)
    st.image(image_parul,width=343)
    #### audio
    audio_file_parul = open('Audios/Parul_arctic_a0017.wav', 'rb')
    audio_bytes_parul = audio_file_parul.read()
    st.audio(audio_bytes_parul, format='audio/ogg')

with st.container():
    st.empty()
with st.container():
    st.empty()

audio = st.file_uploader('**Please upload a random audio file** (.wav) :notes:',type=['wav'],
                accept_multiple_files=False)


if audio:
    st.audio(audio)

    wav_obj = wave.open(audio, 'rb')
    sample_freq = wav_obj.getframerate()
    n_samples = wav_obj.getnframes()
    t_audio = n_samples/sample_freq
    n_channels = wav_obj.getnchannels()
    signal_wave = wav_obj.readframes(n_samples)
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    times = np.linspace(0, n_samples/sample_freq, num=n_samples)

    figure_sound_wave = plt.figure(figsize=(15, 5))
    plt.plot(times,signal_array)
    plt.title('Audio Signal',fontsize=15)
    plt.ylabel('Amplitude',fontsize=15)
    plt.xlabel('Time',fontsize=15)
    plt.xlim(0,t_audio)
    plt.show()
    st.pyplot(figure_sound_wave)

    figure_sound_spectrogram = plt.figure(figsize=(15, 5))
    plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
    plt.title('MEL Spectogram',fontsize=15)
    plt.ylabel('Frequency',fontsize=15)
    plt.xlabel('Time',fontsize=15)
    plt.xlim(0,t_audio)
    plt.colorbar()
    plt.show()
    st.pyplot(figure_sound_spectrogram)

# st.button('Display wave sound',on_click=plot_wave)

with st.form(key='params_for_api'):
    audiofile = audio

if st.button("Make prediction"):

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text=progress_text)

    # speaker_recogn_url = 'http://localhost:8000/predict'
    speaker_recogn_url = 'https://whodis-ebbxnjt4eq-ew.a.run.app/predict'

    files = dict(wav=audio.getvalue())

    response = requests.post(speaker_recogn_url, files=files)
    # st.write(response)
    prediction = response.json()
    # st.write(prediction)

    prediction = prediction['name']

    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
    # st.image(image,width=685)
        st.write('**The speaker is**', prediction,':sunglasses:')
    # st.header(prediction)
