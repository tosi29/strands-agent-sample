import os
from dotenv import load_dotenv
from strands import Agent
from strands_tools import calculator
from strands.models.openai import OpenAIModel
from portkey_ai import PORTKEY_GATEWAY_URL


load_dotenv()

model = OpenAIModel(
    client_args={
        "api_key": os.environ["PORTKEY_API_KEY"],
        "base_url": PORTKEY_GATEWAY_URL
    },
    model_id="@google/gemini-2.5-flash-lite",
)

agent = Agent(model=model, tools=[calculator])
result = agent("こんにちは")
