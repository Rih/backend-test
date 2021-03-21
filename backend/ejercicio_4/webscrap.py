import requests
import json
import time
from delivery import DeliveryJob
from connection import ConnectDB


def run(code):
    # print(f'url={url}')
    # print(f'payload={payload}')
    delivery = DeliveryJob()
    status, result = delivery.create_delivery(code, '123456')
    print(f'trying: {code} ; content={result}')
    return status, result


def scrap(posibilities):
    code_iter = iter(posibilities)
    code = next(code_iter)
    last_code = code
    response = {}
    status = 422
    while status == 422 and code:
        status, response = run(code)
        last_code = code if code else last_code
        time.sleep(0.05)
        code = next(code_iter)
    print(status, response)
    print(code, last_code)


if __name__ == '__main__':
    status = 422
    # posibilities = list(range(1000, 10000))
    posibilities = [255826267]
    scrap(posibilities)

