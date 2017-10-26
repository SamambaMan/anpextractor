import httpretty
import pytest
from ..manager import (
    do_request_station_list,
    extract_stations_id,
    endpoint)

@httpretty.activate
def test_do_request_station_list():
    httpretty.register_uri(httpretty.POST, endpoint,
                           data={'sEstado': 'SP'},
                           status=200)

    assert do_request_station_list('ES').status_code == 200

@pytest.mark.integration
def itest_do_request_station_list_integrated():
    assert do_request_station_list('ES').status_code == 200

@httpretty.activate
def test_extract_stations_id(stations_list):
    assert len(extract_stations_id(stations_list)) == 200

@pytest.mark.integration
def itest_extract_stations_id_integrated():
    extract_stations_id(do_request_station_list("SP").content)
