import streamlit as st
import requests
from tensorflow.io import read_file
from tensorflow.audio import decode_wav
import wave
import numpy as np
import matplotlib.pyplot as plt





with st.container():
    st.markdown("<h1 style='text-align: center; color: black;'>Who\'s this ?</h1>", unsafe_allow_html=True)

with st.container():
    st.empty()

with st.container():
    st.empty()
with st.container():
    st.empty()
with st.container():
    st.empty()

audio = st.file_uploader('**Please upload an audio file** (.wav) :notes:',type=['wav'],
                accept_multiple_files=False,)
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
    plt.title('signal_array',fontsize=15)
    plt.ylabel('Signal Value',fontsize=15)
    plt.xlabel('Time (s)',fontsize=15)
    plt.xlim(0,t_audio)
    plt.show()
    st.pyplot(figure_sound_wave)

    figure_sound_spectrogram = plt.figure(figsize=(15, 5))
    plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
    plt.title('signal_array',fontsize=15)
    plt.ylabel('Frequency (Hz)',fontsize=15)
    plt.xlabel('Time (s)',fontsize=15)
    plt.xlim(0,t_audio)
    plt.colorbar()
    plt.show()
    st.pyplot(figure_sound_spectrogram)


# def plot_wave(audio):
#     # coded_wav = read_file(audio)
#     # plot_sound = decode_wav(coded_wav)
#     # st.pyplot(plot_sound)
#     st.pyplot.figure(figsize=(15, 5))
#     st.pyplot(df_train_preproc_out['times'][0],df_train_preproc_out['signal_array'][0])
#     st.pyplot.title('signal_array')
#     st.pyplot.ylabel('Signal Value')
#     plt.xlabel('Time (s)')
#     plt.xlim(0, df_train_preproc_out['t_audio'][0])
#     st.pyplot.show()


# st.button('Display wave sound',on_click=plot_wave)


with st.form(key='params_for_api'):

    day_of_week = st.number_input('day_of_week')
    time = st.number_input('time')

    st.form_submit_button('Make prediction')

params = {
    'day_of_week':day_of_week,
    'time':time}

speaker_recogn_url = 'https://speaker-recognition-docker-image-ebbxnjt4eq-ew.a.run.app/predict'
response = requests.get(speaker_recogn_url, params=params).json()


# st.markdown(type(response))

# pred = response['wait']
st.markdown(response)


# Speakes = ['rxr', 'ljm', 'jmk', 'rms', 'gka', 'ksp', 'awb', 'clb', 'fem',
#        'bdl', 'lnh', 'ahw', 'slp', 'slt', 'eey', 'aew', 'axb', 'aup'],
