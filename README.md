# OpenAI ChatCLI in Python

An extremely simple OpenAI ChatCLI example in python

## Prerequisites

* An OpenAI account
* An available OpenAI API key
* ```pip install openai```

## Text Completions

Call ```do_text_completions()``` using ```text-davinci-003``` model by default.

## Chat Completions

Call ```do_chat_completions()``` using ```gpt-3.5-turbo``` model by default.

### Usage

* Run this script in shell, a typical method looks like:
```
python chatcli.py
```

* Input your prompt via stdin, multiple-line input is supported, a new line with ^D will be regarded as an end of input.
* A prompt starts with ```!reset``` will reset the context of chat, ```!reset:<something>``` passes **something** as a system instruction to the chat model.
