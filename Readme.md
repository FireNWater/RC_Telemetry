RC_Telemetry
============

* This project uses an Arduino based sensor package to downlink various RC airplane flight parameters to a hand-held Raspberry Pi ground station.  The purpose is as a coaching tool to practice precision aerobatics.
* The airborne sensor package simply reads all of the attached sensors and transmits their values as strings thru the XBee Pro.
* The handheld ground station receives the sensor payload thru its XBee Pro receiver and sends the data to the handheld Raspberry Pi (Rpi) using the USB FTDI cable.  The Rpi then diplays the sensor readings to the pilot.

##Parts List:
-------------

###Airborne Sensor Package:
---------------------------
* (1) Arduino Uno R3
* (1) Adafruit prototyping board
* (1) Adafruit BNO055 9-DOF 3-axis absolute orientation sensor
* (1) Adafruit BME280 pressure / temperature / humidity sensor
* (1) Adafruit Ultimate GPS breakout board v3
* (1) XBee Pro S1 60mW transmitter / receiver
* (1) Adafruit XBee adapter board
* Various pins and pieces

###Handheld Ground Station:
---------------------------
* (1) Raspberry Pi2
* (1) Adafruit 2.8" 320 x 240 capacitive touch screen
* (1) USB FTDI cable
* (1) XBee Pro S1 60mW transmitter / receiver
* (1) Adafruit XBee adapter board
* Various pins and pieces

##Future Expansion:
-------------------
* Utilize the XBee's 2-way communication capabilities
* Add data logging to the ground station to review flight afterwards