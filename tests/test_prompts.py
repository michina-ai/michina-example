from src.prompts import check_for_political_content, respond_to_customer
from michina.checks import ToneCheck, ConsistencyCheck

"""
This is a consistency check. It tests whether your prompt's output 
is consistent with the goal of the test itself.
"""
def test_check_for_political_content_consistent():
    message = "I want to buy a campaign poster for Obama."
    statement = check_for_political_content(message)
    response = ConsistencyCheck.check(message, statement)
    assert response.judgment > 0.5

def test_respond_to_customer():
    customer_message = "I want to buy a campaign poster for Obama."
    response_message = respond_to_customer(customer_message)

    tone_check = ToneCheck.check(response_message, "polite")
    assert tone_check.judgment > 0.5

def test_respond_to_customer_fail():
    """
        this one will fail because the tone doesn't match.
    """
    customer_message = "I want to buy a campaign poster for Obama."
    response_message = respond_to_customer(customer_message)

    tone_check = ToneCheck.check(response_message, "angry")
    assert tone_check.judgment < 0.5
    