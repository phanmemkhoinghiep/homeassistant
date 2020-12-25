# encoding: utf-8


# Declare variables
DOMAIN = 'tts_zalo'
SERVICE_ZALO_TTS = 'say'
# config
CONF_API_KEY = 'api_key'
CONF_SPEED = 'speed'
# data service
CONF_PLAYER_ID = 'entity_id'
CONF_MESSAGE = 'message'
CONF_VOICE_ID = 'voice_id'

# audio file path

CONF_FILE_PATH = '/config/www/tts/'
CON_AUDIO_PATH = '/local/tts/'


import requests, json, os, time, uuid, urllib, datetime

def setup(hass, config):

    def tts_handler(data_call):
        # Get config
        zalo_api = str(config[DOMAIN][CONF_API_KEY])                
        url_hass = str(config[DOMAIN][CONF_URL_HASS])        
        # Get data service
        media_id = data_call.data.get(CONF_PLAYER_ID)
        text_message = str(data_call.data.get(CONF_MESSAGE)[0:2000])
        voice_id = data_call.data.get(CONF_VOICE_ID)
        speed = data_call.data.get(CONF_SPEED)
        # List voice of Zalo Speech Synthesis
        voice_id_list = {'nu_mien_bac_01': 2, 'nam_mien_bac_01': 4, 'nu_mien_nam_01': 1,'nam_mien_nam_02': 3}
        sepaker_id= voice_id_list.get(voice_id)
        encode_type= 1
        # HTTP Request
        url = 'https://api.zalo.ai/v1/tts/synthesize'
        # Header Parameters
        header_parameters = {'apikey': zalo_api}
        # Body Parameters
        data = {'input': text_message.encode('utf-8'), 'speed': speed_read, 'encoder_type': encode_type,'speaker_id': speaker_id}
        # Get response from Server
        url_file = requests.post(url, data = text_message, headers = header_parameters).json()['async']
        # "The content will be returned after a few seconds under the async link, wait some seconds"
        #time.sleep(2)
        # service data for 'CALL SERVICE' in Home Assistant
        service_data = {'entity_id': media_id, 'media_content_id': url_file, 'media_content_type': 'audio/mp3'}
        # Call service from Home Assistant
        hass.services.call('media_extractor', 'play_media', service_data)
        
    hass.services.register(DOMAIN, SERVICE_ZALO_TTS, tts_handler)
    return True
