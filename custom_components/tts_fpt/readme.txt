Register Free FPT TTS Account and get API at: https://fpt.ai/

We need create a folder with name is tts in your homeassistant local folder to store tts file (/config/www/tts)
Develop based on Document at: https://docs.fpt.ai/docs/en/speech/documentation/text-to-speech

This is a example how to use this service
service
  fpt_reading_06:
    sequence:  
    - service: tts_fpt.say
      data_template:
        entity_id: media_player.note4   
        message: "{{ Your text here }}
        voice_type: 'nu_mien_bac' 
        speed: '1.0'

Thank you!
