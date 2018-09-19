# Lorica
A simple ping flood tester written in Python2.7

### Aim
This is a simple Python2.7 script that performs a ping flood attack on a network to test its availability under heavy loads. I don't take any responsibility of its usage. To make it work, just run is as root, then set the IP of the victim and finally answer Y to the question. The same ping packet will be sent as fast as possible to the vicitim device, blocking or slowing down its connection; best results can be obviously achieved in LAN.

### Requirements
  * Python2.7
    * socket
    * struct
    * txtcolors_pylib
    * pingsuite_pylib
