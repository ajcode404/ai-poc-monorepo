from typing import Annotated
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
import os

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

llm = init_chat_model(
    model = "llama3.2:latest",
    model_provider="ollama"
)

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant: ", value["messages"][-1].content)

stream_graph_updates("User: What is the color of a sky")

while False:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Terminate!")
            break
        stream_graph_updates(user_input)
    except:
        user_input = "waht do you know about langgraph?"
        print("User: "+ user_input)
        stream_graph_updates(user_input)
