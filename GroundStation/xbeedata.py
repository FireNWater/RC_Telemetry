

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

		self.complete_data_package = False

		while (not self.complete_data_package):

			data = self.USB_data_Package.readline().strip()   	#Get data payload from Arduino

			if data[0:4] == "Done":						#Check if package is finished
				self.complete_data_package = True 		#Set flag to exit while() loop
			elif data[0:4] == "Cal ":
				self.calibration_system = data[4:]		#Slice off ID
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
			


		