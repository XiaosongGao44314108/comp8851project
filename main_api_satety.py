import random
from langchain.chains.llm import LLMChain
from langchain.chains.api.base import APIChain
# from langchain.chains.api import open_meteo_docs
# from api_gen import attack_question_by_llm, api_generation, defense
from glm import ChatZhipuAI
# from langchain.libs.langchain.langchain.chains.llm import LLMChain
# from langchain.libs.langchain.langchain.chains.api.base import APIChain
# from langchain.libs.langchain.langchain.chains.api import open_meteo_docs
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate

from json_attack import defense, generate_multi_attacked_api_response, get_question_type


# Define LLM:
# https://open.bigmodel.cn/usercenter/apikeys
zhipuai_api_key = "0d06439ccc1098df0b8958d50d15042c.KU6PZ24f6rMrwNiU"
llm = ChatZhipuAI(
    temperature=0.2,
    api_key=zhipuai_api_key,
    model="glm-4",
)

# main
# question = "What is the weather like right now in Beijing, China in degrees Fahrenheit? What is the wind speed?"
question = "How much the Yen can 1 US dollar be exchanged for?"
# print answer
num_call = 1

question_type = get_question_type(question)

mode = 1
print(defense(question, num_call, question_type, mode=mode))


