# Network Device Scanner

A lightweight and efficient Python-based command-line tool to discover active devices on a network. Built for system administrators, cybersecurity enthusiasts, and students.

## ✨ Features

| Feature | Description |
| :--- | :--- |
| 🌐 **Network Discovery** | Scan a subnet or IP range to find active devices |
| 💻 **Host Information** | Retrieves IP Address, Hostname, and Online Status |
| ⚡ **Fast Scanning** | Multi-threaded host discovery using ThreadPoolExecutor |
| 📁 **Report Generation** | Exports scan results directly to a CSV file |
| 🖥️ **Cross-Platform** | Works seamlessly on Linux, Windows, and macOS |

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Modules:** `socket`, `ipaddress`, `subprocess`, `csv`, `concurrent.futures`, `threading`

## 🚀 Installation

Clone the repository and set up the virtual environment:

```bash
git clone https://github.com/Sid-NodeX/network-device-scanner.git
cd network-device-scanner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
