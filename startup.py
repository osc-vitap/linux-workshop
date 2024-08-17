#!/usr/bin/python3

import csv
import os

def main():
	os.system("clear")
	ascii_banner = """

$$$$$$$\                                                                                              
$$  __$$\                                                                                             
$$ |  $$ | $$$$$$\        $$\   $$\  $$$$$$\  $$\   $$\        $$$$$$\ $$\    $$\  $$$$$$\  $$$$$$$\  
$$ |  $$ |$$  __$$\       $$ |  $$ |$$  __$$\ $$ |  $$ |      $$  __$$\\\\$$\  $$  |$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ /  $$ |      $$ |  $$ |$$ /  $$ |$$ |  $$ |      $$$$$$$$ |\$$\$$  / $$$$$$$$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$   ____| \$$$  /  $$   ____|$$ |  $$ |
$$$$$$$  |\$$$$$$  |      \$$$$$$$ |\$$$$$$  |\$$$$$$  |      \$$$$$$$\   \$  /   \$$$$$$$\ $$ |  $$ |
\_______/  \______/        \____$$ | \______/  \______/        \_______|   \_/     \_______|\__|  \__|
                          $$\   $$ |                                                                  
                          \$$$$$$  |                                                                  
                           \______/                                                                  
$$\ $$\                               $$$$\            +--------------------------------------------+                                              
$$ |\__|                             $$  $$\           + Welcome to the Linux Event!                +                                               
$$ |$$\ $$$$$$$\  $$\   $$\ $$\   $$\\\\__/$$ |          + Event by Open Source Community - VIT AP    +                                               
$$ |$$ |$$  __$$\ $$ |  $$ |\$$\ $$  |  $$  |          + Server provided by expanse.host            +                                                         
$$ |$$ |$$ |  $$ |$$ |  $$ | \$$$$  /  $$  /           +--------------------------------------------+                                               
$$ |$$ |$$ |  $$ |$$ |  $$ | $$  $$<   \__/                                                           
$$ |$$ |$$ |  $$ |\$$$$$$  |$$  /\$$\  $$\             Event Hosts:                                               
\__|\__|\__|  \__| \______/ \__/  \__| \__|            Bharath, Himanshu                                               
                                                                                                      
                                                                                                      
ASCII art by: patorjk.com                                                                                                      
"""

	print(ascii_banner)
	reg_no = input("Enter your registration number: ")
	password = input("Enter your password (last 4 digits of your registration number): ")

	with open("registrations.csv", "r") as f:
			reader = csv.reader(f)
			for row in reader:
					if row[0] == reg_no and row[0][-4:] == password:
							os.system("clear")
							print("Welcome!")
							print("You will now be transferred to your own Linux Virtual Machine")
							input("Press Enter to continue...")
							os.system("docker run -it ghcr.io/osc-vitap/linux-event-vm:latest /bin/bash")
							break
			else:
					print("Invalid credentials!")
					input("Press Enter to go to main menu...")
			
			main()

def exitProtection():
	try:
			main()
	
	except KeyboardInterrupt:
			exitProtection()
	
	except EOFError:
			exitProtection()

if __name__ == "__main__":
	exitProtection()