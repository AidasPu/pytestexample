from unittest.mock import patch, MagicMock
from function.api_mock import get_only_numbers, API


def test_api_read_only_numbers():
    test_data = ["1,3,4,5,32,ab,c21,v32,v323v,v32","521,532,633,c2c"]
    expected = "1|3|4|5|32|521|532|633"

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data
    with patch('function.api_mock.API', fake_api):
        result = get_only_numbers()
        assert result == expected

