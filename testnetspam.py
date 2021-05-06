from datetime import datetime
from beem import Hive
from datetime import datetime
from time import sleep
import os
import json

# Testnet instead of main Hive
USE_TEST_NODE = True
TEST_NODE = ['http://testnet.openhive.network:8091']


# If we're using the test net it has to have transactions

server_account = os.getenv('HIVE_SERVER_ACCOUNT')

wif = [os.getenv('HIVE_POSTING_KEY')]

h = Hive(keys=wif,node=TEST_NODE)

operation_id = 'tick-over-testnet'

while True:
    custom_json = {
        'no agenda': 'in the morning',
        'at' : str(datetime.utcnow())
        }

    tx = h.custom_json(id=operation_id, json_data= custom_json,
                        required_posting_auths=[server_account])
    print(json.dumps(tx, indent=2))
    sleep(60)