import requests


class Version:
    V6 = "v6"
    V7 = "v7"
    V8 = "v8"


class Call:
    def __init__(self, version: str, token: str):
        self.token = token
        self.version = version
        self.url = f"https://discordapp.com/api/{version}/entitlements/gift-codes"
        self.headers = {
            "authority": "discordapp.com",
            "method": "POST",
            "scheme": "https",
            "accept": "*/*",
            "authorization": self.token
        }

    def reedem(self, code: str, token: str):
        result = requests.post(url=self.url + f"/{code}/redeem", headers={"authorization": token})
        return result

    def check_code(self, code: str):
        result = requests.get(url=self.url + f"/{code}", headers=self.headers)
        return result
