# ZAIOS – Zentral (Central) All-In-One System  
A modular, Linux-based open-source operating system for IT, HR, organizational, and service management.

[🇬🇧 English](#-english-version) | [🇩🇪 Deutsch](#-deutsch)

---

# 🇬🇧 English Version

## 🧩 What is ZAIOS?

**ZAIOS** is a fully integrated, modular open-source operating system designed for modern organizations.  
It unifies HR, IT service management, user administration, DNS, mail server, ticketing, security, and organizational tools into one modern, browser-based platform.

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
- Integrated DNS server  
- Optional integrated mail server  
- Local data processing (GDPR-compliant)  
- Automatic system & security updates  

---

## 🔐 Integrated Web Application Firewall (WAF)

ZAIOS includes a built-in Web Application Firewall designed to protect the entire system from external threats.  
The WAF filters and analyzes all incoming requests before they reach any module or interface.

### The WAF protects against:
- SQL injection  
- Cross-site scripting (XSS)  
- Cross-site request forgery (CSRF)  
- Brute-force login attempts  
- Unauthorized API access  
- Automated scanners and bot traffic  
- Directory traversal attacks  

### Key Features:
- **Active request filtering** on system level  
- **Automatic blocking** of suspicious or malicious traffic  
- **Security event logging** for administrators  
- **Automatic rule updates** (local, no external servers)  
- **Hardened public access** when exposed to the internet  
- Works reliably in **local intranet** and **public networks**  

The WAF ensures that ZAIOS remains secure even when administrators enable *Public Access Mode*.

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
- Individual cost structure:
  - salary  
  - licenses  
  - devices  
- Optional financial contribution metrics  
- Interactive employee profile:
  - permissions  
  - assets  
  - licenses  
  - active tickets  
- Quick actions:
  - request/remove licenses  
  - activate/deactivate access  
  - order devices  
  - auto-generate tickets  

---

## 🛠️ Integrated Ticket System

- No external ticket solution required  
- Tickets for incidents, requests, changes, access  
- Auto-generated tickets from actions inside the modules  
- Public access mode available  
- Full ticket history per employee and per location  

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
- enabling external web access  
- adjusting firewall rules  
- showing recommended security notices  

### Externally required:
- port forwarding  
- DNS configuration  

### Setup Wizard (Beginner Mode)
Everything that must be configured outside the OS is explained in a  
**step-by-step “Setup for Dummies” wizard**, making public deployment easy even for non-experts.

---

## 🔌 Extendable Modular System

- Document management  
- Asset management  
- Location / branch management  
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
- no possibility of proprietary reuse  

---

## 🛠️ Project Status

ZAIOS is in early development.  
Architecture, modules and base system are being actively built.

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
Es vereint HR, IT-Services, Benutzerverwaltung, DNS, Mailserver, Ticketsystem, Sicherheitsmodule und organisatorische Werkzeuge in einer modernen, browserbasierten Oberfläche.

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
- Integrierter DNS-Server  
- Optionaler Mailserver  
- Lokale Datenhaltung  
- Automatische Sicherheitsupdates  

---

## 🔐 Integrierte Web Application Firewall (WAF)

ZAIOS verfügt über eine eingebaute Web Application Firewall, die das System vor externen Angriffen schützt.  
Die WAF filtert und analysiert alle eingehenden Anfragen, bevor sie ein Modul oder eine API erreichen.

### Die WAF schützt vor:
- SQL-Injection  
- Cross-Site-Scripting (XSS)  
- Cross-Site-Request-Forgery (CSRF)  
- Brute-Force-Angriffen  
- Unautorisiertem API-Zugriff  
- Bots & automatisierten Scannern  
- Directory-Traversal-Angriffen  

### Hauptfunktionen:
- **Aktive Anfragenfilterung**  
- **Automatisches Blockieren** verdächtiger Zugriffe  
- **Protokollierung von Sicherheitsereignissen**  
- **Lokale Regelerneuerung** ohne externe Server  
- **Gehärteter öffentlicher Zugriff**  
- Stabil im **Intranet** und im **öffentlichen Internet**  

Die WAF stellt sicher, dass ZAIOS auch im *öffentlichen Modus* sicher bleibt.

---

## 👥 Benutzer- & Rollenverwaltung

- Lokale Benutzerverwaltung  
- Anbindung an:
  - Microsoft Entra ID  
  - Active Directory  
  - LDAP  
- Rollenbasierte Zugriffssteuerung  
- SSO geplant  

---

## 🧑‍💼 Digitale Personalakte

- Vollständige Personalakte  
- Rollen, Berechtigungen, Standorte  
- Geräte- & Lizenzzuordnung  
- Kostenübersicht  
- HR-Systemanbindung möglich  

---

## ⚽ Team-Übersicht – ähnlich wie ein Fußballmanager

- Übersicht aller Teammitglieder  
- Kosten pro Person  
- Optional: Einnahmen/Beitragsübersicht  
- Interaktive Mitarbeiterprofile  
- Direktaktionen (Lizenzen, Zugänge, Geräte, Tickets)  

---

## 🛠️ Integriertes Ticketsystem

- Kein externes Ticketsystem nötig  
- Störungen, Änderungen, Zugänge, Anfragen  
- Automatische Ticketerstellung  
- Öffentlicher Zugang möglich  
- Ticketverlauf pro Mitarbeiter  

---

## 🌐 Öffentlicher Zugriff

Mit einer öffentlichen IP kann aktiviert werden:

> **„Öffentlichen Zugriff aktivieren“**

ZAIOS erzeugt einen sicheren Link und unterstützt mit Erklärungen sowie Firewallhinweisen.

Der Einrichtungsassistent zeigt alle nötigen externen Schritte in einem  
**„Schritt-für-Schritt für Dummies“**-Modus.

---

## 🔌 Erweiterbare Module

- Dokumentenmanagement  
- Standortverwaltung  
- Assetmanagement  
- Kalender & Planung  
- Reporting  
- Automatisierung  
- Benachrichtigungen  

---

## 🔓 Open Source – GNU GPL v3

Garantiert:

- freie Nutzung  
- offene Weiterentwicklung  
- keine Proprietarisierung möglich  

---

## 🛠️ Projektstatus

ZAIOS befindet sich in einer frühen Entwicklungsphase.

---

## 🤝 Mitwirken

- Repo ⭐ markieren  
- Ideen einreichen  
- Issues öffnen  
- Mitdiskutieren  
- Code beisteuern  

---

## 💡 Projektleitung

**Projektinitiator:** Zeo-ID  
GitHub: https://github.com/Zeo-ID  

---

### 🟢 ZAIOS — Zentral. Sicher. Zukunft.
