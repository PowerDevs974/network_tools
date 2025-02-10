import sys
import nmap
import re


if len(sys.argv) != 2:
    print("Usage: python network_hosts.py <Network_IPv4_Address/Mask>")
    sys.exit(1)

target = sys.argv[1]


# Function to validate the IP address with the subnet mask format
def is_valid_network(network):
    # Regular expression to validate the IP/mask format
    regex = r"^([0-9]{1,3}\.){3}[0-9]{1,3}/([0-9]{1,2})$"
    if re.match(regex, network):
        ip, mask = network.split('/')
        # Check that the mask is in the range 0-32
        if 0 <= int(mask) <= 32:
            return True
    return False


# Validate the network format
if not is_valid_network(target):
    print("Error: The network address is not in the correct format or the mask is invalid.")
    sys.exit(1)

nm = nmap.PortScanner()

print(f"Searching hosts up on network: {target}")

# Try to perform the scan and handle possible exceptions
try:
    nm.scan(hosts=target, arguments="-sn")
except Exception as e:
    print(f"Error while scanning: {e}")
    sys.exit(1)

# Check if the network responded
if not nm.all_hosts():
    print(f"ERROR: The network {target} does not exist or is not responding.")
    sys.exit(1)

counter = 0

# Verify if the IP appears in the scanning result
for host in nm.all_hosts():
    print(host)
    counter += 1

print(f"\nTotal hosts up: {counter}")
