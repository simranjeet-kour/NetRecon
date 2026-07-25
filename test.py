from scanner import scan_target

target = "scanme.nmap.org"

scan_type = "Quick Scan"

result = scan_target(target, scan_type)

for item in result:
    print(item)