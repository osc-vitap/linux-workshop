#!/usr/bin/python3

import csv
import os

def main():
	reg_no = input("Enter your registration number: ")
	password = input("Enter your password (last 4 digits of your registration number): ")

	with open("registrations.csv", "r") as f:
			reader = csv.reader(f)
			for row in reader:
					if row[0] == reg_no and row[0][-4:] == password: 
							print("Welcome!")
							print("You will now be transferred to your own Linux Virtual Machine")
							input("Press Enter to continue...")
							os.system("docker run -it ghcr.io/osc-vitap/linux-event-vm:latest /bin/bash")
							break
			else:
					print("Invalid credentials!") 
			
			main()

def exitProtection():
	try:
		main()
	
	except KeyboardInterrupt:
		print("\nNice try, but you can't escape the program that easily!")
		exitProtection()
	
	except EOFError:
			print("\nIf you are facing any issues, please close the cmd/terminal and connect to server again.")
			print("Or call the event coordinators for help.")
			exitProtection()

if __name__ == "__main__":
	exitProtection()