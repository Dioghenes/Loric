#******************************************************
 # Dioghenes
 # Polytechnic of Turin 
 # 2016
 # pingsuite_pylib v0.2
#******************************************************

from socket import *
from os import getpid
from random import randint
from struct import pack


def ping(ipaddr,timeout=0.05,defPort=0):
	# This function returns:
	# 0 - Host connected
	# 1 - Network unreachable
	# 2 - Generic error
	# 3 - You must be root
	try:
		sock = socket(AF_INET,SOCK_RAW,1)
		sock.settimeout(timeout)
	except:
		return 3
	packetToSend = ICMPpacket()
	try:
		sock.connect((ipaddr,defPort))
		sock.sendto(packetToSend,(ipaddr,defPort))
	except error, msg:
		if "101" in str(msg):
			sock.close()
			return 1
		else:
			sock.close()
			return 2
	return 0


def ICMPpacket():
	# This is a basic implementation of ping function written in C
	# by the defense department of USA in the 80s. It allows to create 
	# ICMP packet.
	ptype = 8
	pcode = 0
	pchsum = 0
	pid = getpid()#*randint(0,2**16) % 2**16
	seq = 1
	data = "ICMP_request"
	primitiveHead = pack("BBHHH",ptype,pcode,pchsum,pid,seq)
	primitivePacket = primitiveHead+data
	pchsum = chksum(primitivePacket)
	ultimateHeader = pack("BBHHH",ptype,pcode,htons(pchsum),pid,seq)

	ultimatePacket = ultimateHeader+data
	return ultimatePacket

def chksum(primPacket):
	# This function creates a checksum value for the given packet
	count = 0
	chks = 0
	while count<len(primPacket):
		tmp = ord(primPacket[count+1])*256+ord(primPacket[count])
		chks = chks+tmp
		count += 2
	chks = (chks >> 16)+(chks & 0xffff)
	chks = chks + (chks >> 16)
	chks = ~chks
	chks = chks & 0xffff
	chks = chks >> 8 | (chks << 8 & 0xff00)
	return chks

def createIpRange(startIP,stopIP):
		# Only IPs in the range a.b.c.d - a.b.e.f are returned.
		# This means that only the last two fields of the IPs are used 
		# to create the list of IPs: in this way you'll get, at maximum,
		# 65536 IPs.
		# Return codes:
		# List of strings - All Ok
		# 1 - Bad start IP
		# 2 - Bad stop IP 
		# 3 - Bad IP tuple
		try:
			IP1 = inet_aton(startIP)
		except:
			return 1
		try:
			IP2 = inet_aton(stopIP)
		except:
			return 2
		startIP = startIP.split(".")
		stopIP = stopIP.split(".")
		if len(startIP)!=4 or len(stopIP)!=4:
			return 3
		for i in range(0,4):
			startIP[i] = int(startIP[i])
			stopIP[i] = int(stopIP[i])

		listOfIPs = []
		while startIP[2] <= stopIP[2]:
			if startIP[2] == stopIP[2]:
				while startIP[3] <= stopIP[3]:
					tmp = str(startIP[0])+"."+str(startIP[1])+"."+str(startIP[2])+"."+str(startIP[3])
					listOfIPs.append(tmp)
					startIP[3] += 1
			else:
				while startIP[3] <= 255:
					tmp = str(startIP[0])+"."+str(startIP[1])+"."+str(startIP[2])+"."+str(startIP[3])
					listOfIPs.append(tmp)
					startIP[3] += 1
				startIP[3] = 0
			startIP[2] += 1
		return listOfIPs
