# ARPSpoof
ARP Spoofing tool written in python with command line interface

## Installation
```
git clone https://github.com/ozXsasson/ARPSpoof
cd ARPSpoof
```

## Usage
```
usage: arpSpoof.py [-h] [-t TARGET] [-g GATEWAY]

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target IP (Victim address)
  -g GATEWAY, --gateway GATEWAY
                        Gateway IP (Router address)
```

## Example
```
# Dont forget to do port-forwarding
# echo 1 > /proc/sys/net/ipv4/ip_forward

sudo python arpSpoof.py --target 10.0.2.15 --gateway 10.0.2.1
