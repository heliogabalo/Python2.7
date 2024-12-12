#!/usr/bin/env python

#/*
# * gitInit.py
# * This file is part of libtool-izator-starter?
# *
# * Copyright (C) 2024 - Raul Vilchez Ruiz
# *
# * libtool-izator-starter is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * libtool-izator-starter is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with <program name>. If not, see <http://www.gnu.org/licenses/>.
# */

import subproces
import os
import shutil


def initialize_git_repo(directory):
	try:
		# Run 'git init' in the specified directory
		subproces.run(["git","init"], cwd=directory, check=True)
		print("Initialized empty Git repository in {directory}")
	except subproces.CalledProcessError as e:
		print("Error Initializing Git repository: {e}")

def remove_directory(directory):
	'''Remove /tmp/example if it exist'''
	try:
		shutil.rmtree("/tmp/example", check=True)
		print("Directory: {directory} had been removed.")
	except subproces.CalledProcessError as e:
		print("Error removing directory: {e}")
		
def copy_directory(directory):
	'''Copy /tmp/exampleA to /tmp/exampleB'''
	try:
		shutil.copy("/tmp/exampleA", "/tmp/exampleB", exist_ok=True, check=True)
		print("Directory: {directory} had been copied.")
	except subproces.CalledProcessError as e:
		print("Error copying directory: {e}")

def create_directory(directory):
	'''Create directories /tmp/example/dirA
		 and /tmp/example/dirB.
		 TODO:
		 	implement a extended prototype(sobrecarga)
		 	with 2, 3 or more args.
	'''
	try:
		os.makedirs("/tmp/example/dirA", exist_ok=True, check=True)
		print("Directory: {directory} had been created.")
	except subproces.CalledProcessError as e:
		print("Error creating directory: {e}")

def change_to_dir(directory):
	'''Change directory to /tmp'''
	try:
		os.chdir("/tmp")
		print("{directory}")
	except:
		pass


#	# Change directory to /tmp
#	os.chdir("/tmp")

#	# Remove /tmp/example if it exist
#	shutil.rmtree("/tmp/example", ignore_errors=True)

#	# Create directories /tmp/example/dirA and /tmp/example/dirB
#	os.makedirs("/tmp/example/dirA", exist_ok=True)
#	os.makedirs("/tmp/example/dirB", exist_ok=True)

#	# Copy /tmp/exampleA to /tmp/exampleB
#	shutil.copy("/tmp/exampleA", "/tmp/exampleB")









# Example usage
initialize_git_repo("/path/to/project")
