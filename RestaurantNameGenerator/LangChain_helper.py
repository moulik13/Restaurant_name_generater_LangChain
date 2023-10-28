import os
os.environ['OPENAI_API_KEY'] = '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'
from langchain.llms import OpenAI

llm = OpenAI(temperature = 0.6)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant for {cuisine} food, suggest me a fancy name for it'
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template='Suggest some menu items for {restaurant_name} Return it as comma seperated list'
    )

    food_item_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')
    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("indian"))