#Step 1: Configuration Cam
#Enable “digest/basic” verification for Web. The menu path is: Configuration > System > Security > Verification > Web verification.
#Create an extra user if don't want use Admin user: Configuration > System > User management > User management > Add. Choose for the level of ‘operator’ and check if ‘Remote PTZ control’ is enabled for this new user. The username and password are referred to as PTZ_USER_NAME and PTZ_PASSWORD in the description below.
#Fixed the IP address of the camera in the Camera configuration or Modem /Router WiFi.
''
camera:

  - platform: ffmpeg
    name: wf_cam_ptz
    input: rtsp://admin:password@192.168.1.3:554     
''
rest_command: #Hass sẽ gửi HTTP Rest tới Cam PTZ qua mạng LAN
  wf_cam_momentary: #Đây là template lệnh quay quét của Caem
    url: http://192.168.1.3/ISAPI/PTZCtrl/channels/1/Momentary
    method: PUT
    payload: '<PTZData>
              	<pan>{{ pan }}</pan>
              	<tilt>{{ tilt }}</tilt>
              	<zoom>{{ zoom }}</zoom>
              	<Momentary>
                  <duration>500</duration>
              	</Momentary>
              </PTZData>'
    username: admin
    password: password
    content_type: 'application/xml'
    verify_ssl: false


  wf_cam_absolute: #Đây là template lệnh đưa CAM về 1 vị trí cố định
    url: http://192.168.1.3/ISAPI/PTZCtrl/channels/1/Absolute
    method: PUT
    payload: '<PTZData>
              	<AbsoluteHigh>
              	    <azimuth>{{ azimuth }}</azimuth>
              	    <elevation>{{ elevation }}</elevation>
              	    <absoluteZoom>{{ absoluteZoom }}</absoluteZoom>
              	</AbsoluteHigh>
              </PTZData>'
    username: admin
    password: password
    content_type: 'application/xml'
    verify_ssl: false
  

script:

#PTZ Camera
  # Các giá trị sẽ là: pan: -100..100, tilt: -100..100, zoom: -100..100, duration: in msecs            

  wf_cam_pan_left:
    alias: 'Cam111 pan left'
    sequence:
      - service: rest_command.wf_cam_111_momentary
        data:
          pan: -50
          tilt: 0
          zoom: 0

  wf_cam_pan_right:
    alias: 'Cam111 pan right'
    sequence:
      - service: rest_command.wf_cam_111_momentary
        data:
          pan: 50
          tilt: 0
          zoom: 0

  wf_cam_tilt_up:
    alias: 'Cam111 tilt up'
    sequence:
      - service: rest_command.wf_cam_111_momentary
        data:
          pan: 0
          tilt: 75
          zoom: 0

  wf_cam_tilt_down:
    alias: 'Cam111 tilt down'
    sequence:
      - service: rest_command.wf_cam_111_momentary
        data:
          pan: 0
          tilt: -75
          zoom: 0

  wf_cam_zoom_in:
    alias: 'Cam4 zoom in'
    sequence:
      - service: rest_command.wf_cam_111_momentary
        data:
          pan: 0
          tilt: 0
          zoom: 100

  wf_cam_zoom_out:
    alias: 'Cam111 zoom out'
    sequence:
      - service: rest_command.wf_cam_111_momentary
        data:
          pan: 0
          tilt: 0
          zoom: -100

  # azimuth: 0..3300, elevation: 0..900, absoluteZoom: 10..40
  wf_cam_ptz_zero:
    alias: 'Cam4 PTZ zero position'
    sequence:
      - service: rest_command.wf_cam_111_absolute
        data:
          azimuth: 1500
          elevation: 0
          absoluteZoom: 10
