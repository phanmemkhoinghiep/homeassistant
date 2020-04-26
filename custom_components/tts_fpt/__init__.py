# encoding: utf-8


# Declare variables
DOMAIN = 'tts_fpt'
SERVICE_FPT_TTS = 'say'
# config
CONF_API_KEY = 'api_key'
CONF_SPEED = 'speed'
CONF_URL_HASS = 'url'
# data service
CONF_PLAYER_ID = 'entity_id'
CONF_MESSAGE = 'message'
CONF_VOICE_TYPE = 'voice_type'

# audio file
CONF_FILE_PATH = '/config/www/tts'
CON_AUDIO_PATH = '/local/tts'

import requests, json, os, time

def setup(hass, config):

    def tts_handler(data_call):
        # Get config
        openfpt_api = str(config[DOMAIN][CONF_API_KEY])
        speed_read = str(config[DOMAIN][CONF_SPEED])
        url_hass = str(config[DOMAIN][CONF_URL_HASS])
        
        # Get data service
        media_id = data_call.data.get(CONF_PLAYER_ID)
        text_message = str(data_call.data.get(CONF_MESSAGE)[0:2000])
        voice_type = data_call.data.get(CONF_VOICE_TYPE)
		
        # List voice of FPT Speech Synthesis
        voice_list = {'nam_mien_bac': 'leminh', 'nu_mien_bac': 'banmai', 'nu_mien_trung': 'myan', 'nu_mien_nam': 'lannhi'}
        voice_type = voice_list.get(voice_type)	
        # HTTP Request
        url = 'https://api.fpt.ai/hmi/tts/v5'
        # Header Parameters
        header_parameters = {'api_key': openfpt_api, 'speed': speed_read, 'prosody': '1', 'voice': voice_type}
        # Body Parameters
	text_message = text_message.encode('utf-8')
        # Get response from Server	
        response = requests.post(url, data = text_message, headers = header_parameters).json()['async']
        # Create unique audio file name
        uniq_filename = 'tts_fpt' + str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'
        # Open audio file
        audio_file = open(CONF_FILE_PATH + uniq_filename, 'wb')
        # Write audio content to file
        audio_file.write(response)
        audio_file.close()
	# Play audio file with Home Assistant Service#	
        url_file = url_hass + CON_AUDIO_PATH + uniq_filename
        # service data for 'CALL SERVICE' in Home Assistant
        service_data = {'entity_id': media_id, 'media_content_id': url_file, 'media_content_type': 'audio/mp3'}
        # Call service from Home Assistant
        hass.services.call('media_player', 'play_media', service_data)
        
    hass.services.register(DOMAIN, SERVICE_FPT_TTS, tts_handler)
    return True

