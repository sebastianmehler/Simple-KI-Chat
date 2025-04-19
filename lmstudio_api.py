import requests
import re
import json
import time


COLOR_ASSISTANT = "\033[92m"
COLOR_THINK = "\033[93m"
COLOR_RESET = "\033[0m"

class LMStudioChat:
    def __init__(self, endpoint_url, system_prompt="", max_history=3):
        self.endpoint_url = endpoint_url.rstrip("/") + "/v1/chat/completions"
        self.system_prompt = system_prompt
        self.max_history = max_history
        self.history = []
        self.model_name = self._get_model_name()

    def _get_model_name(self):
        try:
            response = requests.get(self.endpoint_url.replace("/chat/completions", "/models"))
            response.raise_for_status()
            models = response.json()["data"]
            if not models:
                raise ValueError("Keine Modelle gefunden.")
            print("Verfügbare Modelle:")
            for i, m in enumerate(models):
                print(f"  [{i}] {m['id']}")
            index = int(input("Modellnummer wählen: "))
            return models[index]['id']
        except Exception as e:
            print("Fehler beim Laden der Modelle:", e)
            raise

    def send(self, user_message):
        messages = []
        is_mistral = "mistral" in self.model_name.lower()

        if is_mistral and self.system_prompt:
            user_message = f"{self.system_prompt}\n{user_message}"
        elif self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})

        for entry in self.history[-self.max_history:]:
            messages.append({"role": "user", "content": entry["user"]})
            messages.append({"role": "assistant", "content": entry["assistant"]})

        messages.append({"role": "user", "content": user_message})

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer lm-studio"
        }

        payload = {
            "model": self.model_name,
            "messages": messages,
            "temperature": 0.7,
            "stream": True
        }

        try:
            with requests.post(self.endpoint_url, headers=headers, json=payload, stream=True) as response:
                response.raise_for_status()
                full_response = ""
                in_think_block = False
                last_token_time = time.time()

                print("KI: ", end="", flush=True)
                for line in response.iter_lines():
                    if line:
                        now = time.time()
                        # if now - last_token_time > 1.5:
                        #     print("⏳", end="", flush=True)
                        last_token_time = now

                        line_str = line.decode("utf-8")
                        if line_str.startswith("data: "):
                            line_str = line_str[6:]
                        if line_str.strip() == "[DONE]":
                            break
                        try:
                            delta = json.loads(line_str)
                            content = delta["choices"][0]["delta"].get("content", "")

                            # Farbliche Hervorhebung bei <think>-Blöcken
                            if "<think>" in content:
                                in_think_block = True
                                content = content.replace("<think>", f"{COLOR_THINK}<think>")
                            if "</think>" in content:
                                in_think_block = False
                                content = content.replace("</think>", f"</think>{COLOR_ASSISTANT}")

                            color = COLOR_THINK if in_think_block else COLOR_ASSISTANT
                            print(f"{color}{content}{COLOR_RESET}", end="", flush=True)
                            full_response += content
                        except json.JSONDecodeError:
                            pass
                print()
                self.history.append({"user": user_message, "assistant": full_response})
                return full_response
        except Exception as e:
            print("Fehler bei der Anfrage:", e)
            return None
