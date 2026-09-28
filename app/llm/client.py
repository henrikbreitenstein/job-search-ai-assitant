from ollama import chat

class LLMClient:

    def ask(self, prompt):

        response = chat(
            model='qwen3:8b',
            messages=[
                {
                'role' : 'user',
                'content' : prompt
                }
            ]
        )

        return response['message']['content']


