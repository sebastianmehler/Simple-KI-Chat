# 🧠 Simple-KI-Chat

Ein minimalistischer, lokal laufender Konsolen-Chat mit einer lokalen Sprach-KI über LM Studio.  
Ideal für experimentelle Unterhaltungen, Rollenspiele oder philosophische Gespräche mit einem empathischen, kreativen Assistenten.

Dieses Projekt ist eine erste Annäherung an die Programmiersprache Python und entstand vollständig im Rahmen sogenannter *Vibe Coding*-Sessions – also durch kreatives Prompt Engineering mit KI-Unterstützung.

## 🚀 Features

- Lokale Nutzung eines KI-Modells über LM Studio (OpenAI-kompatibles API)
- Gesprächsverlauf mit Zeitstempel wird automatisch gespeichert
- Unterstützung für System-Prompts und Modellwahl
- **Antworten werden gestreamt**, d. h. sie erscheinen in Echtzeit während der Generierung
- Farbliche Hervorhebung von <think>-Blöcken für "Gedanken" der KI
- Einfache Konfiguration über `config.json`

## 📦 Voraussetzungen

- Python 3.9+
- Lokaler LM Studio Server mit aktiviertem API-Zugriff
- Ein Modell (z. B. Mistral, MythoMax etc.), das mit dem OpenAI-kompatiblen Endpunkt verwendet werden kann

## 🔧 Installation

1. Klone das Repository:

```bash
git clone https://github.com/dein-benutzername/simple-ki-chat.git
cd simple-ki-chat
```

2. Installiere die benötigten Python-Abhängigkeiten:

```bash
pip install -r requirements.txt
```

> **Hinweis:** Die einzige externe Abhängigkeit ist `requests`. Stelle sicher, dass sie installiert ist:
>
> ```bash
> pip install requests
> ```

3. Erstelle deine Konfigurationsdatei:

```bash
cp config.json.sample config.json
```

> **Wichtig:** Die Datei `config.json.sample` muss in `config.json` umbenannt werden, damit das Programm korrekt startet.

Bearbeite `config.json` nach deinen Wünschen. Beispiel:

```json
{
  "system_prompt": "Du bist ein hilfreiches, kreatives KI-Modell.",
  "endpoint_url": "http://localhost:1234",
  "max_history": 10
}
```

## 🗨️ Nutzung

Starte den Konsolenchat mit:

```bash
python chat_console.py
```

Gib deine Nachrichten ein – die KI antwortet live mit farblicher Hervorhebung. Beende den Chat mit `exit` oder `quit`.

Am Ende wird automatisch eine Datei wie `chat_20250419_1530.json` erzeugt, die den kompletten Verlauf enthält.

## 📁 Projektstruktur

```
.
├── chat_console.py        # Hauptprogramm für die Konsoleninteraktion
├── lmstudio_api.py        # API-Kommunikation mit LM Studio (OpenAI-kompatibel)
├── config.json.sample     # Beispielkonfiguration
├── .gitignore             # Ignoriert z. B. Chatverläufe und `config.json`
├── LICENSE                # Lizenz (falls vorhanden)
├── README.md              # Diese Datei
```

## 🛡️ Datenschutz

Alle Daten verbleiben lokal. Es findet keine Kommunikation mit externen Servern statt – alles läuft über deinen eigenen LM Studio Server.

## 📜 Lizenz

Siehe [LICENSE](LICENSE).

## 💡 Idee oder Beitrag?

Pull Requests, Ideen und Verbesserungen sind willkommen!

---

🛠️ *Diese Dokumentation wurde mithilfe von KI und Prompt Engineering durch den Autor erstellt.*

