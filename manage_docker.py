import os
from time import sleep
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
console = Console()


def yprint(string):
	console.print(Text(string,style="bold yellow"))

def rprint(string): 
	console.print(Text(string,style="bold red"))
	
def gprint(string): 
	console.print(Text(string,style="bold green"))

def wait_status(string):
	gprint("\tWait.......................................")
	sleep(2)
	yprint(string)
	
def status_container():
	cmd = os.popen("docker ps").read()
	yprint(cmd)
	
def image_docker():
	l = os.popen("docker images").read()
	img_name = input("\tEnter image name:	")
	with console.status("[bold green]\tWorking on tasks...") as status:
		l = os.popen("docker pull "+img_name).read()
		print(l)
		wait_status("\tTask Completed!!!")
		
def run_container():
	img_name = input("\tEnter image name:	") 
	c_name = input("\tEnter the name to be given to container:	")
	os.popen(f"docker run -it --name {c_name} {img_name}")
	yprint("\tContainer is running")

def delete_container():
	status_container()
	c_name = input("\tEnter the container to be deleted:	")
	os.popen(f"docker stop {c_name}").read()
	wait_status("\tDocker Deleted!!!")
	
def network_details():
	cmd = os.popen("docker network ls").read()
	yprint(cmd)

def add_bridge():
	b_name = input("\t\tEnter the bridge name:	")
	os.popen(f"docker network create -d bridge {b_name}").read()
	wait_status("\t\t Bridge Added!!!")
	
def delete_bridge():
	b_name = input("\t\tEnter the bridge to be deleted:	")
	os.popen(f"docker network rm {b_name}").read()
	wait_status("\t\t Bridge deleted!!!")
	
def connect_bridge():
	status_container()
	c_name = input("\t\tEnter the container name:	")
	b_name = input("\t\tEnter the bridge name:	")
	os.popen(f"docker network connect {b_name} {c_name}").read()
	wait_status("\t\t Bridge Connected!!!")
	
def show_connection_bridge():
	b_name = input("\t\tEnter the bridge name:	")
	cmd = os.popen(f"docker network inspect {b_name}").read()
	yprint("---------------------------------------------------------------")
	yprint(cmd)
	yprint("---------------------------------------------------------------")
	
def disconnect_bridge():
	c_name = input("\t\tEnter the container name:	")
	b_name = input("\t\tEnter the bridge name:	")
	cmd = os.popen(f"docker network disconnect {b_name} {c_name}").read()
	wait_status("\t\t Bridge Disconnected!!!")
	
def modify_network():	
	while True:
		update_network_menu()
		ch = int(input("\t\t Enter the choice:	"))
		network_details()
		if ch == 1:	
			add_bridge()
		elif ch == 2:
			delete_bridge()
		elif ch == 3:
			connect_bridge()
		elif ch == 4:
			disconnect_bridge()
		elif ch == 5:
			show_connection_bridge()
		elif ch == 6:
			break
		else:
			rprint("\t\tWrong choice!!!")
			
def update_network_menu():
	gprint("\t\t1. Add new bridge")
	gprint("\t\t2. Delete bridge")
	gprint("\t\t3. Connect Application to bridge")
	gprint("\t\t4. Disconnect Application from bridge")
	gprint("\t\t5. Show the connection from bidge to App")	
	rprint("\t\t6. Exit")
	
def menu():
	gprint("1. Status of containers")
	gprint("2. Download new Image")
	gprint("3. Run container")
	gprint("4. Delete Container")
	gprint("5. Network details of container")
	gprint("6. Modify Network details of contaniner")
	rprint("7. Exit")
	
while True:
	menu()
	ch = Prompt.ask("Enter your option ", choices=["1", "2", "3","4","5","6","7"])
	if ch == "1":
		status_container()
	elif ch == "2":
		image_docker()
	elif ch == "3":
		run_container()
	elif ch == "4":
		delete_container()
	elif ch == "5":
		network_details()
	elif ch == "6":
		modify_network()
	elif ch == "7":
		break

