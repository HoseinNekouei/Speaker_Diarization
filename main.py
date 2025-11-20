import torch
import os
from dotenv import dotenv_values


#=========================CONFIGURATION==============================
# 1. Audio and Authentication

config= dotenv_values('.env') # Load authentication data
audio_file= r'/src/272211604_50.mp3' # Load audio file
hf_token= config['HF_TOKEN']

# 2.Hardware and Performance
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# 3. Accuracy and Batching
whisper_model_name=...
batch_size= 16

#4. Speakers limits
MIN_SPEAKERS= None
MAX_SPEAKERS= None

print('Starting Whisper and Speaker Diarization ')
print(f'Processing {os.path.basename(audio_file)}')
print(f'Device: {device} | Model: {whisper_model_name}')


#=========================LOAD AUDIO AND TRASCRIBE (WHISPER)=========
