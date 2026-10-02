import ipaddress
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed


def ping_host(ip, timeout=1):
    """Ping a single IP address and return True if reachable."""
    system = platform.system().lower()

    if system == "windows":
        cmd = ["ping", "-n", "1", "-w", str(timeout * 1000), str(ip)]
    else:
        cmd = ["ping", "-c", "1", "-W", str(timeout), str(ip)]

    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout + 1
        )
        return result.returncode == 0
    except Exception:
        return False


def scan_network(network_cidr, max_workers=100):
    """Scan a subnet/IP range and return a list of active IPs."""
    net = ipaddress.ip_network(network_cidr, strict=False)
    active_hosts = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(ping_host, ip): ip
            for ip in net.hosts()
        }

        for future in as_completed(futures):
            ip = futures[future]
            if future.result():
                active_hosts.append(str(ip))

    return sorted(active_hosts, key=lambda x: ipaddress.ip_address(x))
