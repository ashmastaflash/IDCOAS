#!/usr/bin/python
# This script will consume a config file with the following settings:
# Source: Machine IP address
# Destination: Syslog server
# Danger: Interesting pathogen
# Noise: Common pathogens
# Frequency: Messages per second
import getopt
import os.path
import re
import sys
import time
import random
import logging
import logging.handlers

def main(argv):
    # set vars
    help_text = ( "This script only accepts one argument:  -c CONFIGFILE \n"
    "The config file should contain the following: \n"
    "source='' \n"
    "destination=''\n"
    "danger=''\n"
    "noise=''\n"
    "frequency=''\n"
    "snr=''\n"
    "---------------\n"
    "The variables have the following significance:\n"
    "source: This is the source IP of the simulated detection device\n"
    "destination: This is the IP address of the syslog server\n"
    "danger: This is the name of the dangerous pathogen\n"
    "noise: This is a comma-separated list of common pathogens.\n"
    "       Example: 'disease1,disease2,disease3'\n"
    "frequency: This is a number between 1 and 10 and represents how many\n"
    "       messages will be sent every second\n"
    "snr: Signal-to-noise ratio.  This is how many dangerous pathogen messages will occur per second"
    "      Another way to look at this variable is, \"How many noise messages for every danger message?\"\n")
    configfile = ''
    config_sanity = False
    # get config file from args
    try:
        opts,args = getopt.getopt(argv, "c:",[])
    except getopt.GetoptError:
        print help_text
        sys.exit(2)
    for o,a in opts:
        if o == '-c':
            print "CONFIG FILE: ",a
            configfile = a
    # sanity check
    config_sanity , configitems = configfile_is_sane(configfile)
    if not config_sanity:
        print "Insane in the membrane.  Check yer config, yo"
        sys.exit(2)
    else:
        pass
    # set up the logging object
    setup_logger(configitems['destination'])
    # now we get down to the reason we're here
    # we'll do a while true with a timer in it
    while True:
        fire_message_batch(configitems,configfile)
        time.sleep(10)

def send_message(src,pathogen):
    logstring = "Source="+src+" | Pathogen="+pathogen
    logging.info(logstring)

def setup_logger(dst):
    global rootLogger
    rootLogger = logging.getLogger('')
    rootLogger.setLevel(logging.DEBUG)
    socketHandler = logging.handlers.SysLogHandler(address=(dst,514))
    rootLogger.addHandler(socketHandler)
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def fire_message_batch(configitems,configfile):
    # set vars
    src = configitems['source']
    hot = configitems['danger']
    cld = configitems['noise'].split(',')
    num = int(configitems['frequency'])
    snr = int(configitems['snr'])
    nsr = (num-snr)
    print "Config file: "+configfile
    print "Number of commons to send: "+str(nsr)
    print "Number of uncommons to send: "+str(snr)
    # puke out the noise
    for x in range(0,nsr):
        pathogen = random.choice(cld)
        send_message(src,pathogen)
    #puke out the hot stuff
    for x in range(0,snr):
        pathogen = hot
        send_message(src,pathogen)
    return

def configfile_is_sane(configfile):
    conf_items = {}
    must_haves = ['source','destination','danger','noise','frequency','snr']
    ip_regex = '^(((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([0-9]{1,2}))\.){3}((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([0-9]{1,2}))$'
    # does the damn thing exist anyway?
    if not os.path.isfile(configfile):
        print "Invalid file handle.\n Check permissions and file name\n"
        return(False,'')
    with open(configfile) as f:
        contentlines = f.readlines()
    # set our regexes and variable names
    rxmatches = { 'source' : ip_regex ,
                 'destination' : ip_regex ,               # see ip_regex above,
                 'danger' : '^[A-Za-z0-9._-]{1,50}$',   # up to 50 chars
                 'noise' : '^[A-Za-z0-9.,_-]{1,500}$',   # up to 500 chars
                 'frequency' : '^(100|\d{1,2})$',       # up to 100
                 'snr' : '^(1000|\d{1,3})$'}            #up to 1000
    for line in contentlines:
        if '\#' in line:
            continue
        parts = line.rstrip().split('=',2)
        if len(parts) < 2:
            continue
        subject = parts[0].strip('\' ')
        predicate = parts[1].strip()
        rxtest = ''
        try:
            rxtest = re.compile(rxmatches[subject])
            if not rxtest.match(predicate):
                print "Failed sanity check: ", line
                print "String: " , predicate
                return(False,'')
            else:
                conf_items[subject] = predicate
                print "Setting ",subject," to ",predicate
        except:
            pass
    print conf_items
    for item in must_haves:
        if not conf_items.has_key(item):
            print "Failed to find key: ",item
            return(False,'')
        else:
            pass
    f.close()
    return(True,conf_items)






if __name__ == "__main__":
    main(sys.argv[1:])
