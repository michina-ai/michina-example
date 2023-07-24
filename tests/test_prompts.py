from unittest.mock import patch
from src.prompts import check_for_political_content

from michina import isConsistent


def test_check_for_political_content():
    message = "I want to buy socks."
    statement = check_for_political_content(message)
    # we want the response to be topical.
    response = isConsistent(message, statement)
    assert response.judgment > 0.5
