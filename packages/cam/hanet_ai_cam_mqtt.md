
1.2. Create Hanet configuration in Hass Configuration File

```sh
platform: "mqtt"
name: "hanet_camera_Nhận diện khuôn mặt"
state_topic: "/topic/detected/C20371B322"  #C20371B322 is serial of Hanet
value_template: "{{ value_json.person_type 
  ```

1.3. Create Automation to Hass
```sh
alias: Nhận diện khuôn mặt mở cửa
description: ''
trigger:
  - platform: state
    entity_id: sensor.hanet_camera_nhan_dien_khuon_mat
condition:
  - condition: state
    entity_id: sensor.hanet_camera_nhan_dien_khuon_mat
    state: '0'
  - condition: template
    value_template: '{{ trigger.to_state.state != trigger.from_state.state }}'
action:
  - device_id: 791411sdfsdfsadffadsfsdaaea36 # Device_id is id of Zigbee Device
    domain: lock
    type: unlock
    entity_id: lock.0x000d6f0012bb1a9c_lock
  - delay: '00:00:02'
  - service: mqtt.publish
    data:
      topic: /topic/detected/C20371B322
      payload_template: '{"person_type": 7}'
mode: single
  ```
