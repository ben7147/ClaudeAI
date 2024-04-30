import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
)

message2 = input("Kérdezz bármit! ~ ")

message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": message2
                }
            ]
        }
    ]
)
print(message.content)
