# Imports platform and os
import platform
import os


# This is a list of IP addresses to ping
ip_addresses = ["127.0.0.1", "8.0.0.1", "192.168.0.10", "192.168.10.10"]

# These are the ping options I'm using. I have to use -t because I'm using MAC OS and -w doesn't work
ping_options = "-c 1 -t 2"

# This stores the output in a text file called "pinger.txt" which is located in the current directory
output_file = "pinger.txt"

# This is a for loop that goes through the IP addresses in the list
for ip in ip_addresses:
    ping_cmd = f"ping {ping_options} {ip}"

# Prints the current directory
    print("Current Directory:", os.getcwd())

    # This will redirect the output to the pinger text file
    exit_code = os.system(ping_cmd)

    print(f"IP Address: {ip}")
    print(f"Ping Command: {ping_cmd}")
    print(f"Exit Code: {exit_code}")
    print("-" * 20)  # Separator between ping results
