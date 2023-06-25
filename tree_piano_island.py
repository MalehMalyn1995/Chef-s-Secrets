# Importing the necessary packages and libraries
import os
import sys
import time
import random

# Defining a class for the Culinary School
class CulinarySchool():

	# Initializing the class
	def __init__(self):
		self.name = 'Culinary School'
		self.location = 'Location'
		self.programs = []

	# Function to display the name of the Culinary School
	def displayName(self):
		print('Welcome to the ' + self.name + '!')

	# Function to set the location of the Culinary School
	def setLocation(self, location):
		self.location = location

	# Function to add a program to the Culinary School
	def addProgram(self, program):
		self.programs.append(program)

	# Function to display the available programs at the Culinary School
	def displayPrograms(self):
		print('The following programs are offered at ' + self.name + ':')
		for program in self.programs:
			print(program)


# Defining a class for the Culinary Program
class CulinaryProgram():

	# Initializing the class
	def __init__(self, name, duration):
		self.name = name
		self.duration = duration

	# Function to display the name of the Culinary Program
	def displayName(self):
		print('Welcome to the ' + self.name + ' program!')
	
	# Function to display the duration of the Culinary Program
	def displayDuration(self):
		print('This program is ' + str(self.duration) + ' months long.')

	# Function to display the description of the Culinary Program
	def displayDescription(self):
		print('This program provides hands-on training for aspiring chefs who want to hone their culinary skills and expertise.')


# Defining the main function to execute the program
def main():

	# Creating an instance of the Culinary School
	culinarySchool = CulinarySchool()

	# Displaying the name of the Culinary School
	culinarySchool.displayName()

	# Setting the location of the Culinary School
	culinarySchool.setLocation('USA')

	# Creating a Culinary Program
	culinaryProgram = CulinaryProgram('Basic Culinary', 6)

	# Adding the Culinary Program to the Culinary School
	culinarySchool.addProgram(culinaryProgram)

	# Displaying the list of programs offered at the Culinary School
	culinarySchool.displayPrograms()

	# Displaying the name of the Culinary Program
	culinaryProgram.displayName()

	# Displaying the duration of the Culinary Program
	culinaryProgram.displayDuration()

	# Displaying the description of the Culinary Program
	culinaryProgram.displayDescription()


# Calling the main function
if __name__ == '__main__':
	main()