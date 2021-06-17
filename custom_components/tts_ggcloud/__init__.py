# Declare variables
DOMAIN = 'tts_ggcloud'
SERVICE_GGCLOUD_TTS = 'say'
# config
CONF_API = 'api'
CONF_SPEED = 'speed'
CONF_PITCH = 'pitch'
CONF_URL_HASS = 'url'
CONF_LANGUAGE_CODE ='language'
# data service
CONF_PLAYER_ID = 'entity_id'
CONF_MESSAGE = 'message'
CONF_VOICE_NAME = 'voice_name'

# audio file path

CONF_FILE_PATH = '/config/www/tts/'
CON_AUDIO_PATH = '/local/tts/'


import requests, json, os, time, urllib, datetime, base64

def setup(hass, config):

    def tts_handler(data_call):


        # Get config
        
        url_hass = str(config[DOMAIN][CONF_URL_HASS])
        api = str(config[DOMAIN][CONF_API])
        # Get data service
        media_id = data_call.data.get(CONF_PLAYER_ID)
        message = str(data_call.data.get(CONF_MESSAGE)[0:2000])
        voice_name = data_call.data.get(CONF_VOICE_NAME)
        speed = data_call.data.get(CONF_SPEED)
        pitch = data_call.data.get(CONF_PITCH)
        languageCode = data_call.data.get(CONF_LANGUAGE_CODE)
        # List voice of Google Speech Synthesis
        voice_list = {'Google_Voice_1': 'vi-VN-Wavenet-A', 'Google_Voice_2': 'vi-VN-Wavenet-B', 'Google_Voice_3': 'vi-VN-Wavenet-C', 'Google_Voice_4': 'vi-VN-Wavenet-D', 'Google_Voice_5': 'vi-VN-Standard-A', 'Google_Voice_6': 'vi-VN-Standard-B', 'Google_Voice_7':'vi-VN-Standard-C' , 'Google_Voice_8':'vi-VN-Standard-D'}
        voice_name = voice_list.get(voice_name)
        #HTTP Request
        url = 'https://texttospeech.googleapis.com/v1beta1/text:synthesize?key='+ api
        #Header Parameters
        headers = {'Content-type': 'application/json'}
        # Body Parameters
        data = { "audioConfig": { "audioEncoding": "MP3", "pitch": pitch, "speakingRate": speed },  "input": { "text": message }, "voice": { "languageCode": languageCode, "name": voice_name }}
		#Get respounse from Server	
        response = requests.post(url, data = json.dumps(data), headers = headers)
        # Cut audio string from response
        audio_string = response.text.split('"')
        # Convert audio string to audio byte
        audio_byte = base64.b64decode(audio_string[3])
        # Create unique audio file name
        uniq_filename = 'tts_ggcloud' + str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'
        # Open audio file
        audio_file = open(CONF_FILE_PATH + uniq_filename, 'wb')
        # Write audio byte to file
        audio_file.write(audio_byte)
        audio_file.close()

    	# Play audio file with Home Assistant Service#	
        url_file = url_hass + CON_AUDIO_PATH + uniq_filename
        # service data for 'CALL SERVICE' in Home Assistant
        service_data = {'entity_id': media_id, 'media_content_id': url_file, 'media_content_type': 'music'}
        # Call service from Home Assistant
        hass.services.call('media_player', 'play_media', service_data)
        
    hass.services.register(DOMAIN, SERVICE_GGCLOUD_TTS, tts_handler)
    return True
