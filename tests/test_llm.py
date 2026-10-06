from app.llm.client import LLMClient

client = LLMClient()

response = client.ask(
    'What is machine learning?'
)

print(response)
