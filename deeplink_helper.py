#!/usr/bin/env python3
import subprocess
import re

def start_the_process():

	list_of_running_devices = running_devices()
	selected_device = ""

	if len(list_of_running_devices) > 1: 
		print("This are the devices that are running, please pick one:\n")

		# Iterate to be easier to user just select which one he want
		for idx, item in enumerate(list_of_running_devices):
			formated = str(idx) + " - " + item.lstrip()
			print(formated)

		choice = input("Which one: ")

		# We use REGEX to extract our identifier, still have some informations when extracted
		# below before use we need to get the first 'group' as we have another string extracted
		extracted_device_identifier = re.search(r'\((.*?)\)', list_of_running_devices[int(choice)])
		selected_device = extracted_device_identifier.group(1)
	else:
		extracted_device_identifier = re.search(r'\((.*?)\)', list_of_running_devices[0])
		device_name_selected = re.search(r'[^(]*', list_of_running_devices[0]).group(0).lstrip()
		print("\nSelected the only simulator running: " + device_name_selected)

	print("\nWhich deep link do you want to try:")
	# Ask for the deep link that you want 
	deep_link = input("Deep link: ")

	# Here we generate the final command to be called and open the simulator
	first_parameter = selected_device
	second_parameter = "\"{}\"".format(deep_link)
	command_to_open_at_simulator = "xcrun simctl openurl {} {}".format(first_parameter, second_parameter)

	status = subprocess.call(command_to_open_at_simulator,shell=True)

	# If something went wrong usually the deep link that you are using is not valid, you do not have the app
	# installed in order to get / try that deep link, or it have a bad format and can throw a error
	if status != 0:
		print("\nSomething went wrong, most probably your deep link is wrong or don't exist in your app please double check")
	else:
		print("\nSuccess check your simulator :D\n")


def running_devices():
	# Get the device's list that are running
	devicesStringList = subprocess.getoutput("xcrun simctl list | grep Booted")
	list_of_running_devices = devicesStringList.split("\n")
	filtered_list = list(filter(None,list_of_running_devices))

	return filtered_list

if __name__ == "__main__":
	if len(running_devices()) == 0:
		print("\nYou need to have at least one simulator running, please start and run again\n")
	else: 
		start_the_process()