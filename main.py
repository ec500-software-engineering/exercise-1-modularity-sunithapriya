from input import getPatientInfo
from input import readSensorData
from storage import *
from alert_system import *
from output import *

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
	#Check sensorData for alerts#
	alert = alertCheck(sensorData)
	
	#Output Module#
	patient = patient()
	#Recieve message from Alert system
	patient.recieveFromAlert(alert)
	#Display alert to UI
	patient.send_alert_to_UI()



