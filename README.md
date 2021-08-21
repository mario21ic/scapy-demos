# upc-network

Dependencies:
```
$ pip install -r requirements.txt
```

Running a script:
```
$ python dns.py mario21ic.com
```

Sending an icmp with customized source (false mac addres, false ip and dest ip):
```
$ python icmp4_false_src.py 0:e0:4c:f1:ce:a2 192.168.1.10  192.168.1.10
```

Testing UDP:
```
$ python udp.py 192.168.1.10
$ sudo tcpdump -i enp2s0 udp port 666
```
Wireshark filter: ip.addr == 192.168.1.10 && udp

Testing UDP with false source mac & ip:
```
$ python udp_false_src.py 0:e0:4c:f1:ce:a2 192.168.1.10 192.168.1.10
```

Testing UDP on loop:
```
$ sudo netcat -ulp 666
$ sudo nmap -sU localhost -p 666
$ netcat -u localhost 666
$ python udp.py 127.0.0.1
```

ARP spoof:
target_ip spoof_ip spoof_mac
```
$ python arp_spoof.py 192.168.1.10 192.168.1.1 3c:06:30:0c:8b:67
```
On target machine:
```
$ arp -a
```

