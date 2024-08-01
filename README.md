


# Network Address Changer for Linux

A Python script for Linux systems to periodically change the IP and MAC addresses of network interfaces. This tool is ideal for enhancing privacy, testing network configurations, or environments where frequent address changes are necessary.

## Features

- Change IP Address: Randomly assigns a new IP address within the `192.168.x.x` range.
- Change MAC Address:+
- Randomly generates and assigns a new MAC address.
- Periodic Changes:Configurable interval for automatic address updates.
- Logging:Records details of each change in a log file.

## Requirements

- Python 3.x
- `sudo` privileges for modifying network interfaces
- `ip` command-line utility (included in the `iproute2` package)

## Installation

1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/network_address_changer.git
   ```

2. Navigate to the Project Directory:
   ```bash
   cd network_address_changer
   ```

3. Ensure Python 3 is Installed:
   Make sure Python 3 is installed on your system. You can check this with:
   ```bash
   python3 --version
   ```

## Usage

Run the script with the following command, replacing the placeholders with your specific values:

```bash
python3 network_address_changer.py --interfaces eth0,wlan0 --interval 600 --log change_log.txt
```

### Arguments

- `--interfaces`: Comma-separated list of network interfaces to modify (e.g., `eth0,wlan0`).
- `--interval`: Time interval (in seconds) between changes (default: 300 seconds).
- `--log`: Path to the log file where changes will be recorded (default: `change_ip_mac.log`).

## Example Command

Change IP and MAC addresses for interfaces `eth0` and `wlan0` every 600 seconds, and log changes to `change_log.txt`:

```bash
python3 network_address_changer.py --interfaces eth0,wlan0 --interval 600 --log change_log.txt
```

## Notes

- Ensure you have `sudo` privileges to modify network settings.
- Use this tool responsibly to avoid network disruptions.

```

