# ZAIOS – Zentral All-In-One System  
Ein modulares, Linux-basiertes Open-Source-Betriebssystem für IT-, HR-, Organisation- und Servicemanagement.

[🇩🇪 Deutsch](#deutsch) | [🇬🇧 English](#english-version)

---

# 🇩🇪 Deutsch

## 🧩 Was ist ZAIOS?

**ZAIOS** ist ein vollständig integriertes, modulares Open-Source-Betriebssystem für Unternehmen.  
Es kombiniert HR, IT-Service, Benutzerverwaltung, DNS, Mailserver, Ticketsystem, Standortverwaltung und Sicherheitsfunktionen in einer einzigen, modernen, webbasierten Plattform.

ZAIOS läuft als **eigene Linux-Distribution** oder optional als **VM-Komplettpaket**.

---

## 🎯 Vision

ZAIOS soll:

- alle Unternehmensprozesse zentralisieren  
- ausschließlich lokal und DSGVO-konform laufen  
- modular und intuitiv erweiterbar bleiben  
- eine Community-basierte Weiterentwicklung ermöglichen  
- Führungskräften, HR und IT eine klare, moderne Oberfläche bieten  

Das Ergebnis ist ein All-In-One-Unternehmensbetriebssystem.

---

## 🚀 Kernfunktionen (geplant)

### 🖥️ Betriebssystem & Infrastruktur
- Eigene Linux-Distribution (Debian-basiert)  
- Optional als vorgefertigte VM  
- Webbasierte Oberfläche für alle Module  
- Eingebaute WAF (Web Application Firewall)  
- Integrierter DNS-Server  
- Optional integrierter Mailserver  
- Lokale Datenhaltung (DSGVO-konform)  
- Automatische Sicherheitsupdates  

---

## 👥 Benutzer- & Rollenverwaltung
- Lokale Benutzerverwaltung  
- Integration in:
  - Microsoft Entra ID (Azure AD)  
  - Active Directory  
  - LDAP  
- Single-Sign-On (geplant)  
- Rollenbasierte Sichtbarkeit und Zugriffsrechte  

---

## 🧑‍💼 Digitale Personalakte (HR)
- Vollständige Personalakte  
- Rollen, Berechtigungen, Einsatzorte  
- Lizenz- & Gerätezuordnung  
- Kostenübersicht (Gehalt, Lizenzen, Geräte)  
- Optionale Verbindung zu HR-Systemen (z. B. LOGA)  

---

## ⚽ Team-View wie ein Fußballmanager

Führungskräfte erhalten eine moderne Übersicht, inspiriert von einem **Fußballmanager**:

- Übersicht aller Mitarbeitenden eines Teams  
- Kosten pro Mitarbeiter:
  - Gehalt  
  - Lizenzkosten  
  - Gerätenutzung  
- (Optional) wirtschaftlicher Beitrag / Einnahmen  
- Klicken auf Mitarbeiter öffnet ein interaktives Profil:
  - Daten  
  - Rollen  
  - Berechtigungen  
  - Assets  
  - Lizenzen  
  - Tickets  
- Direkt-Aktionen:
  - Lizenz beantragen / entziehen  
  - Zugang erstellen / deaktivieren  
  - Gerät bestellen  
  - Ticket automatisch erstellen  

---

## 🛠️ Integriertes Ticketsystem

- Kein externes Ticketsystem nötig  
- Tickets für Störungen, Änderungen, Zugänge, Geräte  
- Automatische Ticketgenerierung aus Benutzer- oder Modulaktionen  
- Öffentlicher Zugriff möglich (siehe Public Access)  
- Ticketübersicht pro Mitarbeiter und pro Standort  

---

## 🌐 Public Access (Öffentliche Erreichbarkeit)

Alle Module sind **browserbasiert**.  
Wenn ZAIOS eine öffentliche IP hat, kann der Admin im Backend einfach aktivieren:

> **„Extern erreichbar machen“**

Dann zeigt ZAIOS einen Link wie:  
`https://123.45.67.89` oder `https://servicedesk.deinefirma.de`

### Was ZAIOS automatisch macht:
- Webserver für externen Zugriff freigeben  
- Interne Firewall konfigurieren  
- Hinweise zu Sicherheit anzeigen  

### Was extern eingestellt werden muss:
- Portfreigabe (z. B. Router / Firewall)  
- DNS-Eintrag für eigene Domain  

### Aber:
ZAIOS erklärt **alles Schritt für Schritt**, verständlich für Anfänger:  
**„Einrichtung für Dummies“**.  
Der Assistent führt durch Portfreigabe, DNS-Einrichtung, Zertifikate und empfohlene Sicherheitseinstellungen.

---

## 💾 Erweiterbare Module
- Dokumentenmanagement  
- Standortverwaltung  
- Assetmanagement  
- Kalender & Planung  
- Reporting & Dashboards  
- Automatisierungen  
- Benachrichtigungssystem  

---

## 🔓 Open Source – GNU GPL v3

ZAIOS wird unter der **GNU GPL v3** veröffentlicht.  
Diese Lizenz stellt sicher:

- frei nutzbar  
- frei veränderbar  
- Verbesserungen müssen ebenfalls offen bleiben  
- niemand kann das Projekt in ein Closed-Source-Produkt verwandeln  

---

## 🛠️ Projektstatus

Das Projekt befindet sich in der frühen Startphase.  
Die Struktur, Module und Architektur werden aktiv entwickelt.

---

## 🤝 Mitwirken

Mitmachen ist ausdrücklich erwünscht:

- ⭐ Repo beobachten  
- Ideen einreichen  
- Issues erstellen  
- Diskussionen starten  
- Code beitragen (sobald verfügbar)  

---

## 💡 Projektleitung

**Projektinitiator:** Zeo-ID  
GitHub: https://github.com/Zeo-ID  

---

# 🇬🇧 English Version

## 🧩 What is ZAIOS?

**ZAIOS** is a fully integrated, modular open-source operating system designed for companies.  
It unifies HR, IT service management, user administration, DNS, mail server, ticketing, organizational structures and security modules into one modern, browser-based platform.

ZAIOS runs as a **dedicated Linux distribution** or as an **optional VM package**.

---

## 🎯 Vision

ZAIOS aims to:

- centralize all core company processes  
- run completely local and GDPR-compliant  
- stay modular and extendable  
- support community-driven development  
- offer a modern interface for managers, HR and IT  

The result is an all-in-one enterprise operating system.

---

## 🚀 Key Features (planned)

### 🖥️ Operating System & Infrastructure
- Custom Linux distribution (Debian-based)  
- Optional VM image  
- Web-based UI for all modules  
- Built-in WAF (Web Application Firewall)  
- Integrated DNS server  
- Optional mail server  
- Full local data processing (GDPR compliant)  
- Automatic security updates  

---

## 👥 User & Role Management
- Local user management  
- Integration with:
  - Microsoft Entra ID (Azure AD)  
  - Active Directory  
  - LDAP  
- Role-based access  
- Single-sign-on planned  

---

## 🧑‍💼 Digital HR File
- Complete personnel file  
- Roles, permissions, locations  
- Device & license assignment  
- Cost overview  
- Optional HR system integration (e.g., LOGA)  

---

## ⚽ Team View (Football Manager Style)

Leaders get a powerful overview inspired by **football manager interfaces**:

- Team overview  
- Cost breakdown per employee:
  - salary  
  - license costs  
  - device costs  
- (Optional) financial contribution  
- Clicking an employee opens a detailed profile:
  - personal data  
  - permissions  
  - assets  
  - licenses  
  - tickets  
- Quick actions:
  - request/remove license  
  - create/disable access  
  - order device  
  - auto-create tickets  

---

## 🛠️ Integrated Ticket System

- No external ticket solution needed  
- Supports incident, change, access and asset requests  
- Auto-generated tickets from actions in modules  
- Public access toggle available  
- Ticket history per employee  

---

## 🌐 Public Access Mode

All modules run in the browser.  
If ZAIOS has a public IP, the admin can activate:

> **"Enable public access"**

ZAIOS then displays a generated link like:  
`https://123.45.67.89` or `https://servicedesk.company.com`

### ZAIOS handles internally:
- opening the web service externally  
- adjusting internal firewall settings  
- providing security recommendations  

### External requirements:
- router/firewall port forwarding  
- DNS configuration  

### But:
A guided wizard explains **everything step-by-step**,  
suitable even for complete beginners (**"setup for dummies"**).

---

## 💾 Extendable Modules
- Document management  
- Location management  
- Asset management  
- Calendar & planning  
- Reporting & dashboards  
- Automation  
- Notification system  

---

## 🔓 Open Source – GNU GPL v3

ZAIOS is released under the **GNU GPL v3**.  
This ensures:

- freedom to use  
- freedom to modify  
- derived works must stay open  
- no one can turn it into a closed-source product  

---

## 🛠️ Project Status

The project is in early development and actively evolving.

---

## 🤝 Contributing

Contributions are welcome:

- ⭐ star the repository  
- open issues  
- submit ideas  
- join discussions  
- submit code (once available)  

---

## 💡 Project Lead

**Project Initiator:** Zeo-ID  
GitHub: https://github.com/Zeo-ID  

---

### 🟢 “Central. Secure. Future.”  
**ZAIOS – The All-In-One Operating System for Modern Organizations.**


