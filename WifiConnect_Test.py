import network
import time

def connect_wifi():
    ssid = "fathu_wuz_here"  # Replace with your Wi-Fi SSID
    password = "dindaaprili@"  # Replace with your Wi-Fi password
    
    # Create a WLAN object (Wi-Fi interface)
    wlan = network.WLAN(network.STA_IF)  
    wlan.active(True)  # Activate the Wi-Fi interface
    wlan.connect(ssid, password)  # Connect to the Wi-Fi network

    # Wait for connection
    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)  # Wait for the Wi-Fi to connect
    
    print("Connected to Wi-Fi")
    print("IP Address:", wlan.ifconfig()[0])  # Print the IP address of the ESP32

# Call the function to connect to Wi-Fi
connect_wifi()

import urequests

def make_get_request():
    url = "https://iot-group-9-backend.onrender.com/api/test/db_state"  # Example URL
    response = urequests.get(url)  # Send a GET request
    
    print("Response status code:", response.status_code)  # Print status code
    print("Response text:", response.text)  # Print the response content
    
    response.close()  # Close the response to free up resources

# Make the GET request
make_get_request()


