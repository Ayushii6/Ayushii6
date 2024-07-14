import socket as sk

s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
ip_address= "127.0.0.1"
port_no = 2525
address=(ip_address,port_no)
s.bind(address) 
while True:
    data = s.recvfrom(100)
    message =data[0]
    ip_address = data[1][0]
    print(ip_address," >>>>> ",message)