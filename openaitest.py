import openai
openai.api_key = "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"

from openai import OpenAI
client = OpenAI()


response = client.chat.completions.create(
  model="gpt-4o",
  messages=[],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)