Abbree wireless microphone that can be used with ham radio transceiver. Device comes with a dongle you can plug into radio.

You can also pair microphone with PC using bluetooth. However, in bluetooth mode there is no easy PTT down key event and PTT up event. 

Instead it is needed to detect PTT key down (push) from KEY_FASTFORWARD event and PTT key up (release) from KEY_REWIND. KEY_FASTFORWARD events are only sent for few seconds, so it cannot alone be used to detect PTT down.

Just see the code ptt-test.py

![Picture of Abbree bluetooth microphone](https://github.com/OH1KK/Abbree-wireles-microphone-ptt-detect/blob/main/abbree.jpg)

````
user@pc:~$ evtest /dev/input/event27 
Input driver version is 1.0.1
Input device ID: bus 0x5 vendor 0x5d6 product 0xa version 0x240
Input device name: "KST_vHMIC010 (AVRCP)"
Supported events:
  Event type 0 (EV_SYN)
  Event type 1 (EV_KEY)
    Event code 2 (KEY_1)
    Event code 3 (KEY_2)
    Event code 4 (KEY_3)
    Event code 5 (KEY_4)
    Event code 6 (KEY_5)
    Event code 7 (KEY_6)
    Event code 8 (KEY_7)
    Event code 9 (KEY_8)
    Event code 10 (KEY_9)
    Event code 11 (KEY_0)
    Event code 28 (KEY_ENTER)
    Event code 52 (KEY_DOT)
    Event code 59 (KEY_F1)
    Event code 60 (KEY_F2)
    Event code 61 (KEY_F3)
    Event code 62 (KEY_F4)
    Event code 63 (KEY_F5)
    Event code 64 (KEY_F6)
    Event code 65 (KEY_F7)
    Event code 66 (KEY_F8)
    Event code 67 (KEY_F9)
    Event code 103 (KEY_UP)
    Event code 105 (KEY_LEFT)
    Event code 106 (KEY_RIGHT)
    Event code 108 (KEY_DOWN)
    Event code 113 (KEY_MUTE)
    Event code 114 (KEY_VOLUMEDOWN)
    Event code 115 (KEY_VOLUMEUP)
    Event code 138 (KEY_HELP)
    Event code 139 (KEY_MENU)
    Event code 163 (KEY_NEXTSONG)
    Event code 165 (KEY_PREVIOUSSONG)
    Event code 166 (KEY_STOPCD)
    Event code 167 (KEY_RECORD)
    Event code 168 (KEY_REWIND)
    Event code 171 (KEY_CONFIG)
    Event code 174 (KEY_EXIT)
    Event code 200 (KEY_PLAYCD)
    Event code 201 (KEY_PAUSECD)
    Event code 208 (KEY_FASTFORWARD)
    Event code 353 (KEY_SELECT)
    Event code 356 (KEY_POWER2)
    Event code 358 (KEY_INFO)
    Event code 362 (KEY_PROGRAM)
    Event code 364 (KEY_FAVORITES)
    Event code 395 (KEY_LIST)
    Event code 398 (KEY_RED)
    Event code 399 (KEY_GREEN)
    Event code 400 (KEY_YELLOW)
    Event code 401 (KEY_BLUE)
    Event code 402 (KEY_CHANNELUP)
    Event code 403 (KEY_CHANNELDOWN)
    Event code 405 (KEY_LAST)
  Event type 2 (EV_REL)
Key repeat handling:
  Repeat type 20 (EV_REP)
    Repeat code 0 (REP_DELAY)
      Value    300
    Repeat code 1 (REP_PERIOD)
      Value     33
Properties:
Testing ... (interrupt to exit)
Event: time 1775597439.781202, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 1
Event: time 1775597439.781202, -------------- SYN_REPORT ------------
Event: time 1775597440.088066, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 2
Event: time 1775597440.088066, -------------- SYN_REPORT ------------
Event: time 1775597440.099149, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 0
Event: time 1775597440.099149, -------------- SYN_REPORT ------------
Event: time 1775597440.362117, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 1
Event: time 1775597440.362117, -------------- SYN_REPORT ------------
Event: time 1775597440.664069, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 2
Event: time 1775597440.664069, -------------- SYN_REPORT ------------
Event: time 1775597440.698063, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 2
Event: time 1775597440.698063, -------------- SYN_REPORT ------------
Event: time 1775597440.732063, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 2
Event: time 1775597440.732063, -------------- SYN_REPORT ------------
Event: time 1775597440.766064, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 2
Event: time 1775597440.766064, -------------- SYN_REPORT ------------
Event: time 1775597440.800063, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 2
Event: time 1775597440.800063, -------------- SYN_REPORT ------------
Event: time 1775597440.834063, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 2
Event: time 1775597440.834063, -------------- SYN_REPORT ------------
Event: time 1775597440.868064, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 2
Event: time 1775597440.868064, -------------- SYN_REPORT ------------
Event: time 1775597440.902066, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 2
Event: time 1775597440.902066, -------------- SYN_REPORT ------------
Event: time 1775597440.902153, type 1 (EV_KEY), code 208 (KEY_FASTFORWARD), value 0
Event: time 1775597440.902153, -------------- SYN_REPORT ------------
Event: time 1775597441.179190, type 1 (EV_KEY), code 168 (KEY_REWIND), value 1
Event: time 1775597441.179190, -------------- SYN_REPORT ------------
Event: time 1775597441.479567, type 1 (EV_KEY), code 168 (KEY_REWIND), value 0
Event: time 1775597441.479567, -------------- SYN_REPORT ------------
````
