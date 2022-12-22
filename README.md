# Overview

This file is a Python script that uses the OpenAI API to get a response from a GPT-3 model, based on a user-provided prompt. The script reads in a configuration file (`config.ini`) and uses the settings specified in the file to make the request to the OpenAI API. It then prints the response, as well as the number of tokens used for the prompt and response, to the console. The script also appends the prompt and response to a text file (`responses.txt`).

# Dependencies

The following libraries are used in this script:

- `openai`: A Python library for interacting with the OpenAI API.
- `configparser`: A built-in Python library for reading configuration files.

# Configuration

The script reads in a configuration file (`config.ini`) to get the following settings:

- `key`: The API key for accessing the OpenAI API.
- `model`: The name of the GPT-3 model to use for generating the response.
- `max_tokens`: The maximum number of tokens to use for the response.
- `n`: The number of completions to generate for the prompt.
- `stop`: (Optional) A sequence of characters that indicates the end of the response.
- `temperature`: A value between 0 and 1 that determines the randomness of the response. A higher temperature results in a more varied response, while a lower temperature results in a more deterministic response.

# Usage

To run the script, you will need to provide an API key and set up the other desired settings in the `config.ini` file. Then, you can run the script using the following command:

```
python gpt.py
```

The script will prompt you to enter a prompt, and it will generate a response based on the settings specified in the configuration file. The response, as well as the number of tokens used for the prompt and response, will be printed to the console. The prompt and response will also be appended to the `responses.txt` file.

# Note

This script requires an internet connection to access the OpenAI API.
