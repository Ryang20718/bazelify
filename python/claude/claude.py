import requests
import anthropic
import os

def claude_api(data: str, question: str) -> str:
    api_key=os.getenv("ANTHROPIC_API_KEY")
    client = anthropic.Client(api_key)
    response = client.completion(
        prompt=f"{anthropic.HUMAN_PROMPT} {data} {question}?{anthropic.AI_PROMPT}",
        stop_sequences = [anthropic.HUMAN_PROMPT],
        model="claude-v1",
        max_tokens_to_sample=3000)

    if response["exception"] is None:
        print(response["completion"])
        return response
    return ""