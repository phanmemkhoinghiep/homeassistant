Register Free Viettel TTS Account and get Token at: https://viettelgroup.ai/en

We need create a folder with name is tts in your homeassistant local folder to store tts file (/config/www/tts)

Develop based on Python orignal source code at: https://viettelgroup.ai/document/tts


This is a example how to use this service

script:
  viettel_reading_08:
    sequence:  
    - service: tts_viettel.say
      data_template:
        entity_id: media_player.note4    
        message: "{{ Your text here }}
        voice_type: 'nu_mien_nam_1'    
        speed: '1.0'  


Thank you!
