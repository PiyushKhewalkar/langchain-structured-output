from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import List, Literal
from pydantic import BaseModel, Field

load_dotenv()

class Event(BaseModel):
    time: str = Field(description="time of the event")
    attendees: List[str] = Field(description= "name of the people attending this event")
    day: str
    type: str = Field(description="type of the event... eg. casual, business, ...")
    multipleAttendees: Literal["yes", "no"] = Field(description="are then more than 1 attendees attending this event? If yes, say true else false")

model = ChatOpenAI()

structured_model = model.with_structured_output(Event)

result = structured_model.invoke("Piyush and Amit is going to attend a party at saturday at 5 in afternoon")

print(result)