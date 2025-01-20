SSRF Port Scanning Script

This repository contains a Python script to perform a port scan using a Server-Side Request Forgery (SSRF) vulnerability. The script allows scanning specific IP addresses and port ranges to identify open and closed ports.
Features

    User-friendly interactive input prompts.
    Supports scanning any internal IP address accessible via SSRF.
    Outputs a list of open and closed ports.
    Includes error handling for network issues.

Prerequisites

    Python 3.x installed.
    requests library installed. You can install it using:

    pip3 install requests

How to Use
1. Clone the Repository

git clone https://github.com/Shubham03007/Ssrf-port-scanning.git
cd Ssrf-port-scanning

2. Run the Script

Execute the script using Python 3:

python3 ssrf_scan.py

3. Follow the Prompts

    Enter the vulnerable URL, e.g., http://example.com/ssrf?url={}.
    Specify the target IP address to scan.
    Provide the starting and ending port numbers.

Example Run

Enter the vulnerable URL (with {payload} placeholder): http://example.com/ssrf?url={}
Enter the target internal IP: 127.0.0.1
Enter the starting port: 1
Enter the ending port: 100

Scanning ports 1-100 on 127.0.0.1 via http://example.com/ssrf?url={}...
Port 22: OPEN
Port 80: OPEN
Port 443: OPEN
Port 8080: CLOSED
...
--- Scan Complete ---
Open Ports: [22, 80, 443]
Closed Ports: [1, 2, ..., 8080]

Script Overview

The script sends HTTP requests to the provided vulnerable URL with a payload targeting specific ports on the target IP address. Based on the response, it determines whether the port is open or closed.
Limitations

    Requires a vulnerable application with an SSRF vulnerability.
    Assumes different responses for open and closed ports (e.g., HTTP status codes or response content).

Disclaimer

This tool is for educational purposes and authorized penetration testing only. Unauthorized use of this tool is illegal and unethical.
