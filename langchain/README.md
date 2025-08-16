# Langchain POC
Using local ollama as a llm server.

# Setup 
### Run Ollama
go to ollama documentation to install and pull your first ollama image

below only works for me 🤷‍♂️
```sh
# Run ollama model
ollama run llama3.2:latest
```


### Run code
I should create a scrupt for below, maybe a Makefile also will work 🤔
```sh
# Create new virtual python env
python3 -m venv venv
# activate newly created python env
source venv/bin/activate
# Python requirements
pip3 install -r requirements.txt
# Run program
python3 main.py
```


