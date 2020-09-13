
#Feedreader

sensor:
  platform: feedparser
  name: Tin tức RSS
  feed_url: 'https://vnexpress.net/rss/tin-moi-nhat.rss'
  
  automation:
    
  - id: 'thong_bao_tin_tuc_cap_nhat'
    alias: "thong_bao_tin_tuc_cap_nhat"
    trigger:
      platform: state
      entity_id: 
      - sensor.tintuc_rss      
    condition:
      condition: and
      conditions:
        - condition: time
          after: '13:30'
          before: '12:00'
        - condition: template
          value_template: "{{ trigger.to_state.state != trigger.from_state.state }}"      
    action:
      service: script.doc_tin    
      
script:
  doc_tin:
    sequence:
    - service: media_player.volume_set
      data:
        entity_id: media_player.vali_demo
        volume_level: '0.5'
    - service: tts_viettel.say      
      data_template:
        message: "Có tin mới buổi {{ states('sensor.sys_buoi') }} lúc {{ as_timestamp(now()) | timestamp_custom('%I:%M:%S %p, %d/%m/%Y', true) }} như sau: {{states.sensor.tin_tuc_rss.attributes.entries}} " 
        entity_id: media_player.vali_demo
        speed: '1'
        voice_type: '{{["nu_mien_bac_01" , "nu_mien_bac_02" , "nam_mien_bac_01" , "nam_mien_bac_02" , "nu_mien_trung_01", "nam_mien_trung_01" , "nu_mien_nam_01" , "nu_mien_nam_02" , "nu_mien_nam_03" , "nam_mien_nam_01"] |random }} '  
       
          
