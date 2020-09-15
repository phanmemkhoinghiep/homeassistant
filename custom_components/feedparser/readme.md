#Using Custom Component FeedParser at
#https://github.com/custom-components/feedparser/blob/master/custom_components/feedparser/sensor.py
#to view Rss news and play the newest 

This is step by step guide to intergrated these TTS Component to your Home Assistant

### STEP1. Download to your Home Assistant Custom_Component Folder

1. git clone or copy row file to your Home Assistant Custom_Component Folder

### STEP2. Configure the TTS Component

1. Assign input for the RSS Sensor

```sh
sensor:
  - platform: feedparser
    name: RSS News 1
    feed_url: 'https://vnexpress.net/rss/tin-moi-nhat.rss'
    date_format: '%a, %b %d %I:%M %p'
    inclusions:
      - title
      - summary    
    exclusions:
      - link
      - description
      - image
      - language
      - pubDate  
      - language  

  - platform: feedparser
    name: RSS News 2
    feed_url: 'https://thanhnien.vn/rss/home.rss'
    date_format: '%a, %b %d %I:%M %p'
    inclusions:
      - title
      - summary    
    exclusions:
      - link
      - description
      - image
      - language
      - pubDate  
      - language  
  - platform: feedparser
    name: RSS News 3
    feed_url: 'https://forbesvietnam.com.vn/rss/home.rss'
    date_format: '%a, %b %d %I:%M %p'
    inclusions:
      - title
      - summary    
    exclusions:
      - link
      - description
      - image
      - language
      - pubDate  
      - language  
```
2. Configure Automation
```sh      
automation:
    
  - id: 'thong_bao_tin_tuc_cap_nhat_1'
    alias: "thong_bao_tin_tuc_cap_nhat_1"
    trigger:
      platform: state
      entity_id: 
      - sensor.rss_news_1      
    condition:
      condition: and
      conditions:
        - condition: time
          after: '13:30'
          before: '12:00'
        - condition: template
          value_template: "{{ trigger.to_state.state != trigger.from_state.state }}"   
    action:
      service: script.doc_tin_1    

  - id: 'thong_bao_tin_tuc_cap_nhat_2'
    alias: "thong_bao_tin_tuc_cap_nhat_2"
    trigger:
      platform: state
      entity_id: 
      - sensor.rss_news_2      
    condition:
      condition: and
      conditions:
        - condition: time
          after: '13:30'
          before: '12:00'
        - condition: template
          value_template: "{{ trigger.to_state.state != trigger.from_state.state }}"   
    action:
      service: script.doc_tin_2    

  - id: 'thong_bao_tin_tuc_cap_nhat_3'
    alias: "thong_bao_tin_tuc_cap_nhat_3"
    trigger:
      platform: state
      entity_id: 
      - sensor.rss_news_3      
    condition:
      condition: and
      conditions:
        - condition: time
          after: '13:30'
          before: '12:00'
        - condition: template
          value_template: "{{ trigger.to_state.state != trigger.from_state.state }}"      
    action:
      service: script.doc_tin_3    
```
2. Configure Script

```sh      
script:

  doc_tin_1:
    sequence:
    - service: media_player.volume_set
      data:
        entity_id: media_player.vali_demo
        volume_level: '0.5'
    - service: tts_viettel.say      
      data_template:
        message: "Có tin mới cập nhật buổi {{ states('sensor.sys_buoi') }} lúc {{ as_timestamp(now()) | timestamp_custom('%I:%M:%S %p, %d/%m/%Y', true) }} tựa đề {{ states.sensor.rss_news_1.attributes.entries[0].title }} và nội dung: {{ states.sensor.all_news_1.attributes.entries[0].summary|striptags }} "
        entity_id: media_player.vali_demo
        speed: '1'
        voice_type: '{{["nu_mien_bac_01" , "nu_mien_bac_02" , "nam_mien_bac_01" , "nam_mien_bac_02" , "nu_mien_trung_01", "nam_mien_trung_01" , "nu_mien_nam_01" , "nu_mien_nam_02" , "nu_mien_nam_03" , "nam_mien_nam_01"] |random }} '  

  doc_tin_2:
    sequence:
    - service: media_player.volume_set
      data:
        entity_id: media_player.vali_demo
        volume_level: '0.5'
    - service: tts_viettel.say      
      data_template:
        message: "Có tin mới cập nhật buổi {{ states('sensor.sys_buoi') }} lúc {{ as_timestamp(now()) | timestamp_custom('%I:%M:%S %p, %d/%m/%Y', true) }} tựa đề {{ states.sensor.rss_news_2.attributes.entries[0].title }} và nội dung: {{ states.sensor.all_news_1.attributes.entries[0].summary|striptags }} "
        entity_id: media_player.vali_demo
        speed: '1'
        voice_type: '{{["nu_mien_bac_01" , "nu_mien_bac_02" , "nam_mien_bac_01" , "nam_mien_bac_02" , "nu_mien_trung_01", "nam_mien_trung_01" , "nu_mien_nam_01" , "nu_mien_nam_02" , "nu_mien_nam_03" , "nam_mien_nam_01"] |random }} '  

  doc_tin_3:
    sequence:
    - service: media_player.volume_set
      data:
        entity_id: media_player.vali_demo
        volume_level: '0.5'
    - service: tts_viettel.say      
      data_template:
        message: "Có tin mới cập nhật buổi {{ states('sensor.sys_buoi') }} lúc {{ as_timestamp(now()) | timestamp_custom('%I:%M:%S %p, %d/%m/%Y', true) }} tựa đề {{ states.sensor.rss_news_3.attributes.entries[0].title }} và nội dung: {{ states.sensor.all_news_1.attributes.entries[0].summary|striptags }} "
        entity_id: media_player.vali_demo
        speed: '1'
        voice_type: '{{["nu_mien_bac_01" , "nu_mien_bac_02" , "nam_mien_bac_01" , "nam_mien_bac_02" , "nu_mien_trung_01", "nam_mien_trung_01" , "nu_mien_nam_01" , "nu_mien_nam_02" , "nu_mien_nam_03" , "nam_mien_nam_01"] |random }} '        

```      
3. Configure Lovelace View

```sh
title: Tin tức cập nhật
icon: mdi:rss
path: news 
panel: false # this renders the first card on full width, other cards in this view will not be rendered
cards: 
  - type: custom:vertical-style-card
    title: Tin tức cập nhật
    style:
      font_size: 16px
      border: true
      background_color: var(--secondary-background-color)
    cards:
      - type: horizontal-stack
        cards:
        - type: markdown        
          title: VnExpress
          content: >
           {{ states.sensor.all_news_1.attributes.entries|replace("[", "")|replace("]", "")|replace("{", "")|replace("}", "")|replace("title", "Tiêu đề")|replace("summary", "Nội dung") }}
        - type: markdown        
          title: Thanh Niên
          content: >
           {{ states.sensor.all_news_2.attributes.entries|replace("[", "")|replace("]", "")|replace("{", "")|replace("}", "")|replace("title", "Tiêu đề")|replace("summary", "Nội dung") }}
        - type: markdown        
          title: Forbes
          content: >
           {{ states.sensor.all_news_3.attributes.entries|replace("[", "")|replace("]", "")|replace("{", "")|replace("}", "")|replace("title", "Tiêu đề")|replace("summary", "Nội dung") }}
           
```            
### STEP4. Restart Home Assistant
