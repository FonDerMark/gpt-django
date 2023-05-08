from gpt4free import Provider, quora, forefront
import gpt4free
import os

gpt_mode = os.environ['GPT_MODE']

def request_to_gpt(question):
    return {
        'you': lambda: gpt4free.Completion.create(Provider.You, 
                                                         prompt=question),
        'poe': lambda: gpt4free.Completion.create(Provider.Poe, 
                                                         prompt=question, 
                                                         token=quora.Account.create(logging=False), 
                                                         model='ChatGPT'),
        'forefront': lambda: gpt4free.Completion.create(Provider.ForeFront, 
                                                               prompt=question, 
                                                               model='gpt-4', 
                                                               token=quora.Account.create(logging=False)),
        'theb': lambda: gpt4free.Completion.create(Provider.Theb, 
                                                          prompt=question)
    }.get(gpt_mode)
