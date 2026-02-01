from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

model = ChatOpenAI()

schema = [
    ResponseSchema(name='fact_1', description = 'Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description = 'Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description = 'Fact 3 about the topic'),
    ResponseSchema(name='fact_4', description = 'Fact 4 about the topic')
]

parser = StructuredOutputParser(schema)

template = PromptTemplate(
    template = "Tell me some facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

prompt = template.format({
    "topic": "Mount everest"
})

response = model.invoke(prompt)

print(response)