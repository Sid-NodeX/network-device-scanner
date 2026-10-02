# Network Device Scanner

A Python-based command-line tool to discover active devices on a network.

## Features
- Scan a subnet or IP range
- Detect online devices
- Resolve hostnames via reverse DNS
- Export results to CSV

## Tech Stack
- Python 3.x
- socket, ipaddress, subprocess, csv, concurrent.futures

## Installation

git clone https://github.com/Sid-NodeX/network-device-scanner.git
cd network-device-scanner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Usage

python main.py

## Sample Output

[+] 10.22.5.56     Unknown
[+] 10.22.5.204    Unknown
Total Active Devices Found: 2

## Author
Sidhartha Mondal (@Sid-NodeX)
