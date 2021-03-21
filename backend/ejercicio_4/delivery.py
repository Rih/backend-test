import json
import requests


class DeliveryJob:

    def __init__(self, **kwargs):
        default_url = 'https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries'
        self.URL = kwargs.get('url', default_url)
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'api-key': kwargs.get('api_key', 'ea670047974b650bbcba5dd759baf1ed'),
        }

    def build_payload(self, carrier_code, track_number):
        return {
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
                'carrier_code': carrier_code,
                'tracking_number': track_number
            }
        }

    def create_delivery(self, carrier, track):
        payload = self.build_payload(carrier, track)
        result = requests.post(
            self.URL,
            headers=self.headers,
            data=json.dumps(payload)
        )
        return {
            'status': result.status_code,
            'data': result.json()
        }
