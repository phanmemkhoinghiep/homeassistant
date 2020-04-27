
Developed base on source code at: https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/texttospeech

How to create Google API key : https://support.google.com/googleapi/answer/6158862?hl=en

We need create a folder with name is tts in your homeassistant local folder to store tts file (/config/www/tts)
This is the example of speaking using this Service

script:
  gg_reading_01:
    sequence:  
    - service: tts_ggcloud.say
      data_template:
        entity_id: media_player.van_phong
        message: "Your text input here"
        speed: '1.0'
        pitch: '0'
        language: "vi-VN"
        voice_name: "vi-VN-Wavenet-A"



Thank you!
