#Step 1: Configuration Hass

1.1. Go to Configuration, Intergrations, Add Intergrations

1.2. Search and select IFTTT, OK

1.3 Copy IFTT Webhook Url

1.4 Replace the local ip address of Hass in IFTT Webhook URL with external (Base URL) of Hass

1.5 Write down this Webhook URL

#Step 2: Configuration in Hanet Developers Page

2.1. Go to http://developers.hanet.ai/

2.2. Select console

2.3. Login with Hanet Account that control the Hanet AI Camera

2.4. Create an App

2.5. Put the Webhook URL in 1.5 in to WebHook filed

2.6. Save and close 

#Step3: Configuration in Hanet Connect App

3.1. Go to Home Tab

3.2. Select the Camera

3.3. Select three dot in the upper right conner to go to the Camera Setting

3.4. Select Annoucement Section, Anncoucement Setting

3.5. Enable Annoucment for Execute, Stranger, Customer

#Step4: Add configuration to Configuration File in Hass

4.1. Create Automation to Hass
```sh
- id: '1611224207667'
  alias: Test Cam Hanet phát hiện nhân viên
  description: Test Cam Hanet phát hiện nhân viên
  trigger:
    event_type: ifttt_webhook_received
    platform: event
    # event_data:
      # action: 'call_service'
  condition:
  - condition: template
    value_template: '{{ trigger.event.data.personType in ["0"] }}'
  action:
  - service: tts_viettel.say
    data:
      message: 'Phát hiện {{ trigger.event.data.personName }}'      
      entity_id: media_player.phong_da_nang_speaker
      speed: '0.8'
      voice_type: nu_mien_bac_01
  mode: single 

- id: '1611224207890'
  alias: Test Cam Hanet phát hiện đối tác
  description: Test Cam Hanet phát hiện đối tác
  trigger:
    event_type: ifttt_webhook_received
    platform: event
    # event_data:
      # action: 'call_service'
  condition:
  - condition: template
    value_template: '{{ trigger.event.data.personType in ["1"] }}'
  action:
  - service: tts_viettel.say
    data:
      message: 'Phát hiện đối tác {{ trigger.event.data.personName }} '      
      entity_id: media_player.phong_da_nang_speaker
      speed: '0.8'
      voice_type: nu_mien_bac_01
  mode: single 

- id: '1611797640597'
  alias: Test Cam Hanet phát hiện người lạ
  description: Test Cam Hanet phát hiện người lạ
  trigger:
    event_type: ifttt_webhook_received
    platform: event
    # event_data:
      # action: 'call_service'
  condition:
  - condition: template
    value_template: '{{ trigger.event.data.personType in ["2"] }}'
  action:
  - service: tts_viettel.say
    data:
      message: 'Phát hiện người lạ '      
      entity_id: media_player.phong_da_nang_speaker
      speed: '0.8'
      voice_type: nu_mien_bac_01
  mode: single 
  ```
4.2. Reload Automation

