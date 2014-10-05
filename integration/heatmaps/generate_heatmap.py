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
import pygeoip
import heatmap
import random

def main(argv):
    # set vars
    help_text = ( "This script only accepts one argument:  -c IPLISTFILE \n"
    "The IP list file should only contain IP addresses,one per line: \n"
    "---------------\n" )
    gip_file = './GeoLiteCity.dat'
    iplistfile = ''
    config_sanity = False
    # get ip file from args
    try:
        opts,args = getopt.getopt(argv, "i:",[])
    except getopt.GetoptError:
        print help_text
        sys.exit(2)
    for o,a in opts:
        if o == '-i':
            print "IP FILE: ",a
            iplistfile = a
    # sanity check
    config_sanity , iplist= ipfile_is_sane(iplistfile)
    if not config_sanity:
        print "Insane in the membrane.  Check yer ip file, yo"
        sys.exit(2)
    else:
        pass
    coords = build_coordlist(iplist,gip_file)
    #print coords
    kml_filename = iplistfile+'.kml'
    write_kml(coords,kml_filename)

def write_kml(coords,kml_filename):
    print kml_filename
    hm = heatmap.Heatmap()
    hm.heatmap(coords,scheme='classic',opacity=199)
    hm.saveKML(kml_filename)

def build_coordlist(iplist,gip_file):
    gic=pygeoip.GeoIP(gip_file)
    coordlist = []
    for ip in iplist:
        dataz = gic.record_by_addr(ip)
        lat = random.uniform(dataz['latitude']-0.5,dataz['latitude']+0.5)
        lon = random.uniform(dataz['longitude']-0.5,dataz['longitude']+0.5)
        latlon = (lon,lat)
        coordlist.append(latlon)
    coordtup = tuple(coordlist)
    return coordtup

def ipfile_is_sane(ipfile):
    ip_items = []
    ip_regex = '^(((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([0-9]{1,2}))\.){3}((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([0-9]{1,2}))$'
    # does the damn thing exist anyway?
    if not os.path.isfile(ipfile):
        print "Invalid file handle.\n Check permissions and file name\n"
        return(False,'')
    with open(ipfile) as f:
        contentlines = f.readlines()
    # set our regexes and variable names
    for line in contentlines:
        lineclean = line.rstrip()
        if '\#' in lineclean:
            continue
        rxtest = ''
        try:
            rxtest = re.compile(ip_regex)
            if not rxtest.match(lineclean):
                print "Failed sanity check: ", lineclean
            else:
                print lineclean
                ip_items.append(lineclean)
        except:
            pass
    f.close()
    return(True,ip_items)






if __name__ == "__main__":
    main(sys.argv[1:])
