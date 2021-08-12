import getpass
import telnetlib
from time import sleep

# credential and telnet server info
HOST = "192.168.148.180"
user = 'teladmin'
password = 'telpwd'

tn = telnetlib.Telnet(HOST)
tn.set_debuglevel(100)

tn.read_until(b"Login: ", 3)
tn.write("teladmin".encode('ascii') + "\r\n".encode('ascii'))


tn.read_until(b"Password: ", 3)
tn.write("telpwd".encode('ascii') + "\r\n".encode('ascii'))


tn.write("read status o24".encode('ascii'))
tn.write("\r".encode('ascii'))

tn.write("quit".encode('ascii'))
tn.write("\r".encode('ascii'))

print(tn.read_all().decode('ascii'))

'''

# default username: teladmin
# default password: telpwd

# read status scoket 24
# read status o24

sample output:
> read status o01
 Outlet 01 on

> read status o24
 Outlet 24 off

sw o24 on delay
sw o24 off delay



quit

# tn.write("\r".encode('ascii'))

# tn.write("vt100\n") 
# sleep(15)
# tn.write("read status o24".encode('ascii') + "\r".encode('ascii'))
# tn.write("\r".encode('ascii'))
# tn.write(0xFF)   
# tn.write(0xFB)  
# tn.write(0x01)   

# tn = telnetlib.Telnet(HOST)

# user = input("Enter your remote account: ")
# password = getpass.getpass()

'''