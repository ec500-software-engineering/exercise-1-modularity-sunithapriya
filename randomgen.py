import random
import json
# for x in range(10):
#   print random.randint(1,101)
def randomData():
	sensordata = {}
	sensordata['1234'] = {'pulse': random.randint(60,70),
						'pulseRange': {'lower': 60, 'upper': 70},
						'bloodPressure': random.randint(80,90),
						'pressureRange': {'lower':80, 'upper':90},
						'bloodOx': random.randint(100,120),
						'oxRange': {'lower':100, 'upper':120},
						'time': '12-Feb-2019'}
	json_string = json.dumps(sensordata)
	return(json_string)