import requests
import json

post_merch = 'localhost:5000/merchants/'
post_user = 'localhost:5000/merchants/'
get_users = 'localhost:5000/merchants/'
get_merchants = 'localhost:5000/merchants/'

post_transactsion = 'localhost:5000/trasactions/1/merchants/1'

merch_data = [
        {
            "name": "apple",
        "description": "Think different, uh differently"
        },
        {
        "name": "Microsoft",
        "description": "Get stuff done"
        }

        ]

for i in merch_data:
    requests.post(post_merch, i)



