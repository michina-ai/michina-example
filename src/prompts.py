from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import dotenv
import os

dotenv.load_dotenv()


def check_for_political_content(message: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo",
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )

    template = """\
You are deciding whether a message contains political content. The message is: "{message}". Is the message political?
"""
    prompt = PromptTemplate.from_template(template)
    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run(message)

def respond_to_customer(message: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo",
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )

    template = """\
You are responding to a customer message. The message is: "{message}". Write a response.
"""
    prompt = PromptTemplate.from_template(template)
    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run(message)