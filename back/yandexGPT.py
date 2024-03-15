import requests
import json
from time import sleep


class YandexGPT:
    def __init__(self):
        self.yandex_cloud_catalog = "b1gmasb9gep76ibr32ga"
        self.yandex_gpt_api_key = "AQVN2kypilSivP_FGODoaobvzAmweoeI4l0LKsks"
        self.yandex_gpt_model = "yandexgpt"
        self.system_prompt = "Ты опытный ментор, который выстаивает траекторию поступления в определенный вуз по полученным характеристикам школьника. Формат ответа: Университеты в этом городе, курсы для сдачи ЕГЭ, курсы для развития в профессии, возможные профессии. "
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {self.yandex_gpt_api_key}",
            "x-folder-id": self.yandex_cloud_catalog,
        }
        self.body = {
            "modelUri": f"gpt://{self.yandex_cloud_catalog}/{self.yandex_gpt_model}",
            "completionOptions": {"stream": False, "temperature": 0.6, "maxTokens": "2000"},
            "messages": [{"role": "system", "text": None},
                         {"role": "user", "text": None}
                        ]
        }
        self.url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completionAsync"

    def post(self, prompt: str):
        self.body["completionOptions"] = {"stream": False, "temperature": 0.6, "maxTokens": "2000"}
        self.body["messages"][0]["text"] = self.system_prompt
        self.body["messages"][1]["text"] = prompt
        response = requests.post(self.url, headers=self.headers, json=self.body)
        response_json = json.loads(response.text)
        operation_id = response_json["id"]
        url = f"https://llm.api.cloud.yandex.net/operations/{operation_id}"
        headers = {"Authorization": f"Api-Key {self.yandex_gpt_api_key}"}
        done = False
        while not done:
            response = requests.get(url, headers=headers)
            response_json = json.loads(response.text)
            done = response_json["done"]
            sleep(0.5)
        answer = response_json["response"]["alternatives"][0]["message"]["text"]
        return answer



#gpt = YandexGPT()
#print(gpt.post("Санкт-петербург, бэкенд разработчик, 11 класс"))
