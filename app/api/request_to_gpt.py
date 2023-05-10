from gpt4free import Provider, quora
import gpt4free
import os

def request_to_gpt(question, mode):
    response = {
        'you': lambda: gpt4free.Completion.create(Provider.You, prompt=question),
        'poe': lambda: gpt4free.Completion.create(Provider.Poe, prompt=question, token=quora.Account.create(logging=False), model='ChatGPT'),
        'forefront': lambda: gpt4free.Completion.create(Provider.ForeFront, prompt=question, model='gpt-4', token=quora.Account.create(logging=False)),
        'theb': lambda: gpt4free.Completion.create(Provider.Theb, prompt=question)
    }.get(mode)()
    return response