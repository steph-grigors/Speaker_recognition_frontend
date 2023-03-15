import streamlit as st
import requests
import wave
import numpy as np
import matplotlib.pyplot as plt

with st.container():
    st.markdown("<h1 style='text-align: center; color: black;'>Who dis ?</h1>", unsafe_allow_html=True)
with st.container():
    st.empty()
with st.container():
    st.empty()
with st.container():
    st.empty()
with st.container():
    st.empty()

audio = st.file_uploader('**Please upload an audio file** (.wav) :notes:',type=['wav'],
                accept_multiple_files=False)

# audio, sample_rate = librosa.load(audiofile_path, sr= None, mono = True, offset = 0.0, duration = None, res_type='soxr_hq')

if audio:
    st.audio(audio)

    # y, sample_rate = librosa.load(audio, sr= None, mono = True, offset = 0.0, duration = None, res_type='soxr_hq')
    # mel_spect = librosa.feature.melspectrogram(y=y, sr=sample_rate, n_fft=512, hop_length=128, center = True, pad_mode = 'symmetric')
    # mel_spect = librosa.power_to_db(mel_spect, ref=np.max)
    # plt.title('Mel Spectrogram');
    # plt.colorbar(format='%+2.0f dB');
    # figure_sound_wave = librosa.display.specshow(mel_spect, y_axis='mel', fmax=16000, x_axis='time');

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

# st.button('Display wave sound',on_click=plot_wave)

with st.form(key='params_for_api'):
    audiofile = audio

if st.button("Make prediction"):

    speaker_recogn_url = 'http://localhost:8000/predict'
    # speaker_recogn_url = 'https://whodis-ebbxnjt4eq-ew.a.run.app'

    files = dict(wav=audio.getvalue())

    response = requests.post(speaker_recogn_url, files=files)
    # st.write(response)
    prediction = response.json()
    # st.write(prediction)

    prediction = prediction['name']
    # st.write(prediction)
    # name = prediction[1]


    # text = f'The speaker is :{prediction}'

    # text

    st.write('The speaker is',prediction)
    # st.header(text)
