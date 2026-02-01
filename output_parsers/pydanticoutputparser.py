from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

class Schema(BaseModel):
    point_1: str = Field(description="Point 1 of the text")
    point_2: str = Field(description="Point 2 of the text")
    point_3: str = Field(description="Point 3 of the text")
    point_4: str = Field(description="Point 4 of the text")
    point_5: str = Field(description="Point 5 of the text")

parser = PydanticOutputParser(pydantic_object=Schema)

template1 = PromptTemplate(
    template="Create a detailed report about this research paper: {paper} \n {format_instructions}",
    input_variables=["paper"],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

template2 = PromptTemplate(
    template="Write a 5 point summary on the given text: {text} \n {format_instructions}",
    input_variables=["text"],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({
    "paper": "Attension is all you need"
})

print(result)