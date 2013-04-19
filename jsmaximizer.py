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
		if "{" in mincontent[lastseperator:fileline+1]:
			maxfile.write("\t"*indentation + mincontent[lastseperator:fileline+1] + "\n")
			indentation += 1
		elif "}" in mincontent[lastseperator:fileline+1]:
			maxfile.write("\t"*indentation + mincontent[lastseperator:fileline] + "\n")
			if indentation != 0:
				indentation -= 1
			maxfile.write("\t"*indentation + mincontent[fileline:fileline+1] + "\n")
		else: # else it's a ;
			maxfile.write("\t"*indentation + mincontent[lastseperator:fileline] + "\n")

		lastseperator = fileline+1
	
	maxfile.write(mincontent[lastseperator:])

	minfile.close()
	maxfile.close()

if __name__ == "__main__":
	main(sys.argv[1:])
