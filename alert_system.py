"""
Credit @author: Xiangkun Ye

"""
import json


def sendToUI(msg,j):
    ui_dict={"alert_message":msg,"bloodPressure":j["bloodPressure"],"pulse":j["pulse"],"bloodOx":j["bloodOx"]}
    ui_json=json.dumps(ui_dict)
    return ui_json
    #call_output_method

def alertCheck(j_o):
    j=json.loads(j_o)
    alert_message=""
    for value in j.values():
        val = value
    if(val["bloodPressure"]<val["pressureRange"]["lower"]):
        alert_message+="BloodPressure is Too low, "
    elif(val["bloodPressure"]>val["pressureRange"]["upper"]):
        alert_message="BloodPressure is Too high, "
    if(val["pulse"]<val["pulseRange"]["lower"]):
        alert_message+="Pulse is Too low, "
    elif(val["pulse"]>val["pulseRange"]["upper"]):
        alert_message+="Pulse is Too high, "
    if(val["bloodOx"]<val["oxRange"]["lower"]):
        alert_message+="BloodOx is Too low, "
    elif(val["bloodOx"]>val["oxRange"]["upper"]):
        alert_message+="BloodOx is Too high, "
    return sendToUI(alert_message, val)