from input import *
from storage import *
from alert_system import *

if __name__ == "__main__":
	#Input Module#
	patientInfo = getPatientInfo()
	patientInfo.encode("ascii","replace")
	sensorData = readSensorData()
	sensorData.encode("ascii","replace")

	#Storage Module#
	#Insert paitent and sensor data into mongodb
	insert(patientInfo, sensorData)
	#Search for Patient Details using PatientId
	patientDetails = searchPerson("1234")

	#Alert Module#
	#CHeck sensorData for alerts#
	alert = alertCheck(sensorData)
	
	
