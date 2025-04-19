import json
import os
import sys
from datetime import datetime
from time import perf_counter
from lmstudio_api import LMStudioChat

CONFIG_PATH = "config.json"
if not os.path.exists(CONFIG_PATH):
    print("⚠️ Konfigurationsdatei nicht gefunden.")
    sys.exit(1)

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

SYSTEM_PROMPT = config.get("system_prompt", "")
ENDPOINT_URL = config.get("endpoint_url", "http://localhost:1234")
MAX_HISTORY = config.get("max_history", 3)

chat_start_time = datetime.now()
timestamp = chat_start_time.strftime("%Y%m%d_%H%M%S")
chat_datei = f"chat_{timestamp}.json"

chat = LMStudioChat(endpoint_url=ENDPOINT_URL, system_prompt=SYSTEM_PROMPT, max_history=MAX_HISTORY)

chatstruktur = {
    "model": chat.model_name,
    "creationDate": chat_start_time.strftime("%Y-%m-%d %H:%M:%S"),
    "systemPrompt": SYSTEM_PROMPT,
    "chatMessages": []
}


def speichere_chatverlauf(dateiname, struktur):
    with open(dateiname, "w", encoding="utf-8") as f:
        json.dump(struktur, f, indent=2, ensure_ascii=False)


print("Starte lokalen KI-Chat (LM Studio). Beende mit 'exit' oder 'quit'.\n")

while True:
    user_input = input("Du: ")
    if user_input.lower() in ["exit", "quit"]:
        speichere_chatverlauf(chat_datei, chatstruktur)
        print(f"📂 Chatverlauf gespeichert in: {chat_datei}")
        break

    start = perf_counter()
    antwort = chat.send(user_input)
    dauer = perf_counter() - start

    if antwort:
        chatstruktur["chatMessages"].append({
            "User": user_input,
            "Assistent": antwort,
            "duration": f"{dauer:.2f} Sekunden"
        })
        speichere_chatverlauf(chat_datei, chatstruktur)
