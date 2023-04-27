import openai
openai.api_key=''
completion=openai.ChatCompletion.create(
    model='gpt-3.5-Turbo',
    messages=[{'role':'assistant','content':'hello'}]
)
print(completion)
