import pytest
from report_app.web_report import *

client = app.test_client()


def test_home():
    response = client.get('/')
    assert response.status_code == 200


def test_common_statistic():
    response = client.get('/report/?order=asc')
    assert response.status_code == 200


def test_common_statistic_desc():
    response = client.get('/report/?order=desc')
    assert response.status_code == 200


def test_show_drivers():
    response = client.get('/report/drivers/')
    assert response.status_code == 200


def test_show_drivers_statistics():
    response = client.get('/report/drivers/?driver_id=DRR')
    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main()
