"""  
	Class to collect data from Xbee Pro module, parse, and make available to
	other modules
"""

class XbeeData:
	def __init__(self):
		import serial
		self.USB_data_Package = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

		self.calibration_system = ""
		self.calibration_gyro = ""
		self.calibration_accel = ""
		self.calibration_mag = ""
		self.magnetic_heading = ""
		self.roll = ""
		self.pitch = ""
		self.HPA_pressure = ""
		self.humidity = ""
		self.temperature = ""
		self.latitude = ""
		self.longtitude = ""
		self.GPS_altitude = ""
	

	def update_data(self):

		self.complete_data_package = False

		while (not self.complete_data_package):

			data = self.USB_data_Package.readline()
			#print data

			if data[0:4] == "Done":
				self.complete_data_package = True
			elif data[0:4] == "CalS":
				self.calibration_system = data[4:]
			elif data[0:4] == "CalG":
				self.calibration_gyro = data[4:]
			elif data[0:4] == "CalA":
				self.calibration_accel = data[4:]
			elif data[0:4] == "CalM":
				self.calibration_mag = data[4:]
			elif data[0:4] == "Mag_":
				self.magnetic_heading = data[4:]
			elif data[0:4] == "Roll":
				self.roll = data[4:]
			elif data[0:4] == "Pit_":
				self.pitch = data[4:]
			elif data[0:4] == "Pres":
				self.HPA_pressure = data[4:]
			elif data[0:4] == "Hum_":
				self.humidity = data[4:]
			elif data[0:4] == "Temp":
				self.temperature = data[4:]
			elif data[0:4] == "Lat:":
				self.latitude = data[4:]
			elif data[0:4] == "Long":
				self.longtitude = data[4:]
			elif data[0:4] == "GPSA":
				self.GPS_altitude = data[4:]
			


		