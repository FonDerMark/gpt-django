from gpt4free import Provider, quora, forefront
import gpt4free
import os

gpt_mode = os.environ['GPT_MODE']

def request_to_gpt():
    return {
        'you': lambda question: gpt4free.Completion.create(Provider.You, 
                                                         prompt=question),
        'poe': lambda question: gpt4free.Completion.create(Provider.Poe, 
                                                         prompt=question, 
                                                         token=quora.Account.create(logging=False), 
                                                         model='ChatGPT'),
        'forefront': lambda question: gpt4free.Completion.create(Provider.ForeFront, 
                                                               prompt=question, 
                                                               model='gpt-4', 
                                                               token=quora.Account.create(logging=False)),
        'theb': lambda question: gpt4free.Completion.create(Provider.Theb, 
                                                          prompt=question)
    }.get(gpt_mode, print('wrong mode'))
