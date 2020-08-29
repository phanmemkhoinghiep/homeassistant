# encoding: utf-8


# Declare variables
DOMAIN = 'tts_fpt'
SERVICE_FPT_TTS = 'say'
# config
CONF_API_KEY = 'api_key'
CONF_SPEED = 'speed'
# data service
CONF_PLAYER_ID = 'entity_id'
CONF_MESSAGE = 'message'
CONF_VOICE_TYPE = 'voice_type'

import requests, json, os, time, uuid, urllib, datetime

def setup(hass, config):

    def tts_handler(data_call):
        # Get config
        openfpt_api = str(config[DOMAIN][CONF_API_KEY])        
        url_hass = str(config[DOMAIN][CONF_URL_HASS])        
        # Get data service
        media_id = data_call.data.get(CONF_PLAYER_ID)
        text_message = str(data_call.data.get(CONF_MESSAGE)[0:2000])
        voice_type = data_call.data.get(CONF_VOICE_TYPE)
        speed_read = data_call.data.get(CONF_SPEED)
        # List voice of FPT Speech Synthesis
        voice_list = {'nam_mien_bac_01': 'leminh', 'nu_mien_bac_01': 'banmai','nu_mien_bac_02': 'thuminh', 'nam_mien_trung_01': 'gia_huy','nu_mien_trung_01': 'myan', 'nu_mien_nam_01': 'lannhi','nu_mien_nam_02': 'linhsan'}
        voice_type = voice_list.get(voice_type)
        # HTTP Request
        url = 'https://api.fpt.ai/hmi/tts/v5'
        # Header Parameters
        header_parameters = {'api_key': openfpt_api, 'speed': speed_read, 'prosody': '1', 'voice': voice_type}
        # Body Parameters
        text_message = text_message.encode('utf-8')
        # Get response from Server
        url_file = requests.post(url, data = text_message, headers = header_parameters).json()['async']
        # "The content will be returned after a few seconds under the async link, wait some seconds"
        time.sleep(2)
        # service data for 'CALL SERVICE' in Home Assistant
        service_data = {'entity_id': media_id, 'media_content_id': url_file, 'media_content_type': 'audio/mp3'}
        # Call service from Home Assistant
        hass.services.call('media_extractor', 'play_media', service_data)
        
    hass.services.register(DOMAIN, SERVICE_FPT_TTS, tts_handler)
    return True
