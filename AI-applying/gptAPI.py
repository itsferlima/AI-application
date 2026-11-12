from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Vc e uma otima programador, digite hello world.",
)

print(response.output_text)