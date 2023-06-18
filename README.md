# CCBridge
![Header](https://github.com/EzraApple/ccbridge/blob/main/Readme%20Logo.png)
#### Bridging the Gap between Customer and Company

## Creators
- My name is Ezra Apple and I am 3rd year EECS major at UC Berkeley. I worked on the python scripts that allow the user to chat with the service rep bot. I am very interested in natural language processing and how you can integrate LLMs into various fields and applications. Add me on [LinkedIn](https://www.linkedin.com/in/ezraapple/).
### Background
CCBridge is a project that aims to make conversations between customers and companies more seamless and convenient. By utilizing the OpenAI API, customers can easily send inquiries to the customer service provided by gpt-3 and get feedback without having to wait for long periods of time. We also utilize a database (.csv file for this simple example) to store user data. This data is retrieved and included in a system prompt to gpt3 to provide more context and make the responses more personal than the base language model.

This project is set up with an exmaple company and example users w/data. The company is called "Maple Travel Agency" and seeks to set users up with their ideal vacation. User data includes some basic contact info, family info, some information about previous trips, and various interests.

## Command Line ChatBot
#### Requirements
In order to use CCBridge, you will need the following:
- OpenAI API Key 
- Install the required libraries with `pip install -r requirements.txt`

#### OpenAI API Key
In order to use CCBridge, you will need an OpenAI API Key. You can obtain one [here](https://openai.com/blog/openai-api).

#### How to Use
Using CCBridge is easy. Follow these steps:

1. Sign up for an OpenAI API Key
2. Paste your API Key into the provided field in generate_response.py
3. To start a conversation from the command line run `python3 customer_service.py`
4. You will be prompted for an ID number, 0-9 are example users in the .csv user database
5. You can exit the chat at any time by saying "exit"
***
## Website

## Speech Recognition

## Future Steps/Ideas
