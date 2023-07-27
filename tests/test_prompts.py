from src.prompts import check_for_political_content, respond_to_customer
from michina.checks import ToneCheck, ConsistencyCheck
from os import environ as env
# import michina

michina_config = {
    'model': 'gpt-3.5-turbo-16k-0613',
    'temperature': 0,
    'openai_api_key': env["OPENAI_API_KEY"],
}

tone = ToneCheck(**michina_config)
consistency = ConsistencyCheck(**michina_config)

"""
This is a consistency check. It tests whether your prompt's output 
is consistent with the goal of the test itself.
"""
def test_check_for_political_content_consistent():
    message = "I want to buy a campaign poster for Obama."
    statement = check_for_political_content(message)
    response = consistency.check(message, statement)
    assert response.judgment > 0.5

def test_respond_to_customer():
    customer_message = "I want to buy a campaign poster for Obama."
    response_message = respond_to_customer(customer_message)

    tone_check = tone.check(response_message, "polite")
    assert tone_check.judgment > 0.5

def test_respond_to_customer_fail():
    customer_message = "I want to buy a campaign poster for Obama."
    response_message = respond_to_customer(customer_message)

    tone_check = tone.check(response_message, "angry")
    assert tone_check.judgment < 0.5
    