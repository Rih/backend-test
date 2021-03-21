import requests
import json
import time
URL = 'https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries'
headers = {
    'Accept': 'application/json',
    'Content-Type':'application/json',
    'api-key': 'ea670047974b650bbcba5dd759baf1ed',

}
payload = {
    'shipping_order': {
        'n_packages': '1',
        'content_description': 'ORDEN 255826267',
        'imported_id': '255826267',
        'order_price': '24509.0',
        'weight': '0.98',
        'volume': '1.0',
        'type': 'delivery'
    },
    'shipping_origin': {
        'warehouse_code': '401'
    },
    'shipping_destination': {
        'customer': {
            'name': 'Bernardita Tapia Riquelme',
            'email': 'b.tapia@outlook.com',
            'phone': '977623070'
        },
        'delivery_address': {
            'home_address': {
                'place': 'Puente Alto',
                'full_address': 'SAN HUGO 01324, Puente Alto, Puente Alto'
            }
        }
    },
    'carrier': {
        'carrier_code': '',
        'tracking_number': ''
    }
}


def run(url, payload, code):
    # print(f'url={url}')
    payload['carrier']['carrier_code'] = str(code)
    payload['carrier']['tracking_number'] = '123456'
    # print(f'payload={payload}')

    result = requests.post(url, headers=headers, data=json.dumps(payload))
    status = result.status_code
    content = json.loads(result.content)
    print(f'trying: {code} ; content={content}')
    return status, content


if __name__ == '__main__':
    status = 422
    response = {}
    # posibilities = list(range(1000, 10000))
    posibilities = [255826267]
    code_iter = iter(posibilities)
    code = next(code_iter)
    last_code = code
    while status == 422 and code:
        status, response = run(URL, payload, code)
        last_code = code if code else last_code
        time.sleep(0.05)
        code = next(code_iter)
    print(status, response)
    print(code, last_code)
