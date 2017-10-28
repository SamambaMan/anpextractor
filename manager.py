import re
import io
from multiprocessing.dummy import Pool
from flask import Flask, send_file
from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

THREADED = True

app = Flask(__name__)

endpoint = 'http://anp.gov.br/postos/consulta.asp'
endpoint_result = 'http://anp.gov.br/postos/resultado.asp'

@app.route('/postos/<uf>')
def encode(uf):
    details = get_stations_details_by_uf(uf)
    wb = transform_into_excel(uf, details)

    out = io.StringIO()
    wb.save(out)
    out.seek(0)

    return send_file(
        out,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        attachment_filename='{}.xlsx'.format(uf),
        as_attachment=True)

def do_request_station_list(uf, page=1):
    'Returns a station list request body'
    return requests.post(endpoint,
                         {'sEstado':uf,
                          'hPesquisar': 'PESQUISAR',
                          'sMunicipio': 0,
                          'sBandeira': 0,
                          'sProduto': 0,
                          'sTipodePosto': 0,
                          'p': page})

def extract_stations_id(htmlbody):
    'Returns a list of cnpj and code for a html body'
    soup = BeautifulSoup(htmlbody, "html.parser")

    inputs = soup.find_all(
        name='input',
        attrs={'name': re.compile("i[0-9]+"),
               'type': 'hidden'})

    return [i['value'] for i in inputs]

def has_next_page(htmlbody):
    'Verify if there is a next page'
    soup = BeautifulSoup(htmlbody, "html.parser")

    return len(soup.find_all(name='input', attrs={'name': 'Submit3'})) > 0

def do_request_station_detail(station_id):
    'Returns a station detail from it`s id'

    return requests.post(endpoint_result,
                         {'Cod_inst':station_id})

def extract_station_detail(htmlbody):
    'Extracts extation details from a response body'

    soup = BeautifulSoup(htmlbody, "html.parser")

    detail_list = soup.find_all(
        name="td",
        attrs={
            'align': 'left',
            'valign': 'top',
            'bgcolor': re.compile(r'\#(d7d7d7|e7e7e7)')
        })

    nstr = lambda s: s or ""

    return [nstr(i.string).replace(u'\xa0', u' ') for i in detail_list]

def get_stations_details_by_uf(uf):
    'Returns a array with all station details by UF'
    def get_station_details(station_id):
        'simplify station detail retrieval'
        return extract_station_detail(do_request_station_detail(station_id).content)

    returned_details = []
    page = 1

    list_page = do_request_station_list(uf, page).content
    details_id = extract_stations_id(list_page)
    pooler = Pool(4)
    while True:
        if THREADED:
            details = pooler.map(get_station_details, details_id)
            returned_details.append(details)
        else:
            for station_id in details_id:            
                returned_details.append(get_station_details(station_id))

        if not has_next_page(list_page):
            break

        page = page + 1
        list_page = do_request_station_list(uf, page).content
        details_id = extract_stations_id(list_page)

    return returned_details

def transform_into_excel(uf, details):
    wb = Workbook()
    ws = wb.active

    for detail in details:
        linha = [uf]+ detail
        ws.append(linha)

    return wb
