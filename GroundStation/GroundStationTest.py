#!/usr/bin/env python

import xbeedata

telemetry = xbeedata.XbeeData()

for i in range(1, 10):
	
	telemetry.update_data()

	print "System Calibration: " + telemetry.calibration_system
	print "Roll" + telemetry.roll
	
