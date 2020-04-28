# encoding: utf-8

# FPT TTS"

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

CONF_FILE_PATH = '/config/www/tts/'
CON_AUDIO_PATH = '/local/tts/'

import requests, json, os, time, uuid, urllib, datetime

def setup(hass, config):

    def tts_handler(data_call):
        # Get config
        openfpt_api = str(config[DOMAIN][CONF_API_KEY])
        # speed_read = str(config[DOMAIN][CONF_SPEED])
        url_hass = str(config[DOMAIN][CONF_URL_HASS])
        
        # Get data service
        media_id = data_call.data.get(CONF_PLAYER_ID)
        text_message = str(data_call.data.get(CONF_MESSAGE)[0:2000])
        voice_type = data_call.data.get(CONF_VOICE_TYPE)
        speed_read = data_call.data.get(CONF_SPEED)
        # List voice of FPT Speech Synthesis
        voice_list = {'nam_mien_bac': 'leminh', 'nu_mien_bac': 'banmai', 'nu_mien_trung': 'myan', 'nu_mien_nam': 'lannhi'}
        voice_type = voice_list.get(voice_type)	
        # HTTP Request
        url = 'https://api.fpt.ai/hmi/tts/v5'
        # Header Parameters
        header_parameters = {'api_key': openfpt_api, 'speed': speed_read, 'prosody': '1', 'voice': voice_type}
        text_message = text_message.encode('utf-8')
        # Get url of audio file	
        url_mp3 = requests.post(url, data = text_message, headers = header_parameters).json()['async']
		
        # time sleep in seconds
        time_sleep = 0.5
        # time_wait = 10 seconds/time_sleep
        time_wait = 20
        tcount = 0
        
        # check status request
        res_response = requests.get(url_mp3)
        res_status = res_response.status_code
        # Wait for hass request FPT Speech Synthesis to complete
        while (res_status == 404 and tcount < time_wait):
            time.sleep(time_sleep)
            res_response = requests.get(url_mp3)
            res_status = res_response.status_code
            tcount += 1
        # if error => msgbox_error
        if tcount == time_wait:
            msgbox_error = "Đã xảy ra lỗi. Vui lòng kiểm tra lại."
            msgbox_error = msgbox_error.encode('utf-8')
            url_error = requests.post(url, data = msgbox_error, headers = header_parameters).json()['async']
            res_response = requests.get(url_error)

        # Delete if File exist
        # if os.path.exists(CONF_FILE_PATH):
            # os.remove(CONF_FILE_PATH)

        # Download audio file
        uniq_filename = 'tts_fpt_' + str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'
        audio_file = open(CONF_FILE_PATH + uniq_filename, 'wb')
        audio_file.write(res_response.content)
        audio_file.close()
	
        ## Play audio file on media player ##	
        # media_content_id
        url_audio = url_hass + CON_AUDIO_PATH + uniq_filename
        # service data for 'CALL SERVICE' in Home Assistant
        service_data = {'entity_id': media_id, 'media_content_id': url_audio, 'media_content_type': 'audio/mp3'}
        # Call service from Home Assistant
        hass.services.call('media_player', 'play_media', service_data)
        
    hass.services.register(DOMAIN, SERVICE_FPT_TTS, tts_handler)
    return True
