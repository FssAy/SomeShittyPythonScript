import api
import time
import random
code = ""


def random_code(characters: str, length: int):
    code = ""
    for _ in range(length):
        code += random.choice(characters)
    return code


token_scan = "Bot TOKEN"
token_reedem = "TOKEN"
charset = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
call = api.Call(api.Version.V8, token_scan)

counter = 0
run = True
while run:
    counter += 1
    code = random_code(charset, 16)
    result = call.check_code(code)
    if "Unknown Gift Code" not in str(result.text):
        run = False
    print(f"{counter} | {code} | {result.text}")
    time.sleep(.6)

if not run:
    call.reedem(code, token_reedem)
