

class XbeeData:
	"""	Class to collect data from Xbee Pro module."""
	def __init__(self):
		import serial
		self.USB_data_Package = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

		self.calibration_system = ""
		self.magnetic_heading = ""
		self.roll = ""
		self.pitch = ""
		self.HPA_pressure = ""
		self.humidity = ""
		self.temperature = ""
		self.latitude = ""
		self.longitude = ""
		self.GPS_altitude = ""
	

	def update_data(self):

		for data in self.USB_data_Package.readline().split("~"):   #Get data payload

			if data[0:4] == "Cal ":
				self.calibration_system = data[4:]		#Slice off ID (first 4 chars)
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
				self.longitude = data[4:]
			elif data[0:4] == "GPSA":
				self.GPS_altitude = data[4:]
			


		