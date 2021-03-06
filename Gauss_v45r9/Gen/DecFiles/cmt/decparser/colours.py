#--------------------------------------
# Class holding colours for printing coloured text to terminal and printing functions, also handles the general log
# Written by Tomas Pilar, t.pilar@warwick.ac.uk
# March 2011
#--------------------------------------

import settings, os

#settings imported from the settings file
logfile=settings.logfile

#handle the log filename
if not settings.overwrite:
    if os.path.exists(logfile):
        for i in range(10000):
            if not os.path.exists(logfile+"."+str(i)):
                logfile=logfile+"."+str(i)
                break

#open the log
log=open(logfile,'w')
failed = False

#--------------------------------------
# Class holding colours for printing coloured text to terminal
#--------------------------------------

class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def enable(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'

if not settings.enable_colours:
    bcolours.disable()

#--------------------------------------
# Text Functions
#--------------------------------------


def query(string):

#print a query, wait, at the end of the dots for either fail() or done()

    string = str(string) + (60 - len(str(string)))*"."
    print string,

    #try to log it
    try:
        log.write(string)
    except:
        pass

    failed = False

def openlog():

# open the logfile manually again after it has been closed

    globals()["log"]=open(logfile,'a')
    query("Opening logfile <"+logfile+">")
    done()

query("Opening logfile <"+logfile+"> and loading colours")

def mesg(string):

# Simple announcing information debug function, in white

    string=str(string)
    print string
    log.write(string+"\n")

def stop(string):

#Most serious error announcing function, in red

    string=str(string)
    print bcolours.FAIL+string+bcolours.ENDC
            #log it
    log.write(string+"\n")

def done():

# Prints DONE in green letters - to be used in conjunction with query() above

    print bcolours.OKGREEN+"DONE"+bcolours.ENDC

    #try to log it
    try:
        log.write("DONE\n")
    except:
        pass


def fail(list):

# Prints FAIL in red letters and follows with debug information if they were passed in the list[strings] as an argument, to be used in conjunction with query() above

    print bcolours.FAIL+"FAIL"+bcolours.ENDC
    log.write("FAIL\n")

    #print the debug info
    if list != []:
        print bcolours.WARNING+"Printing debug info:\n"

        #log it
        log.write("Debug info:\n")
        for foo in list:
            print foo
            log.write(str(foo)+"\n")
        print bcolours.ENDC

def warning(string):

# Prints a yellow warning string that is passed as the argument, moderate problem

    string=str(string)
    #print if runlevel is 1 or higher
    print bcolours.WARNING+string+bcolours.ENDC
    log.write(string+"\n")

def closeLog():

#closes log after it's been opened manually

    log.close()

done()
