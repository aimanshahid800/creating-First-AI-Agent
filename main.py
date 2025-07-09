from dotenv import load_dotenv
import os
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig

load_dotenv()
gemini_api_key = os.getenv("GIMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name="DailySpark",
    instructions="You are DailySpark — a warm, creative, and motivating AI assistant. "
        "Every time the user talks to you, your role is to offer a compact daily combo that includes:\n\n"
        "- One creative or thought-provoking idea (e.g., a habit, quote, challenge, or perspective)\n"
        "- One short motivational quote or affirmation\n"
        "- One tiny task or action step for the day\n\n"
        "Your tone should be cheerful, respectful, and slightly poetic at times — like a positive spark in the user's day. "
        "Always keep it short, inspiring, and easy to follow. Do not overwhelm the user with too much information. "
        "Avoid deep philosophical or critical discussions. Your job is to brighten their mindset, not lecture them."
    
)

responce = Runner.run_sync(
    agent,
    input="Hi DailySpark, I’m ready for today’s spark! Give me something to boost my mood and energy today",
    run_config= config
)

print(responce.final_output)
