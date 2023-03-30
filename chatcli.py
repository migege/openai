#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
#      Filename: chatcli.py
#        Author: lzw.whu@gmail.com
#       Created: 2023-03-28 14:03:50
# Last Modified: 2023-03-30 15:39:02
###################################################
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
import openai

openai.api_key = '<paste your api key here>'


def get_model_list():
    ret = openai.Model.list()
    return ret.data


def make_text_completion(prompt):
    kwargs = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 2048,
        "temperature": 0,
    }
    res = openai.Completion.create(**kwargs)
    return res


class ChatSession(object):

    def __init__(self, content="You are an AI assistant developed by OpenAI"):
        self.messages = [{"role": "system", "content": content}]

    def chat(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        kwargs = {
            "model": "gpt-3.5-turbo",
            "messages": self.messages,
            "max_tokens": 2048,
            "temperature": 0.3,
        }
        res = openai.ChatCompletion.create(**kwargs)
        # print(res)
        message = res.choices[0].message
        assert message.role == 'assistant'
        self.messages.append(message)
        return message.content

    def reset(self, content):
        if content and content.strip():
            self.__init__(content)
        else:
            self.__init__()


def do_text_completions():
    print("--- input your prompt, input ^D as END ---")
    prompt = sys.stdin.read()
    print("--- requesting ---")
    completion = make_text_completion(prompt)
    print(completion)
    print("--- completion ---")
    print(completion.choices[0].text)


def do_chat_completions():
    chat = ChatSession()
    while True:
        print("--- input your prompt, input ^D as END ---")
        prompt = sys.stdin.read()
        if prompt.startswith("!reset"):
            try:
                system = propmpt.split(":", 1)[1]
            except:
                system = None
            chat.reset(system)
            print("--- chat session reset ---")
            continue
        print("--- ping ---")
        res = chat.chat(prompt)
        print("--- pong ---")
        print(res)


def main():
    print("--- getting model list ---")
    models = get_model_list()
    for model in models:
        print("id: {id}".format(**model))

    do_chat_completions()


if __name__ == '__main__':
    main()
