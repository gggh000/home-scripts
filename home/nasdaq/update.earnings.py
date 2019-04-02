#!/virtualenv/bin/python
#!c:\python27\python.exe

import os
import time 
import re
import datetime
import collections
import random
#from collections import OrderedDict
global threadStatus 
threadStatus = []
threadStatus = 1000 * [0]

#

def getHttpStockSymbol(pThreadIdx, pSymbol):
    debug = 1
    global threadStatus
    global threadReturns
    print "------------------------------"
    print "getHttp... entered: pThreadIdx: ", pThreadIdx, ", pSymbol: ", pSymbol
    os.system("rm -rf " + pSymbol)
    os.system("nohup wget http://www.nasdaq.com/earnings/report/" + pSymbol.split('-')[0])

    print "thread: ", pThreadIdx, "is done."

    i = ""
    # Loop initialization. These initializations should not be moved out of loop!!!

    # The symbol entry for current iteration will be in <companyname>-<industry> format. 
    # Split and get the company name/stock symbol.

    symbol = pSymbol.split('-')[0]

    # Determine the industry, if error, set the industry to dash '-'.

    try:
        industry = i1.split('-')[1]
    except Exception as msg:
        industry = '-'

    # Determine the date now.

    date = None
    dateBeforeAfter = None
    line = ""

    # remove the file named after symbol and fetch from http again for updated one.
        
    #os.system("rm -rf " + symbol)
    #os.system("wget http://www.nasdaq.com/earnings/report/" + symbol)

    if not CONFIG_TEST_MODE:
        print "Sleeping randomly.."
        time.sleep(random.randrange(2, 10))

    # Extract the line containing "is expected" phrase which likely to contain the date and before/after info.

    cmd = "cat " + symbol + " | grep -i \"is expected\""
    print "cmd: ", cmd
    announce=os.popen(cmd).read().split(' ')

    if debugL2:
        print '-----------------------------------------------------------'
        print announce
        print '-----------------------------------------------------------'
    
    # Look fo a date in the line and set the date.

    for j in range(0, len(announce)):
        if re.search(".*/.*/.*", announce[j]):
            date = re.sub('/','-',announce[j])
            print "I believe I found a date: " + announce[j]

            # Look for before or after word in the line and set dateBeforeAfter flag. 
            # The word is right after the date.    

            if re.search("after|before", announce[j+1], re.IGNORECASE):
                print "I believe I found whether the earnings will be before or after the market open or close. :p "
                dateBeforeAfter = announce[j+1]
                print dateBeforeAfter
                break
    
    if date==None: 
        print "I did not found a date. Probably did not publish the earning date."

    if dateBeforeAfter == None:
        print "I don't believe I found whether the earnings will be before and after the market open or close. :("

    for i in ([date, dateBeforeAfter]):
        if i == None:
            i = '--'
        line += i + ","
    line += symbol + ',' + industry

    print "line now: ", line
    threadReturns[pThreadIdx % CONFIG_CONCURRENT_THREADS] = line

    try:
        threadStatus[pThreadIdx] = 1
    except Exception as msg:
        print "FATAL ERROR: Can not set threadStatus with pThreadIdx: ", pThreadIdx
        print threadStatus
    return 

#   Sort the company list file. Read the file content and close it. After that sort it and overwrite it back to same file.
#   Company list file is a simple text file with each line containing either of following format:
#   <company_name>
#   <company_name>-<industry>
#   
#   Result is same file is sorted after calling this function.
#   input: 
#   - None.
#   output:
#   - Sorted list of company in <list> format.

def sortList():
	fp = open("list.log", 'r')
	data = sorted(fp.read().split())
	fp.close()

	fp = open("list.log", 'w')

	for i in data:
		fp.write(i + '\n')

	fp.close()
	return data 

print "Program entry."
print "Sorting first"

companyEntries = sortList()

#   Initialize threadStatus list, each entry represents the threadstatus.
#   Initial value = 0 thread is not run.
#   value = 1 indicates thread is finished, when all list members are 1, all threads are ran
#   meaning synchronization is done.

threadStatus = len(companyEntries) * [0]
print "threaStatus: ", threadStatus

#   Configuration variables.

CONFIG_TEST_MODE = 1
CONFIG_CONCURRENT_THREADS = 50

#   Initialization of variables. 

dateDelim = "-|/"
fpOut = None
debug = 1
debugL2 = 0
date = None
dateBeforeAfter = None 
print "Fetching company earning date-s..."
line = ""
industry = None
global threadReturns
threadReturns = []

fNameOut = 'earnings.csv'
fpOut = open(fNameOut, 'w')

#   Now with the file is opened for writing, the fpOut will be a csv file with updated earnings date populated after this loop.
#   However earnings.csv contains the date-unsorted populated earnings information.

#   Using concurrent threads, we will process 5 symbol at a time.

for i0 in range(0, len(companyEntries), CONFIG_CONCURRENT_THREADS):
    i1 = companyEntries[i0:i0+CONFIG_CONCURRENT_THREADS]

    if len(i1) != CONFIG_CONCURRENT_THREADS:
        CONFIG_CONCURRENT_THREADS = len(i1)

    threadReturns = CONFIG_CONCURRENT_THREADS * [""]
    print "Processing threads", i0, " through ", i0+CONFIG_CONCURRENT_THREADS-1
    print i1

    for i2 in i1:
        print "=============================="
        print "starting thread for ", i2

        # Launch thread name, the threadId is the index of current entry in companyEntries master list.

        getHttpStockSymbol(companyEntries.index(i2), i2)
        
    while sum(threadStatus[i0:i0+CONFIG_CONCURRENT_THREADS]) < CONFIG_CONCURRENT_THREADS:
        os.system("clear")
        print "threads ", i0, " through ", i0+CONFIG_CONCURRENT_THREADS, " are not finished running."
        print threadStatus[i0:i0+CONFIG_CONCURRENT_THREADS]
        time.sleep(3)

    print "threads ", i0, " through ", i0+CONFIG_CONCURRENT_THREADS-1, " are finished running."
    
    # if date or dateBeforeAfter is None set to '--' signifying it can not be determined.
    # Construct a line in the format <date>,<beforeAfterFlag>,<symbol>,<industry> and write to output file: earnings.csv.

    line = '\n'.join(threadReturns)
    line += '\n'
    print "Recording to file now: "
    print line
    print "============================="
    fpOut.write(line)
    
fpOut.close()

os.system('cat ' + fNameOut)

#   Perform a sort now.

fpOut=open(fNameOut, 'r')

content = []

#   DateNow is today's date. It can be used later for enhancement.

dateNow = datetime.datetime.now().date()
print "date now: ", dateNow

#   Two dictionary format: dictReadBack will contain the list of company whose earning dates are known.
#   dictReadBackNoDate will contain whose earnings date can not be determined.

dictReadBack = {}
dictReadBackNoDate = {}

counterNoDate = 0

while 1:
    if debugL2:
        print '------------------------------------'

    # Read one line at a time, remove the new line. 
    # Once read is finished, break out of loop.
    # content var is all the lines in list format.
    
    line = re.sub('\n','', fpOut.readline()).strip()
    
    if not line:
        print "done reading."
        break
        
    content.append(line)

    if debugL2:
        print "line: ", line 

    # Extract the date field of each line.

    lineDate = str(re.sub('-','',line.split(',')[0])).strip()

    #If date is just -, then it means, date was not obtained after last reading.

    if lineDate:
        if debugL2:
            print "lineDate: ", lineDate, type(lineDate), len(lineDate)

        # Construct datetime object using the date extracted from each line.

        lineDateObj = datetime.datetime.strptime(str(lineDate), "%m%d%Y").date()

        if debugL2:
            print lineDateObj

        # Since the datetime is a key and there could be a duplicate keys and python does not support it.
        # we maintain single key but values will be a list. If list was not created, then create new one,
        # otherwise append to list. 

        if lineDateObj in dictReadBack:
            
            dictReadBack[lineDateObj].append(line)
        else:
            dictReadBack[lineDateObj] = [line]
            
    else:
        
        # If no date is set, then we append to simple counter-keyed dictionary.

        if debugL2:
            print "No date."
        counterNoDate += 1
        dictReadBackNoDate[counterNoDate] = line

if debugL2:
    print "Readback with dates: "

    for i in range(0, len(dictReadBack)):
        if debugL2:
            print '-------'
            print dictReadBack.keys()[i], ", ", dictReadBack.values()[i]
    
    for i in range(0, len(dictReadBackNoDate)):
        if debugL2:
            print '-------'
            print dictReadBackNoDate.keys()[i], ", ", dictReadBackNoDate.values()[i]
    
if debugL2:
    print "sorted: ", sorted(dictReadBack.keys())
    print "sorted: ", sorted(dictReadBackNoDate.keys())

#   Start doing the heavy lifting of sorting here, use a OrderedDict to hold the sorted dates.

dictReadBackSorted = collections.OrderedDict()

#   Get the keys and sort it immediately and assign to Ordered dict.

for i in sorted(dictReadBack.keys()):
    dictReadBackSorted[i] = dictReadBack[i]

print "Sorted: "

if debugL2:
    for i in range(0, len(dictReadBackSorted)):
        print dictReadBackSorted.keys()[i], ": ", \
        	dictReadBackSorted.values()[i]

#   Open file to save the sorted list.

fNameOutSorted = "earnings.sorted.csv"
fpOutSorted = open(fNameOutSorted, 'w')
fpHtmlSorted = open("/home/pxeboot/earnings.html", 'w')

if not fpOutSorted:
    print "Err: can not open for writing: ", fNameOutSorted
    quit(1)

if not fpHtmlSorted:
    print "Err: can not open for writing: ", fpHtmlSorted
else:
    fpHtmlSorted.write('<!DOCTYPE html>\n')
    fpHtmlSorted.write('<html>\n')
    fpHtmlSorted.write('<head>\n')
    fpHtmlSorted.write('EANINGS LIST FROM NASDAQ.COM\n')
    fpHtmlSorted.write('</head>\n')
    fpHtmlSorted.write('<body>\n')
    fpHtmlSorted.write('<p>LAST UPDATED: ' + str(os.popen('date').read())+ '</p>\n')

#   Start writing the sorted list from Ordered dictionary.

for i in range(0, len(dictReadBackSorted)):
    print dictReadBackSorted.keys()[i], ": "

    for j in dictReadBackSorted.values()[i]:
        print j

    print '-----------------------------'
    fpOutSorted.write('------------------\n')

    if fpHtmlSorted:
        fpHtmlSorted.write('<p>------------------</p>\n')

    for j in dictReadBackSorted.values()[i]:
        fpOutSorted.write(j + '\n')

        if fpHtmlSorted:
            fpHtmlSorted.write('<p>' + j + '</p>\n')
    
# 	Also write the unsorted companies at the end of file.

for i in dictReadBackNoDate.values():
    fpOutSorted.write('<p>' + i + '</p>\n')

    if fpHtmlSorted:
        fpHtmlSorted.write('<p>' + i + '</p>\n')

fpOutSorted.close()

fpHtmlSorted.write('</body>\n')
fpHtmlSorted.write('</html>\n')
fpHtmlSorted.close()

#   Remove the residual files.

for i1 in companyEntries:
    i = ""

    # Loop initialization. These initializations should not be moved out of loop!!!

    symbol = i1.split('-')[0]
    os.system("rm -rf " + symbol)
