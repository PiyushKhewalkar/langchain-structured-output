from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, List, Annotated, Literal

load_dotenv()

class Event(TypedDict):
    time: Annotated[str, "time of the event"]
    attendees: Annotated[List[str], "name of the people attending this event"]
    day: str
    type: Annotated[str, "type of event"]
    multipleAttendees: Annotated[Literal["yes", "no"], "are then more than 1 attendees attending this event? If yes, say true else false"]

model = ChatOpenAI()

structured_model = model.with_structured_output(Event)

result = structured_model.invoke("Piyush and Amit is going to attend a party at saturday at 5 in afternoon")

print(result)