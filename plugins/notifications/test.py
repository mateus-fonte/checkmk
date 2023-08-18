#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# My CheckMK Notification Plugin
import json
import os
import time


current_timestamp = int(time.time())

long_service_output = os.environ.get("NOTIFY_LONGSERVICEOUTPUT")
hostname = os.environ.get("NOTIFY_HOSTNAME")
service_output = os.environ.get("NOTIFY_SERVICEOUTPUT")
host_output = os.environ.get("NOTIFY_HOSTOUTPUT")
long_host_output = os.environ.get("NOTIFY_LONGHOSTOUTPUT")
service_problem_id = os.environ.get("NOTIFY_SERVICEPROBLEMID")
host_problem_id = os.environ.get("NOTIFY_HOSTPROBLEMID")
host_or_service = os.environ.get("NOTIFY_WHAT")

print(hostname, service_output)

match host_or_service:
	case "SERVICE":
		if long_service_output:
			notification_data = {	
				"monitoringInfo" : {
					"monitoringObjectHostname" : hostname,
					"monitoringObjectSource" : "CheckMK",
					"monitoringObjectAlertDescription" : service_output,
					"monitoringObjectAlertFullDescription" : long_service_output,
					}
				}
		else:
			notification_data = {   
                                "monitoringInfo" : {
                                        "monitoringObjectHostname" : hostname,
                                        "monitoringObjectSource" : "CheckMK",
                                        "monitoringObjectAlertDescription" : service_output,
                                        }
                                }

		file_name =f"{current_timestamp}_{service_problem_id}"

	case "HOST":
		if long_host_output:
			notification_data = {   
                        	"monitoringInfo" : {
                                	"monitoringObjectHostname" : hostname,
                                	"monitoringObjectSource" : "CheckMK",
                                	"monitoringObjectAlertDescription" : host_output,
					"monitoringObjectAlertFullDescription" : long_host_output,
                                	}
                        	}
		else:
			notification_data = {   
                                "monitoringInfo" : {
                                        "monitoringObjectHostname" : hostname,
                                        "monitoringObjectSource" : "CheckMK",
                                        "monitoringObjectAlertDescription" : host_output,
                                        }
                                }

		file_name =f"{current_timestamp}_{host_problem_id}"


json_string = json.dumps(notification_data, indent=4)

file_path = f"/omd/sites/master/tmp/{file_name}.log"

with open(file_path, "w") as file:
	file.write(json_string)

print(f"Notification data written to file: {file_path}")
