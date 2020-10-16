#Hello
This is step by step guide to intergrated these TTS Component to your Home Assistant

### STEP1. Download to your Home Assistant Custom_Component Folder

1. git clone or copy row file to your Home Assistant Custom_Component Folder

### STEP2. Configure these TTS Component

1. Register Free FPT TTS Account and get API at: https://fpt.ai/

2. Register Free Viettel TTS Account and get Token at: https://viettelgroup.ai/en

3. Register and create Google API key at: https://support.google.com/googleapi/answer/6158862?hl=en

4. Create folder name tts at local home assistant: www/tts

5. Configure the API in your configuration.yaml
```sh
#TTS of Vietnamese FPT TTS
tts_fpt:
 api_key: 'your_key'
#See in the /custom_components/tts_fpt/readme.txt for more detail how to create FPT API
#No need to use Base URL for this component
# Service for play url file that given by FPT API
media_extractor:
```
3. Restart your hass to active these TTS Component

### STEP2. Configure these TTS Component
1. Example script use FPT TTS

```sh
service
  fpt_reading_06:
    sequence:  
    - service: tts_fpt.say
      data_template:
        entity_id: media_player.note4   
        message: "{{ Your text here }}
        voice_type: 'nu_mien_bac' 
        speed: '1.0'
```

5. Enjoy with the TTS voice
