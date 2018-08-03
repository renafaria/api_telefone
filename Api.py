from service.api_service import ApiService
from flask import Flask
from config.api import API
import logging


app = Flask(__name__)
file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/', methods=['GET'])
def get():
    return ApiService().get()


@app.route('/telefone/<string:empresa>', methods=['GET'])
def telefone(empresa):
    return ApiService().get_telefone(empresa)


if __name__ == '__main__':
    app.run(host=str(API["host"]), port=int(API["port"]), debug=bool(API["debug"]))
