# Network Scanning

## IP scan only
```bash
sudo nmap -sn 10.0.0-1.0-255    # specifying ranges of search. 
```
Use eth or wifi ip as guide to available networks.
Sudo allows it to get more information but is not a requirement.

## Detailed single IP scan
Looks at all ports too
```bash
sudo nmap -A -T4 10.0.0.100
```

## Identify the manufacturer

```bash
sudo nmap -sn 10.0.0.0-255
```
>> Nmap scan report for 10.0.0.100\
>> Host is up (-0.12s latency).\
>> MAC Address: 14:1F:78:5C:A6:FE (Unknown)\
>> ...
> 
Paste "14:1F:78" into website search field https://www.wireshark.org/tools/oui-lookup.html#
>> 14:1F:78 Samsung Electronics Co.,Ltd

i.e. My Samsung Cellphone
