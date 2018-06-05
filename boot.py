import esp
import gc
gc.collect()

import network
import urequests
import ujson
import time
import machine

file = open("configuration.json")
configuration = ujson.loads(file.read())
file.close()
access_point = configuration["access_point"]
access_point_password = configuration["access_point_password"]
hue_bridge_ip = configuration["hue_bridge_ip"]
hue_api_key = configuration["hue_api_key"]
onboard_led = 2

def api_url(path):
    return "http://" + hue_bridge_ip + "/api/" + hue_api_key + path

def turn_on_led():
    led = machine.Pin(onboard_led, machine.Pin.OUT)
    led.off()

def turn_off_led():
    led = machine.Pin(onboard_led, machine.Pin.OUT)
    led.on()

def connect():
    wireless = network.WLAN(network.STA_IF)
    wireless.active(True)
    wireless.connect(access_point, access_point_password)
    turn_on_led()
    while True:
        time.sleep(0.1)
        if wireless.isconnected():
            turn_off_led()
            return True
            break

def get(url):
    response = urequests.get(url)
    content = response.content
    response.close()
    return content

def put(url, json):
    response = urequests.put(url, json=json)
    content = response.content
    response.close()
    return content

def toggle_lights():
    lights = ujson.loads(get(api_url("/lights")))
    for light_id in lights:
        on = lights['1']['state']['on']
        print("Light " + light_id + " on:", on)

        if on:
            print(put(api_url("/lights/" + light_id + "/state"), { 'on': False, "bri": 150}))
        else:
            print(put(api_url("/lights/" + light_id + "/state"), { 'on': True, "bri": 150}))

connect()
toggle_lights()
