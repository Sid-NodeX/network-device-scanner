import csv
import os


def export_to_csv(devices, filename="reports/devices.csv"):
    """Export discovered devices to CSV."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["IP Address", "Hostname", "Status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(devices)
