# Raspberry Pi Carplay

# Goal:
I currently have a 2007 Honda Accord and I am wanting to use a Raspberry Pi 4 to incorporate Carplay and a backup camera in my vehicle. 
This is currently is progress and this repository is to track code, hardware, 3D  prints, and anything that goes into this
with the hope that it becomes reusable for others.

## Components
### Hardware
* [Raspberry pi 4 4GM RAM](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-4gb)
* [7in Touchscreen display](https://www.raspberrypi.com/products/raspberry-pi-touch-display/)
* [Car microphone](https://www.amazon.com/dp/B0B84M452Z?psc=1&ref=ppx_yo2ov_dt_b_product_details) (a mic is needed for Siri/voice commands to work)
* [USB audio adapter](https://www.walmart.com/ip/Plugable-USB-Audio-Adapter-with-3-5mm-Speaker-Headphone-and-Microphone-Jack-Add-an-External-Stereo-Sound-Card-to-Any-PC/49301606)
(The microphone has to run through a USB to work - either it doesn't work to go through the Pi's aux or I couldn't figure it out)
* [Carplay adapter](https://www.amazon.com/dp/B088T9CZNK?psc=1&ref=ppx_yo2ov_dt_b_product_details) (special adapter needed to connect phone and make Carplay work)
* [AUX adapter](https://www.amazon.com/dp/B01EUZ948Y?psc=1&ref=ppx_yo2ov_dt_b_product_details) (this was a unique situation I ran into with a 2007 Honda Accord.
2003-2007 Honda Accords don't typically have an aux plug-in available, but for some reason they built them with the ability to have it - there's even
an AUX button in the car, but the AUX connectors were never put in. To connect the Carplay system through the car speakers I will need this adapter.
More info on this situation can be read [here](https://vehiclefreak.com/where-is-the-aux-port-in-a-2007-honda-accord/#:~:text=So%20in%20short%2C%20no%20the,the%20rear%20of%20the%20stereo.). 
Video on how to access and install the adapter [here](https://www.youtube.com/watch?v=0YeY0smqU9Q))
* To be updated: [Current Backup Camera](https://www.walmart.com/ip/Dual-Electronics-XCAM200-Waterproof-Full-Color-Backup-Camera-with-Wide-Viewing-Angle-Lens-and-Back-up-Parking-Guides/280067357?athbdg=L1200) - Still need to figure out the right one. Many of the cheaper wired backup cameras are analog (yellow RCA) and so I need to figure out a way to either [convert to digital signal](https://raspberrypi.stackexchange.com/questions/88113/rca-ntsc-camera-input-is-becoming-an-absolute-nightmare) and connect to the Pi, or find a usb camera. Potential adapter solution [here](https://www.amazon.com/easyday-DC60-Capture-Software-Compatible/dp/B0126O0RDC/ref=sr_1_3?keywords=easycap+dc60&qid=1662994455&sr=8-3).
The standard analog camera typically connects the power to the reverse lights so that when the car is put in reverse it turns the camera on. 
I like this approach and hope to incorporate it so that I don't need to include a button or something to change the screen from Carplay to the backup camera.
* [Reed Switch](https://arduinomodules.info/ky-021-mini-magnetic-reed-switch-module/) I am using this as a way to turn the backup camera on. I've installed this next to the reverse spot near the gear shifter. Then I have placed a magnet on the gear shifter so that when the car is in reverse the reed switch's signal changes. This will trigger the screen to switch to the backup camera. 
![IMG_2408](https://github.com/seth602/rpi_carplay/assets/107073994/bca9979b-b011-46c9-b79a-8d7970f0b864)


### Software
* I wouldn't have been able to make it work without the App Image created by [Rhys Morgan](https://github.com/rhysmorgan134/react-carplay). 
Huge thank you to Rhys!!!
(Check out the video on this [here](https://www.youtube.com/watch?v=mBeYd7RNw1w) - this is also where I learned about the Carplay adaper that is needed).
* ~~To-do: additional software to display backup camera and switch back and forth automatically~~ added 5/16/2023. 'show_backup_camera_v2.py' can be added to the pi's boot script and will run indefinitely in the background.

### 3D prints
* To-do: I've done a little bit with creating 3D designs that I then print at my local library. Given all the extra hardware and specific design of my car's dashboard
I want to experiment with designing my own case to hold the touchscreen, Pi, and other components.



