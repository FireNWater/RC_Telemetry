
//	This sketch uses 9DOF sensor and GPS unit data transmitted by an XBee Pro module to a ground station.
//
//	9DOF (Adafruit_BNO055) I2C connection on	Pins A4, A5
//	GPS (Adafruit Ultimate GPS) connection on	Software Serial Pins 4, 5
//	XBee Pro 2.4Ghz modem on					Software Serial Pins 2, 3


#include <SoftwareSerial.h>		// Serial ports for GPS and Xbee
#include <Wire.h>				// I2C library
#include <SPI.h>				// SPI library
#include <Adafruit_BME280.h>	// Altimeter library
#include <Adafruit_Sensor.h>	// Adafruit sensor
#include <Adafruit_BNO055.h>	// 9DOF Sensor library
#include <utility/imumaths.h>	// Library needed for 9DOF sensor (I think)
#include <TinyGPS++.h>			// GPS library

// Constants for the BNO055 9DOF Sensor
#define BNO055_SAMPLERATE_DELAY_MS (500)
Adafruit_BNO055 bno = Adafruit_BNO055();

// TinyGPS++
TinyGPSPlus gps;
static const uint32_t GPSBaud = 9600;

// BME280 Altimeter
Adafruit_BME280 altimeter;
float seaLevelPressure = 1013.25;	// default Standard Day pressure

// Set up the Software Serial Ports 
SoftwareSerial XBeeSerial = SoftwareSerial(2, 3);
SoftwareSerial GPSSerial =  SoftwareSerial(5, 4);

void setup()  {

	//pinMode(13, OUTPUT);	// Setup to use COM port for IDE.
	//Serial.begin(9600);		// 

	/* Initialize the 9 DOF sensor */
	if (!bno.begin())
	{
		/* There was a problem detecting the BNO055 ... check your connections */
		Serial.println("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
		while (1);
	}

	bno.setExtCrystalUse(true);
	
	// Initialize the altimeter
	if (!altimeter.begin()) {
		Serial.println("Could not find a valid BME280 sensor, check wiring!");
		while (1);
	}
	// set the data rate for the XBee SoftwareSerial port
	XBeeSerial.begin(9600);

	// Set up the GPS Sensor
	GPSSerial.begin(GPSBaud);

}	// End Setup()



void loop()                     // run over and over again
{
	String sensorDataPayload = "";

	// Build the Gyro Calibration payload
	uint8_t system, gyro, accel, mag = 0;
	bno.getCalibration(&system, &gyro, &accel, &mag);
	sensorDataPayload   =	"Cal S:"	+ String(system, DEC) 
							+ " G:"		+ String(gyro, DEC) 
							+ " A:"		+ String(accel, DEC) 
							+ " M:"		+ String(mag, DEC)
							+"~";						// Using "~" as separator

	// Build Gyro Orientation payload

	imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
	
	sensorDataPayload	+=	"Mag_"		+ String(euler.x())
							+ "~"
							+ "Roll"	+ String(euler.y())
							+ "~"
							+ "Pit_"	+ String(euler.z())
							+ "~";

	// Build the Altimeter payload

	sensorDataPayload +=	"Pres"		+ String(altimeter.readPressure())
							+ "~"
							+ "Hum_"	+ String(altimeter.readHumidity())
							+ "~"
							+ "Temp"	+ String(altimeter.readTemperature())
							+ "~";

	// Build the GPS payload

	sensorDataPayload +=	"Lat:"		+ String(gps.location.lat(), 8)
							+ "~"
							+ "Long"	+ String(gps.location.lng(), 8)
							+ "~"
							+ "GPSA"	+ String(gps.altitude.feet())
							+ "~";

	sensorDataPayload +=	"Done";

	// Send the payload

	XBeeSerial.println(sensorDataPayload);

	smartDelay(50);		// Keeps GPS updating during delay

}	// End loop()


static void smartDelay(unsigned long ms)
{
	unsigned long start = millis();
	do
	{
		while (GPSSerial.available())
			gps.encode(GPSSerial.read());
	} while (millis() - start < ms);
}


