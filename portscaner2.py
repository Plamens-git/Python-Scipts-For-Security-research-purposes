import sys
import socket
import pyfiglet
import multiprocessing

# ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentesters \nPort Scanner")
# print(ascii_banner)

ip = '35.156.209.163'
open_ports = []

# Define the number of processes to use
NUM_PROCESSES = multiprocessing.cpu_count()

# Function to probe a single port
def probe_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
    except Exception as e:
        print(f"Error probing port {port}: {e}")

# Function to perform port scanning using multiprocessing
def port_scan():
    with multiprocessing.Pool(processes=NUM_PROCESSES) as pool:
        pool.map(probe_port, range(1, 65536))

if __name__ == '__main__':
    # Perform port scanning
    port_scan()

    if open_ports:
        print("Open Ports are: ")
        print(sorted(open_ports))
    else:
        print("Looks like no ports are open :(")

