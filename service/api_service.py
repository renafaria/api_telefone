from bs4 import BeautifulSoup
from flask import jsonify
import requests
import re


class ApiService:

    def get(self):
        response = jsonify({
                    'projeto': 'Api Telefone',
                    'data': '02/08/2017',
                    'descricao': 'Busca e retorna o telefone de uma empresa'
        })
        response.status_code = 200
        return response

    def get_telefone(self, empresa):
        page_source = requests.get('https://www.google.com/search?q=brasil+{empresa}+telefone+telefone'
                                   '&oq=brasil+{empresa}+telefone+telefone'
                                   .format(empresa=empresa.replace(' ', '+'))).text
        soup = BeautifulSoup(page_source, 'html.parser')
        class_telefone = soup.find_all(True, class_='mrH1y')
        try:
            telefone = class_telefone[0].text
        except IndexError:
            telefone = ''
        if self.__is_telefone(telefone):
            response = jsonify({
                'status': 'OK',
                'busca': empresa,
                'telefone': telefone
            })
        else:
            response = jsonify({
                'status': 'ERRO',
                'busca': empresa,
                'telefone': '',
                'mensagem': 'Telefone não encontrado em nossa busca'
            })
        return response, 200

    @staticmethod
    def __is_telefone(telefone):
        return bool(re.search(re.compile('\d{4,5} *?- *?\d{4}', re.IGNORECASE), str(telefone)))
