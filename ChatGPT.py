import openai
openai.api_key='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'
completion=openai.ChatCompletion.create(
    model='gpt-3.5-Turbo',
    messages=[{'role':'assistant','content':'hello'}]
)
print(completion)