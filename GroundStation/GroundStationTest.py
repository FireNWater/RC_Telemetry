#!/usr/bin/env python

import xbeedata as xb

telemetry = xb.XbeeData()

for i in range(1, 5):
	
	telemetry.update_data()

	print "System Calibration: " + telemetry.calibration_system
	print "Roll" + telemetry.roll
	print  float(telemetry.roll) + 100.0
	print "Pitch" + telemetry.pitch
	print "Mag Hdg" + telemetry.magnetic_heading