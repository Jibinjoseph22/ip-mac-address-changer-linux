#!/usr/bin/env python3

import argparse
import subprocess
import time
import random
import re

def get_network_interfaces():
    """Get a list of available network interfaces."""
    result = subprocess.run(['ip', 'link', 'show'], stdout=subprocess.PIPE, text=True)
    interfaces = []
    for line in result.stdout.split('\n'):
        if line and ':' in line:
            interface = line.split(':')[1].strip()
            interfaces.append(interface)
    return interfaces

def validate_interfaces(interfaces):
    """Validate if the specified network interfaces exist."""
    available_interfaces = get_network_interfaces()
    for interface in interfaces:
        if interface not in available_interfaces:
            print(f"Interface {interface} not found.")
            return False
    return True

def change_mac(interface):
    """Change the MAC address of the specified network interface."""
    new_mac = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
    try:
        # Bring the interface down
        subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'down'], check=True)
        # Change the MAC address
        subprocess.run(['sudo', 'ip', 'link', 'set', 'dev', interface, 'address', new_mac], check=True)
        # Bring the interface up
        subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'], check=True)
        print(f"Changed MAC address for {interface} to {new_mac}")
        return new_mac
    except subprocess.CalledProcessError as e:
        print(f"Error changing MAC address for {interface}: {e}")
        return None

def change_ip(interface):
    """Change the IP address of the specified network interface."""
    new_ip = f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"
    try:
        # Change the IP address
        subprocess.run(['sudo', 'ip', 'addr', 'flush', 'dev', interface], check=True)
        subprocess.run(['sudo', 'ip', 'addr', 'add', new_ip + '/24', 'dev', interface], check=True)
        # Bring the interface up
        subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'], check=True)
        print(f"Changed IP address for {interface} to {new_ip}")
        return new_ip
    except subprocess.CalledProcessError as e:
        print(f"Error changing IP address for {interface}: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Change IP and MAC addresses periodically.')
    parser.add_argument('--interfaces', required=True, help='Comma-separated list of network interfaces.')
    parser.add_argument('--interval', type=int, default=300, help='Change interval in seconds.')
    parser.add_argument('--log', default='change_ip_mac.log', help='Log file path.')

    args = parser.parse_args()
    interfaces = args.interfaces.split(',')
    interval = args.interval
    log_file = args.log

    # Validate interfaces
    if not validate_interfaces(interfaces):
        print("One or more specified interfaces are not available.")
        return

    # Open log file
    with open(log_file, 'a') as log:
        while True:
            for interface in interfaces:
                new_mac = change_mac(interface)
                new_ip = change_ip(interface)
                log.write(f"Interface: {interface}\n")
                log.write(f"New IP address: {new_ip}\n")
                log.write(f"New MAC address: {new_mac}\n")
                log.write('-' * 40 + '\n')
            log.flush()
            print(f"Waiting for {interval} seconds before the next change...")
            time.sleep(interval)

if __name__ == '__main__':
    main()
