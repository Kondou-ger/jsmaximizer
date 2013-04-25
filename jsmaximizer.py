#!/usr/bin/python3
#encoding: utf-8

import sys
import argparse
import re

def main(argv):
	"""
	Parse our arguments
	"""

	parser = argparse.ArgumentParser(description="JS-Maximizer \nMaximize minimized JS, so it's easier to analyze.")
	parser.add_argument("Input", type=str, help="File to maximize")

	minfilename = parser.parse_args().Input
	maxfilename = parser.parse_args().Input + ".max.js"
	

	minfile = open(minfilename, 'r')
	maxfile = open(maxfilename, 'w')

	mincontent = minfile.read()

	lastseperator = 0
	indentation = 0

	for fileline in [fileline.start() for fileline in re.finditer(";|{|}", mincontent)]:
		maxfile.write("\t"*indentation + mincontent[lastseperator:fileline] + "\n")

		if "{" in mincontent[lastseperator:fileline+1]:
			indentation += 1
		elif ("}" in mincontent[lastseperator:fileline+1]) and (indentation > 0):
			indentation -= 1

		lastseperator = fileline+1
	
	maxfile.write(mincontent[lastseperator:])

	minfile.close()
	maxfile.close()

if __name__ == "__main__":
	main(sys.argv[1:])
