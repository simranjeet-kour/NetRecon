import nmap

scanner = nmap.PortScanner(
    nmap_search_path=(
        r"C:\Program Files (x86)\Nmap\nmap.exe",
    )
)


def scan_target(target, scan_type):

    scan_options = {
        "Quick Scan": "-F",
        "Full Scan": "-p-",
        "Version Detection": "-sV",
        "OS Detection": "-O",
        "Aggressive Scan": "-A"
    }

    arguments = scan_options.get(scan_type, "-F")

    scanner.scan(hosts=target, arguments=arguments)

    results = []

    for host in scanner.all_hosts():

        host_status = scanner[host].state()

        os_name = "Unknown"

        if "osmatch" in scanner[host]:

            if len(scanner[host]["osmatch"]) > 0:
                os_name = scanner[host]["osmatch"][0]["name"]

        if "tcp" in scanner[host]:

            for port in scanner[host]["tcp"]:

                port_info = scanner[host]["tcp"][port]

                results.append({

                    "host": host,

                    "status": host_status,

                    "port": port,

                    "service": port_info.get("name", "Unknown"),

                    "state": port_info.get("state", "Unknown"),

                    "version": port_info.get("version", ""),

                    "product": port_info.get("product", ""),

                    "os": os_name

                })

    return results


def calculate_risk(results):

    score = 0

    recommendations = []

    open_ports = []

    for item in results:

        if "error" in item:
            continue

        port = item["port"]

        state = item["state"]

        if state != "open":
            continue

        open_ports.append(port)

        if port == 21:

            score += 25

            recommendations.append(
                "FTP (Port 21) is open. Disable FTP if it is not required."
            )

        elif port == 22:

            score += 10

            recommendations.append(
                "SSH is exposed. Use strong passwords or SSH keys."
            )

        elif port == 23:

            score += 35

            recommendations.append(
                "Telnet detected. Replace it with SSH."
            )

        elif port == 25:

            score += 15

            recommendations.append(
                "SMTP is exposed. Configure spam protection."
            )

        elif port == 53:

            score += 10

            recommendations.append(
                "Secure your DNS server."
            )

        elif port == 80:

            score += 10

            recommendations.append(
                "HTTP detected. Redirect users to HTTPS."
            )

        elif port == 110:

            score += 20

            recommendations.append(
                "POP3 detected. Consider encrypted alternatives."
            )

        elif port == 143:

            score += 20

            recommendations.append(
                "IMAP should use SSL/TLS."
            )

        elif port == 443:

            score += 3

            recommendations.append(
                "HTTPS is enabled. Keep certificates updated."
            )

        elif port == 3389:

            score += 25

            recommendations.append(
                "RDP exposed. Restrict access using firewall rules."
            )

        else:

            score += 5

    if score <= 20:

        level = "LOW"

        color = "green"

    elif score <= 50:

        level = "MEDIUM"

        color = "orange"

    else:

        level = "HIGH"

        color = "red"

    if len(recommendations) == 0:

        recommendations.append(
            "No major security issues were detected."
        )

    return {

        "score": score,

        "level": level,

        "color": color,

        "recommendations": recommendations,

        "open_ports": len(open_ports)

    }