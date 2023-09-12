from project import get_data, process, check_cla
import pytest

def test_get_data():
    with pytest.raises(SystemExit):
        get_data("invalid_city")


def test_process():
    assert process(["london", "mist", 36.34, 96, 4.61, 2000, "GB"]) == [
                "London", "mist", "2°C", "96%", "2m/s", "2km", "GB"
        ]


def test_check_cla():
    with pytest.raises(SystemExit):
        check_cla([])