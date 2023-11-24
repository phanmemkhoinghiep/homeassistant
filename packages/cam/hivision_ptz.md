#Step 1: Configuration Cam

1.1. Enable “digest/basic” verification for Web. The menu path is: Configuration > System > Security > Verification > Web verification.

1.2. Create an extra user if don't want use Admin user: Configuration > System > User management > User management > Add. Choose for the level of ‘operator’ and check if ‘Remote PTZ control’ is enabled for this new user. The username and password are referred to as PTZ_USER_NAME and PTZ_PASSWORD in the description below.

1.3. Fixed the IP address of the camera in the Camera configuration or Modem /Router WiFi.

#Step2: Add Cam Stream to Hass

#Step3: Add configuration to Configuration File in Hass
3.1. Add rest_command to Hass
```sh
camera:
  - platform: ffmpeg
    name: wf_cam_ptz
    input: rtsp://admin:password@192.168.1.3:554     
```
3.2. Add rest_command to Hass
```sh
rest_command: #Hass will send HTTP Rest Request to Cam PTZ within LAN
  wf_cam_ptz_momentary: #This is  template rest_command to move PTZ Camera from the current position
    url: http://192.168.1.3/ISAPI/PTZCtrl/channels/1/Momentary
    method: PUT
    payload: '<PTZData>
              	<pan>{{ pan }}</pan>
              	<tilt>{{ tilt }}</tilt>
              	<zoom>{{ zoom }}</zoom>
              	<Momentary>
                  <duration>500</duration> #duration: in msecs
              	</Momentary>
              </PTZData>'
    username: admin
    password: password
    content_type: 'application/xml'
    verify_ssl: false
  wf_cam_ptz_absolute: #This is  template rest_command to move PTZ Camera to the fixed position
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
  ```
3.3. Restart Hass

#4. Add Hass

4.1. Add Script to move PTZ Camera from the current position

```sh
script:
#PTZ Camera
  wf_cam_ptz_1:
    alias: 'Cam PTZ control 1'
    sequence:
      - service: rest_command.wf_cam_ptz_momentary
        data:
          pan: -50 # (The value is -100..100, <0 to left, >0 to right)
          tilt: 0 # ( The value is -100..100) 
          zoom: 0   ( The value is -100..100)
```
4.2. Add Script to move PTZ Camera from the current posittion to the fixed position

```sh
  # azimuth: 0..3300, elevation: 0..900, absoluteZoom: 10..40
  wf_cam_ptz_zero_position:
    alias: 'Cam4 PTZ zero position'
    sequence:
      - service: rest_command.wf_cam_ptz_absolute
        data:
          azimuth: 1500
          elevation: 0
          absoluteZoom: 10
   ```
