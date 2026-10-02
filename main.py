from scanner import scan_network
from hostname_resolver import resolve_hostname
from exporter import export_to_csv


def main():
    print("=" * 45)
    print("       NETWORK DEVICE SCANNER")
    print("=" * 45)

    target = input("Enter target network (e.g. 192.168.1.0/24): ").strip()

    if not target:
        target = "192.168.1.0/24"

    print(f"\nTarget Network: {target}")
    print("Scanning...\n")

    active_ips = scan_network(target)

    devices = []

    for ip in active_ips:
        hostname = resolve_hostname(ip)

        devices.append({
            "IP Address": ip,
            "Hostname": hostname,
            "Status": "Online"
        })

        print(f"[+] {ip:15} {hostname}")

    print(f"\nTotal Active Devices Found: {len(devices)}")

    if devices:
        choice = input("\nExport results to CSV? (y/n): ").strip().lower()

        if choice == "y":
            export_to_csv(devices)
            print("Results saved to reports/devices.csv")


if __name__ == "__main__":
    main()
