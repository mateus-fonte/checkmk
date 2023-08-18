from .agent_based_api.v1 import *

def discover_linux_net(section):
	yield Service()

def check_linux_net(section):
	interface_count = int(section[0][0])
	if interface_count >= 0 and interface_count < 2:
		yield Result(state=State.OK, summary=f"Normal number of network interfaces {interface_count}")
	elif interface_count >= 2 and interface_count <= 4:
		yield Result(state=State.WARN, summary=f"Alerting number of networks {interface_count}")
	elif interface_count > 4:
		yield Result(state=State.CRIT, summary=f"Dangerous number of network interfaces {interface_count}")

register.check_plugin(
	name = "network_interfaces",
	service_name = "Total number of network interfaces",
	discovery_function = discover_linux_net,
	check_function = check_linux_net,
) 
