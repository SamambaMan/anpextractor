from flask import Flask
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

endpoint = 'http://anp.gov.br/postos/consulta.asp'

@app.route('/postos/<uf>')
def encode(uf):
 
    return 'content'

def do_request_station_list(uf):
    'Returns a station list request body'
    return requests.post(endpoint,
                         {'sEstado':uf,
                          'hPesquisar': 'PESQUISAR',
                          'sMunicipio':0,
                          'sBandeira':0,
                          'sProduto':0,
                          'sTipodePosto':0})

def extract_stations_id(htmlbody):
    'Returns a list of cnpj and code for a html body'
    soup = BeautifulSoup(htmlbody, "html.parser")

    inputs = soup.find_all(
        name='input',
        attrs={'name': re.compile("i[0-9]+"),
               'type': 'hidden'})

    return [i['value'] for i in inputs]

def do_request_station_detail(station_id):
    'Returns a station detail from it`s id'

    return request.post()

