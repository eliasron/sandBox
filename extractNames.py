#!/usr/bin/python
import os,sys
import time
import urllib2

def readFile(url):

    if '?' in url:
        url.replace('?','\\?')
    #
    r=urllib2.urlopen(url)
    return r


def extractAdress(url):

    emailAdresses=[]
    r=readFile(url)
    for line in r:
        if ':' in line:
            words=line.split(':')
            if '@' in words[-1]:
                if not words[-1] in emailAdresses:
                    emailAdresses.append(words[-1].replace('\n',''))
                #
            #
    return emailAdresses


if __name__=='__main__':
    

    if len(sys.argv)==1:
        print 'please provide a url within quotation marks'
        sys.exit()
    #
    #
    url=sys.argv[1]
    adresses=extractAdress(url)

    print '------------------'
    print 'email adresses in column'
    print '------------------'
    for ad in adresses:
        print ad+','
    #
    print 
    print
    #
    print '------------------'
    print 'email adresses in line'
    print '------------------'
    line=''
    for ad in adresses:
        line+=ad+','
    print line

    
