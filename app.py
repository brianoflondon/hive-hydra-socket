import logging
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from beem import Hive
import os

# Testnet instead of main Hive
USE_TEST_NODE = True
TEST_NODE = ['http://testnet.openhive.network:8091']

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = os.getenv('SECRET_KEY')

logging.basicConfig(level=logging.INFO,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/')
def index():
    """ Simple page for testing """
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('message')
def url_in(url):
    """ Send a URL and I'll post it to Hive """
    custom_json = {'url': url}
    trx_id, success = send_notification(custom_json=custom_json)
    custom_json['trx_id'] = trx_id
    custom_json['success'] = success
    emit('response', {'data': custom_json})


def send_notification(custom_json, server_account='', wif=''):
    """ Sends a custom_json to Hive
        Expects two env variables, Hive account name and posting key
        HIVE_SERVER_ACCOUNT
        HIVE_POSTING_KEY
        """

    id = 'hive-hydra'

    try:
        if server_account == '':
            server_account = os.getenv('HIVE_SERVER_ACCOUNT')
            pass
        if wif == '':
            wif = [os.getenv('HIVE_POSTING_KEY')]
            pass

        if USE_TEST_NODE:
            h = Hive(keys=wif,node=TEST_NODE)
        else:
            h = Hive(keys=wif)
        h = Hive(keys=wif)

        tx = h.custom_json(id=id, json_data= custom_json,
                            required_posting_auths=[server_account])

        trx_id = tx['trx_id']
        logging.info(f'Transaction sent: {trx_id}')
        return trx_id, True

    except Exception as ex:
        error_message = f'{ex} occurred {ex.__class__}'
        logging.error(error_message)
        trx_id = error_message
        return trx_id, False


if __name__ == '__main__':
    socketio.run(app)