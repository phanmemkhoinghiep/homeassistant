# encoding: utf-8


# Declare variables
DOMAIN = 'tts_viettel'
SERVICE_VIETTEL_TTS = 'say'
# config
CONF_TOKEN = 'token'
CONF_SPEED = 'speed'
CONF_URL_HASS = 'url'
# data service
CONF_PLAYER_ID = 'entity_id'
CONF_MESSAGE = 'message'
CONF_VOICE_TYPE = 'voice_type'

# audio file path

CONF_FILE_PATH = '/config/www/tts/'
CON_AUDIO_PATH = '/local/tts/'

import requests, json, os, time, uuid, urllib, datetime

def setup(hass, config):

    def tts_handler(data_call):
        # Get config
        viettel_token = str(config[DOMAIN][CONF_TOKEN])
        # speed_read = str(config[DOMAIN][CONF_SPEED])
        url_hass = str(config[DOMAIN][CONF_URL_HASS])
        
        # Get data service
        media_id = data_call.data.get(CONF_PLAYER_ID)
        text_message = str(data_call.data.get(CONF_MESSAGE)[0:2000])
        voice_type = data_call.data.get(CONF_VOICE_TYPE)
        speed_read = data_call.data.get(CONF_SPEED)
        # List voice of Viettel Speech Synthesis
        voice_list = {'nu_mien_bac_1': 'hn-quynhanh', 'nu_mien_bac_2': 'trinhthiviettrinh', 'nam_mien_bac_1': 'hn-thanhtung', 'nam_mien_bac_2': 'phamtienquan', 'nu_mien_trung_1': 'hue-maingoc', 'nam_mien_trung_1': 'hue-baoquoc', 'nu_mien_nam_1': 'hcm-diemmy', 'nu_mien_nam_2': 'lethiyen', 'nu_mien_nam_3': 'nguyenthithuyduyen', 'nam_mien_nam_1': 'hcm-minhquan'}
        voice_type = voice_list.get(voice_type)
        # HTTP Request
        url = 'https://viettelgroup.ai/voice/api/tts/v1/rest/syn'
        # Header Parameters
        headers = {'Content-type': 'application/json', 'token': viettel_token}
        # Body Parameters
        data = {'text': text_message, "voice": voice_type, "id": "2", "without_filter": False, "speed": speed_read, "tts_return_option": 3}
        # Get response from Server
        response = requests.post(url, data = json.dumps(data), headers = headers)
        # Create unique audio file name
        uniq_filename = 'tts_viettel_' + str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'
        # Open audio file     
        audio_file = open(CONF_FILE_PATH + uniq_filename, 'wb')
        # Write audio content to file
        audio_file.write(response.content)
        audio_file.close()
        # Play audio file with Home Assistant Service#
        url_file = url_hass + CON_AUDIO_PATH + uniq_filename
        # service data for 'CALL SERVICE' in Home Assistant
        service_data = {'entity_id': media_id, 'media_content_id': url_file, 'media_content_type': 'audio/mp3'}
        # Call service from Home Assistant
        hass.services.call('media_player', 'play_media', service_data)
        
    hass.services.register(DOMAIN, SERVICE_VIETTEL_TTS, tts_handler)
    return True
