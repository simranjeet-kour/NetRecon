# 🛡️ NetRecon

## Professional Network Security Assessment Tool

NetRecon is a Flask-based Network Security Assessment Tool that uses **Nmap** to perform network scans and present the results through a modern web dashboard. It helps users identify open ports, running services, assess potential security risks, and generate downloadable security reports.

---

## 🚀 Features

- 🔍 Scan IP addresses and hostnames
- ⚡ Multiple Nmap scan modes
  - Quick Scan
  - Full Scan
  - Version Detection
  - OS Detection
  - Aggressive Scan
- 📊 Interactive Dashboard
- 🔓 Open Ports Detection
- 💻 Operating System Detection
- 🛡️ Automatic Security Risk Analysis
- 💡 Security Recommendations
- 📄 Download Scan Report
- 🌙 Modern Responsive UI

---

## 🛠️ Technologies Used

- Python
- Flask
- Nmap
- HTML5
- CSS3
- JavaScript
- Git
- GitHub

---

## 📂 Project Structure

```text
NetRecon/

│── app.py

│── scanner.py

│── report.py

│── requirements.txt

│── README.md

│

├── templates/

│ └── index.html

│

├── static/

│ ├── style.css

│ └── script.js

│

├── reports/

├── screenshots/

└── venv/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/simranjeet-kour/NetRecon.git
```

### Open Project

```bash
cd NetRecon
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
py app.py
```

### Open Browser

```
http://127.0.0.1:5000
```

---

# 📷 Screenshots

## 🏠 Home Dashboard

![Home](screenshots/home.png)

---

## 🔍 Network Scan

![Scan](screenshots/scan.png)

---

## 📊 Scan Results

![Results](screenshots/results.png)

---

## ⚠️ Risk Analysis

![Risk](screenshots/risk.png)

---

## 📄 Download Report

![Report](screenshots/report.png)

---

# 🔒 Risk Analysis

NetRecon evaluates scanned services and assigns a security risk score.

Examples:

| Port | Risk |
|------|------|
|21 FTP|🔴 High|
|22 SSH|🟡 Medium|
|23 Telnet|🔴 Critical|
|80 HTTP|🟢 Low|
|443 HTTPS|🟢 Secure|

The application automatically generates security recommendations based on detected services.

---

# 📄 Generated Report

The application generates a downloadable report containing:

- Scan Date
- Target Information
- Host Status
- Operating System
- Open Ports
- Running Services
- Risk Score
- Security Recommendations

---

# 📈 Future Enhancements

- PDF Report Generation
- Scan History
- Network Topology Visualization
- Vulnerability Database Integration
- CVE Detection
- Multi-host Scanning
- Export Results as CSV
- User Authentication
- Database Support

---

# 👨‍💻 Author

**Simranjeet Kour**

Cybersecurity Student

Lovely Professional University

GitHub:
https://github.com/simranjeet-kour

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
