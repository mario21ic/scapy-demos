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
