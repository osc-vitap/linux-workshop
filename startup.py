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
							os.system("docker run -it linux-event-test:latest /bin/bash")
							break
			else:
					print("Invalid credentials!") 

def exitProtection():
	try:
		main()
	
	except KeyboardInterrupt:
		print("\nNice try, but you can't escape the program that easily!")
		exitProtection()
	
	except EOFError:
		print("\nDamn, but not today.")
		exitProtection()

if __name__ == "__main__":
	exitProtection()