import sys
import nmap

if len(sys.argv) != 2:
    print("Use: python port_scanner.py <IP_address>")
    sys.exit(1)

target = sys.argv[1]

# Create a PortScanner instance
nm = nmap.PortScanner()

# Execute scanning
nm.scan(target, arguments="-T4 -p-")

if target not in nm.all_hosts():
    print(f"No response from host: {target}")
    sys.exit(1)

print(f"Open ports in host: {target}:")

for port in nm[target]['tcp']:
    if nm[target]['tcp'][port]['state'] == 'open':
        print(f" - {port}") 
