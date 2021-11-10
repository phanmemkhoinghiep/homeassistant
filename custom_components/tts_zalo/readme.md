#Hello
This is step by step guide to intergrated these TTS Component to your Home Assistant

### STEP1. Download to your Home Assistant Custom_Component Folder

1.1. git clone or copy row file to your Home Assistant Custom_Component Folder

### STEP2. Register and get Free Token/API from STT engines

2.1. Register Free ZALO TTS Account and get Token at: https://zalo.ai/user-profile


### STEP3. Configure these TTS Component

3.1. Create folder name tts at local home assistant: www/tts

3.2. Configure the API in your configuration.yaml

```sh
#TTS of Vietnamese Zalo TTS
tts_zalo:
 api: 'your Zalo API' 
   #See in the /custom_components/tts_zalo/readme.txt for more detail how to create Zalo API
  ```


### STEP4. Configure these TTS Component

4.1. Example script use Zalo TTS
```sh
script:
  zalo_reading_07:
    sequence:  
    - service: tts_zalo.say
      data_template:
        entity_id: media_player.note4    
        message: "{{ Your text here }}
        voice_type: 'nu_mien_nam_01'    
        speed: '1.0'  

```

### STEP5. Enjoy with the TTS voice
