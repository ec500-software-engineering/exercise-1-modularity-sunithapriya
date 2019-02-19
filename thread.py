from input import getPatientInfo, readSensorData
from storage import searchPerson, insert
from alert_system import alertCheck
from output import patient
from randomgen import randomData
import threading 
import Queue


patientInfo = getPatientInfo()
patientInfo.encode("ascii","replace")

q = Queue.Queue() 

#Process each thread and add the output into a queue for displaying
def processThread(atientInfo,sensorData):
	#print(threading.current_thread())
	insert(patientInfo, sensorData)
	alert = alertCheck(sensorData)
	q.put(alert)
	
#Generate 3 random inputs and start a thread for each input
for i in range(3):
	sensorData = randomData()
	t = threading.Thread(target=processThread, args = (patientInfo,sensorData))
	t.daemon = True
	t.start()

#Display data from queue into output
while q.empty():
	alert = q.get()
	#Output Module
	patientOp = patient()
	#Recieve message from Alert system
	patientOp.recieveFromAlert(alert)
	#Display alert to UI
	patientOp.send_alert_to_UI()
