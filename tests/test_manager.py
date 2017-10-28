import httpretty
import pytest
from ..manager import (
    do_request_station_list,
    extract_stations_id,
    endpoint_result,
    endpoint,
    has_next_page,
    extract_station_detail,
    do_request_station_detail,
    get_stations_details_by_uf,
    transform_into_excel)

@httpretty.activate
def test_do_request_station_list():
    httpretty.register_uri(httpretty.POST,
                           endpoint)

    assert do_request_station_list('ES').status_code == 200

@pytest.mark.integration
def test_do_request_station_list_integrated():
    assert do_request_station_list('ES').status_code == 200

@pytest.mark.integration
def test_do_request_station_detail_integrated():
    assert do_request_station_detail(8362).status_code == 200
    print(do_request_station_detail(8362).content)

def test_extract_stations_id(stations_list):
    assert len(extract_stations_id(stations_list)) == 200

@pytest.mark.integration
def test_extract_stations_id_integrated():
    extract_stations_id(do_request_station_list("SP").content)

def test_has_next(stations_list):
    assert has_next_page(stations_list)

def test_doesnt_have_next():
    assert not has_next_page("<html></html>")

def test_extract_station_detail(station_detail):
    assert len(extract_station_detail(station_detail)) == 11

@pytest.mark.integration
def test_get_stations_details_by_uf():
    get_stations_details_by_uf('AC')

@pytest.mark.fulltest
@httpretty.activate
def test_excel_export(station_detail, stations_list):
    httpretty.register_uri(httpretty.POST,
                           endpoint,
                           body=stations_list)
    httpretty.register_uri(httpretty.POST,
                           endpoint_result,
                           body=station_detail)

    stations = get_stations_details_by_uf('AC')
    transform_into_excel('AC', stations)
