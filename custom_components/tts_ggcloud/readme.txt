
Developed base on source code at: https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/texttospeech

How to create Google API key : https://support.google.com/googleapi/answer/6158862?hl=en

We need create a folder with name is tts in your homeassistant local folder to store tts file (/config/www/tts)
This is the example of speaking using this Service

script:
  gg_reading_01:  #May be from your script name
    sequence:  
    - service: tts_ggcloud.say
      data_template:
        entity_id: media_player.van_phong
        message: "Your text input here" #May be from your input_text
        speed: '1.0' #May be from your input_number
        pitch: '0' #May be from your input_number
        language: "vi-VN" #May be from your input_select
        voice_name: "vi-VN-Wavenet-A"' #May be from your input_select

Thank you!
