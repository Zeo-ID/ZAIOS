# ZAIOS – Zentral (Central) All-In-One System  
A modular, Linux-based open-source operating system for IT, HR, organizational, and service management.

[🇬🇧 English](#-english-version) | [🇩🇪 Deutsch](#-deutsch)

---

# 🇬🇧 English Version

## 🧩 What is ZAIOS?

**ZAIOS** is a fully integrated, modular open-source operating system designed for modern organizations.  
It unifies HR, IT service management, user administration, mail server, ticketing, reverse proxy, security, and organizational tools into one modern, browser-based platform.

ZAIOS can run as a **standalone Linux distribution** or as a **preconfigured virtual machine (VM)**.

---

## 🎯 Vision

ZAIOS aims to:

- centralize essential business processes  
- operate fully local and GDPR-compliant  
- offer a modular and intuitive interface  
- empower collaboration through open-source development  
- give leadership, HR, and IT a clear and modern overview  

---

## 🚀 Core Features (planned)

### 🖥️ Operating System & Infrastructure
- Custom Linux distribution (Debian-based)  
- Optional VM image  
- Web-based interface for all modules  
- Integrated reverse proxy for secure routing  
- Optional integrated mail server  
- Local data processing (GDPR-compliant)  
- Automatic system & security updates  

---

## 🔐 Integrated Web Application Firewall (WAF)

ZAIOS includes a built-in Web Application Firewall designed to protect the entire system from external threats.  
Every incoming request is analyzed before it reaches any module.

### The WAF protects against:
- SQL injection  
- Cross-site scripting (XSS)  
- Cross-site request forgery (CSRF)  
- Brute-force login attempts  
- Unauthorized API access  
- Automated scanners and bot traffic  
- Directory traversal attacks  

### Key Features:
- **Active request filtering**  
- **Automatic blocking** of malicious traffic  
- **Security event logging**  
- **Local rule updates** (no external servers required)  
- **Hardened public access** when modules are exposed  
- Works in **intranet** and **public networks**  

The WAF ensures that ZAIOS remains secure even when administrators enable *Public Access Mode*.

---

## 🔁 Integrated Reverse Proxy

ZAIOS uses a built-in reverse proxy to:

- route all internal services through one secure entry point  
- handle HTTPS certificates  
- enable the Public Access Mode  
- centralize logging and security  
- protect backend services  

This makes deployment simpler and significantly increases security.

---

## 👥 User & Role Management
- Local user directory  
- Integration with:
  - Microsoft Entra ID (Azure AD)  
  - Active Directory  
  - LDAP  
- Role-based access control (RBAC)  
- Single sign-on planned  

---

## 🧑‍💼 Digital Personnel File (HR Module)

- Complete digital employee file  
- Roles, permissions, work locations  
- Device & license assignments  
- Salary and cost overview  
- Optional integration with external HR systems (e.g., LOGA)  

---

## ⚽ Team View – Inspired by Football Manager

A unique leadership dashboard that visualizes teams like a football manager simulation:

- Overview of all employees in a team  
- Individual cost structure  
- Optional financial contribution data  
- Interactive employee profiles  
- Quick actions:
  - assign/remove licenses  
  - activate/deactivate access  
  - order devices  
  - auto-generate tickets  

---

## 🛠️ Integrated Ticket System

- Fully built-in ticketing  
- Incidents, requests, access, changes  
- Tickets auto-generated from HR/IT actions  
- Public access mode available  
- Ticket history per employee and location  

---

## 🌐 Public Access Mode

All modules run in the browser.

If ZAIOS has a public IP, administrators can activate:

> **“Enable Public Access”**

ZAIOS will then generate a secure link such as:

`https://123.45.67.89`  
or  
`https://servicedesk.yourcompany.com`

### Internally handled by ZAIOS:
- activating external access  
- configuring the reverse proxy  
- enabling WAF hardening  
- showing security recommendations  

### Externally required:
- port forwarding  
- optional DNS configuration

### Setup Wizard (Beginner Mode)
All external steps are guided through a  
**step-by-step “Setup for Dummies” wizard**.

---

## 🔌 Extendable Modular System

- Document management  
- Location management  
- Device & asset management  
- Calendar & planning  
- Reporting dashboards  
- Automation engine  
- Notification system  

---

## 🔓 Open Source – GNU GPL v3

ZAIOS is licensed under the **GNU GPL v3**, guaranteeing:

- free use  
- free modification  
- open development  
- no proprietary reuse possible  

---

## 🛠️ Project Status

ZAIOS is in early development.  
Architecture, modules, and the base system are actively being built.

---

## 🤝 Contributing

Contributions are welcome:

- ⭐ Star the repository  
- Submit ideas  
- Open issues  
- Join discussions  
- Contribute code  

---

## 💡 Project Lead

**Project Initiator:** Zeo-ID  
GitHub: https://github.com/Zeo-ID  

---

# 🇩🇪 Deutsch

## 🧩 Was ist ZAIOS?

**ZAIOS** ist ein vollständig integriertes, modulares Open-Source-Betriebssystem für Unternehmen.  
Es vereint HR, IT-Services, Benutzerverwaltung, Mailserver, Ticketsystem, Reverse-Proxy, Sicherheitsmodule und organisatorische Werkzeuge in einer modernen, browserbasierten Oberfläche.

ZAIOS läuft als **eigene Linux-Distribution** oder als **vorkonfigurierte VM**.

---

## 🎯 Vision

ZAIOS soll:

- zentrale Unternehmensprozesse bündeln  
- lokal und DSGVO-konform arbeiten  
- modular und intuitiv sein  
- gemeinschaftliche Weiterentwicklung ermöglichen  
- klare Oberflächen für Führung, HR und IT bereitstellen  

---

## 🚀 Zentrale Funktionen (geplant)

### 🖥️ Betriebssystem & Infrastruktur
- Eigene Linux-Distribution (Debian-basiert)  
- Optional als VM  
- Browserbasierte Oberfläche  
- Integrierter Reverse-Proxy  
- Optionaler Mailserver  
- Lokale Datenhaltung  
- Automatische Sicherheitsupdates  

---

## 🔐 Integrierte Web Application Firewall (WAF)

ZAIOS verfügt über eine eingebaute WAF, die das gesamte System schützt:

### Schutz vor:
- SQL-Injection  
- XSS  
- CSRF  
- Brute-Force  
- Unerlaubtem API-Zugriff  
- Bots & Scannern  
- Directory Traversal  

### Hauptfunktionen:
- Aktive Anfragefilterung  
- Automatisches Blockieren  
- Sicherheitsprotokolle  
- Lokale Regelupdates  
- Gehärteter öffentlicher Zugang  
- Stabil im Intranet & Internet  

---

## 🔁 Integrierter Reverse-Proxy

Der Reverse-Proxy übernimmt:

- Routing aller internen Dienste  
- HTTPS-Zertifikate  
- Absicherung des öffentlichen Zugangs  
- Zentrale Protokollierung  
- Schutz der internen Module  

---

## 👥 Benutzer- & Rollenverwaltung

- Lokale Benutzer  
- Anbindung an:
  - Entra ID  
  - Active Directory  
  - LDAP  
- Rollenbasierte Rechte  
- SSO geplant  

---

## 🧑‍💼 Digitale Personalakte

- Vollständige Akten  
- Rollen, Berechtigungen, Standorte  
- Geräte & Lizenzen  
- Kostenübersicht  
- Optional: HR-Systemanbindung  

---

## ⚽ Team-Übersicht – ähnlich wie ein Fußballmanager

- Teamübersicht  
- Kosten pro Person  
- Optional Einnahmen/Beitrag  
- Mitarbeiterprofil  
- Direktaktionen (Lizenzen, Geräte, Tickets)  

---

## 🛠️ Ticketsystem

- Komplett integriert  
- Störungen, Anfragen, Änderungen  
- Automatische Ticketerstellung  
- Öffentlicher Zugang möglich  
- Ticketverlauf pro Person  

---

## 🌐 Öffentlicher Modus

> **„Öffentlichen Zugriff aktivieren“**

ZAIOS öffnet den Reverse-Proxy, aktiviert die WAF und zeigt Hinweise zur Sicherheit.

Ein **„Schritt-für-Schritt für Dummies“-Assistent** führt durch alle extern notwendigen Schritte.

---

## 🔌 Erweiterbare Module

- Dokumente  
- Standorte  
- Assets  
- Kalender  
- Reporting  
- Automatisierung  
- Benachrichtigungen  

---

## 🔓 Open Source – GNU GPL v3

- freie Nutzung  
- offene Entwicklung  
- keine proprietäre Übernahme möglich  

---

## 🛠️ Projektstatus

ZAIOS befindet sich in einer frühen Entwicklungsphase.

---

## 🤝 Mitwirken

- Repo ⭐ markieren  
- Ideen einreichen  
- Issues öffnen  
- Mitdiskutieren  
- Code beitragen  

---

## 💡 Projektleitung

**Projektinitiator:** Zeo-ID  
GitHub: https://github.com/Zeo-ID  

---

### 🟢 ZAIOS — Zentral. Sicher. Zukunft.
