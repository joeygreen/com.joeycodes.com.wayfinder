import pytest
from unittest.mock import patch, Mock
from application import scraper

def test_fetch_html_success():
    url = "http://example.com"
    expected_html = "<html><body>Hello</body></html>"
    mock_response = Mock()
    mock_response.text = expected_html
    mock_response.raise_for_status = Mock()
    with patch("requests.get", return_value=mock_response) as mock_get:
        html = scraper.fetch_html(url)
        mock_get.assert_called_once_with(url, headers=pytest.ANY)
        mock_response.raise_for_status.assert_called_once()
        assert html == expected_html

def test_fetch_html_raises_for_status():
    url = "http://example.com"
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = Exception("HTTP Error")
    with patch("requests.get", return_value=mock_response):
        with pytest.raises(Exception, match="HTTP Error"):
            scraper.fetch_html(url)

def test_check_availability_element_found():
    html = "<html><body><div class='stock'>In Stock</div></body></html>"
    selector = ".stock"
    result = scraper.check_availability(html, selector)
    assert result == "In Stock"

def test_check_availability_element_not_found():
    html = "<html><body><div class='other'>Out of Stock</div></body></html>"
    selector = ".stock"
    result = scraper.check_availability(html, selector)
    assert result == "This item may be in stock."