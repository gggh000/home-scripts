#c:\python27\python.exe
import os
import datetime
import re
import sys
import time
#import exception 

ARG_LIST = "--list"
ARG_SLEEP = "--sleep"
ARG_DELETE_INTER = "--delete-inter"
ARG_DELETE_SRC = "--delete-src"
ARG_NO_DELETE_INTER = "--no-delete-inter"
ARG_NO_DELETE_SRC = "--no-delete-src"
explicitFilesToConvert = []
cmdLineArgs = {ARG_LIST: None, ARG_SLEEP: None, ARG_DELETE_INTER: None, ARG_DELETE_SRC: None, ARG_NO_DELETE_INTER: None, ARG_NO_DELETE_SRC: None}

CONFIG_DEFAULT_DELETE_INTER = None
CONFIG_DEFAULT_DELETE_SRC = None

# Set default values. 

cmdLineArgs[ARG_DELETE_INTER] = CONFIG_DEFAULT_DELETE_INTER
cmdLineArgs[ARG_DELETE_SRC] = 	CONFIG_DEFAULT_DELETE_SRC

sleepTime = 3

def	printHelp():
	os.system("cls")
	print "==========================================================================="
	print sys.argv[0].upper().split('\\')[-1], " utility."
	print "==========================================================================="
	print "USAGE: "
	print "--help for this help."
	print "--sleep <INT> to specify wait time before starting conversion"
	print "--list <fileName1> <fileName2> ... <fileName<N-1>>, <fileName<N>> to explicitly specify list of files to be converted."
	print "Note: Currently no validation is made for the files' existence, if the list of files contains file does not exist"
	print "behavior is unpredictable, no error-checking. "
	print "--delete-inter for deleting all intermediate, converted files that area created before concatenating to generate the last one."
	print "--delete-src for deleting all source files"
	print "--no-delete-inter for force NOT deleting all intermediate, converted files that area created before concatenating to generate the last one."
	print "--no-delete-src for force NOT deleting all source files"
	print "==========================================================================="
	
# Process all command line arg-s here.

try:
	if sys.argv[1] == "--help":
		printHelp()
		quit(0)
except Exception as msg:
		print ""

for i in range(0, len(sys.argv)):
	if re.search(ARG_DELETE_INTER, sys.argv[i]):
		cmdLineArgs[ARG_DELETE_INTER] = 2
	if re.search(ARG_DELETE_SRC, sys.argv[i]):
		cmdLineArgs[ARG_DELETE_SRC] = 2
	
	if re.search(ARG_NO_DELETE_INTER, sys.argv[i]):
		cmdLineArgs[ARG_NO_DELETE_INTER] = 2
	if re.search(ARG_NO_DELETE_SRC, sys.argv[i]):
		cmdLineArgs[ARG_NO_DELETE_SRC] = 2
		
if 	cmdLineArgs[ARG_NO_DELETE_SRC] == 2 and cmdLineArgs[ARG_DELETE_SRC] == 2:
	print "You can specify both of ", ARG_NO_DELETE_SRC, " and ", ARG_DELETE_SRC
	quit(1)

if 	cmdLineArgs[ARG_NO_DELETE_INTER] == 2 and cmdLineArgs[ARG_DELETE_INTER] == 2:
	print "You can specify both of ", ARG_NO_INTER_SRC, " and ", ARG_INTER_SRC
	quit(1)
	
if cmdLineArgs[ARG_NO_DELETE_SRC]:
	cmdLineArgs[ARG_DELETE_SRC] = None
	
if cmdLineArgs[ARG_NO_DELETE_INTER]:
	cmdLineArgs[ARG_DELETE_INTER] = None


for i in range(0, len(sys.argv)):
	# Process list of files to convert and concatenate.
	
	if sys.argv[i] == ARG_LIST:
	
		# Do all sort of error checking here:
		
		try:
			if re.search("^--",sys.argv[i+1]):
				print "Error: --list argument should be followed by list of files to be converted, found: ", sys.argv[i+1] 
				quit(1)
		except Exception as msg:
				print "Error: --list argument should be followed by list of files to be converted, found nothing after --list" 
				quit(1)
		
		# Explicit list of file to be converted. Process 'em here. 
		
		print "Will build explicit list of files to be converted rather than entire directory content."
			
		# Gather the list of files until it meets any cmdline switch: --<SWITCH_NAME>
		
		for j in range(i+1, len(sys.argv)):
			if not re.search("^--", sys.argv[j]):
				print "adding" , sys.argv[j], " to a list of explicit files to be converted."
				explicitFilesToConvert.append(sys.argv[j])
			else:
				break
				
		cmdLineArgs[ARG_LIST] = 1								

for i in range(0, len(sys.argv)):
	if sys.argv[i] == ARG_SLEEP:
		try:
			sleepTime = int(sys.argv[i+1])
		except Exception as msg:
			print "Error: --sleep must be followed by integer. "
			quit(1)
			
		cmdLineArgs[ARG_SLEEP] = 1
			
if not cmdLineArgs[ARG_SLEEP]:
	sleepTime = 3
	print "Sleeptime is defaulted to 3 seconds."

print  "sleeping for ", sleepTime, " seconds. "

time.sleep(sleepTime)

print "Finished sleeping. Starting conversaion."

outputFileExtension=".flv"

supportedOutputFormats = ['mpg','flv','mp4']

print str(len(sys.argv))

if len(sys.argv) >= 2:
	if sys.argv[1] in supportedOutputFormats:
		outputFileExtension = "." + sys.argv[1]
		print "outputFileExtension set to : " + outputFileExtension
	else:
		print "outputFileExtension specified is not supported. Will use default: " + outputFileExtension
	
else:
		print "No outputFileExtension specified. Will use default: " + outputFileExtension
time.sleep(3)		
	
print os.getcwd()

if not cmdLineArgs[ARG_LIST]:
	files = os.listdir(os.getcwd())	
else:
	files = explicitFilesToConvert
	
print "No. of files to be converted: ", len(files)
print files
time.sleep(3)

#videoOption = "-s hd1080"
videoOption = "-s 3840x2160"
videoScale="-vf scale=1080:768"
counter = 0
outputList = []
command = ""
outputConcatFile=""
debug = 0

for i in files:
	if i[-3:] == "avi":
		print "converting to: " + i[:-4] + outputFileExtension
		outputName = "movie" + str(counter) + outputFileExtension
		command = "ffmpeg -i \"" + str(i) + "\" " + videoOption + " " + outputName
		#command = "ffmpeg -i \"" + str(i) + "\" " videoScale + " " + outputName
		outputList.append(outputName)		
		print "--------------------------"
		print "convert command: " + str(command)
		print "--------------------------"
		time.sleep(3)
		os.system(command)
		counter += 1
		
		if counter > 1 and debug:
			break
outputListFileName = "outputList.log"		
fp=open(outputListFileName, 'w+')

for i in outputList:
	fp.write('file \'' + i + '\'\n')
fp.close()	

outputConcatFile = re.sub(":", ".", str(datetime.datetime.now().isoformat()))
print "outputConcatFile: " + str(outputConcatFile)

command = "ffmpeg -f concat -i "+ str(outputListFileName) +" -c copy " + outputConcatFile + outputFileExtension
print "concatenation command: " + str(command)
os.system(command)


if cmdLineArgs[ARG_DELETE_INTER]:
	print "deleting intermediate files: " 

	for i in outputList:
		print "deleting: ", i
		os.system("del "+ i)
		
else:
	print "Leaving intermediate files untouched (not deleted)."
	
if cmdLineArgs[ARG_DELETE_SRC]:
	print "deleting source files: " 

	for i in files:
		print "deleting: ", i
		os.system("del \"" + str(i) + "\"")
else:
	print "Leaving intermediate files untouched (not deleted)."
	
	
	
