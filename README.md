# CCBridge
#### Bridging the Gap between Customer and Company

### Background
CCBridge is a project that aims to make conversations between customers and companies more seamless and convenient. By utilizing the OpenAI API Key, customers can easily send inquiries to the customer service provided by gpt-3 and get feedback without having to wait for long periods of time. We also utilize a database (.csv file for a simple example) to store user data. This data is retrieved and included in a system prompt to gpt3 to provide more context and make the responses more personal than the base language model.

### Requirements
In order to use CCBridge, you will need the following:
- OpenAI API Key 
- Install the required libraries with `pip install -r requirements.txt`

### OpenAI API Key
In order to use CCBridge, you will need an OpenAI API Key. You can obtain one [here](https://openai.com/blog/openai-api).

### How to Use
Using CCBridge is easy. Follow these steps:

1. Sign up for an OpenAI API Key
2. Paste your API Key into the provided field in generate_response.py
3. Enter your inquiry and hit submit
4. After sending your inquiry, you will receive a response from the customer service representative (gpt-3) within seconds.