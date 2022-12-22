import openai
import configparser

# Read the config file
config = configparser.ConfigParser()
config.read("config.ini")

# Set up the OpenAI API client
openai.api_key = config.get("API", "key")

# Get the prompt from the user
prompt = input("Enter your prompt: ")

# Get the model name from the config file
model = config.get("GPT-3", "model")

# Get the maximum number of tokens from the config file
max_tokens = config.getint("GPT-3", "max_tokens")

# Get the number of completions from the config file
n = config.getint("GPT-3", "n")

# Get the stop sequence from the config file if it exists
if config.has_option("GPT-3", "stop"):
    stop = config.get("GPT-3", "stop")
else:
    stop = None

# Get the temperature from the config file
temperature = config.getfloat("GPT-3", "temperature")

# Set up the parameters for the GPT-3 request
completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=max_tokens, n=n,stop=stop,temperature=temperature)

# Get the first completion response
response = completions.choices[0].text

# Get the number of tokens used for the response
prompt_tokens = completions.usage.prompt_tokens
response_tokens = completions.usage.completion_tokens
total_tokens = completions.usage.total_tokens

# Print the number of tokens used
print(f"Prompt tokens: {prompt_tokens}")
print(f"Response tokens: {response_tokens}")
print(f"Total tokens: {total_tokens}")

# Print the response
print(response)

# Save the prompt and response to a text file
with open("responses.txt", "a") as file:
    file.write(f"Prompt: {prompt}\n")
    file.write(f"Response: {response}\n")
