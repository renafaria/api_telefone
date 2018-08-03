from flask import jsonify
import requests


class ApiService:

    @staticmethod
    def get():
        response = jsonify({
                    'projeto': 'Api Telefone',
                    'data': '02/08/2017',
                    'descricao': 'Busca e retorna o telefone de uma empresa'
        })
        response.status_code = 200
        return response

    @staticmethod
    def get_telefone(empresa):
        page_source = requests.get('https://www.google.com/search?q={empresa}+telefone&oq={empresa}+telefone'
                                   .format(empresa=empresa.replace(' ', '+'))).text
        return ''
