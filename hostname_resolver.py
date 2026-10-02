import socket


def resolve_hostname(ip):
    """Resolve hostname using reverse DNS lookup."""
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except (socket.herror, socket.gaierror, OSError):
        return "Unknown"
