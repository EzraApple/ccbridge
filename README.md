# CCBridge
![Header](https://github.com/EzraApple/ccbridge/blob/main/Readme%20Logo.png)
#### Bridging the Gap between Customer and Company

## Creators
- My name is Ezra Apple and I am 3rd year EECS major at UC Berkeley. I worked on the python scripts that allow the user to chat with the service rep bot. I am very interested in natural language processing and how you can integrate LLMs into various fields and applications. Add me on [LinkedIn](https://www.linkedin.com/in/ezraapple/).
- Hi, I'm Srikaran Nimmagadda (Sri) and I atttend UC Merced as an CSE major. I worked as the prompt engineer and as the website developer for the hosting of the project. I have a deep interest in Web Development, AI and Blockchain technoloigies. I hope to continue to grow in bot skill and as a person. Connect with me on [LinkedIn](https://www.linkedin.com/in/snimmagadda9/).
### Background
CCBridge is a project that aims to make conversations between customers and companies more seamless and convenient. By utilizing the OpenAI API, customers can easily send inquiries to the customer service provided by gpt-3 and get feedback without having to wait for long periods of time. We also utilize a database (.csv file for this simple example) to store user data. This data is retrieved and included in a system prompt to gpt3 to provide more context and make the responses more personal than the base language model.

This project is set up with an exmaple company and example users w/data. The company is called "Maple Travel Agency" and seeks to set users up with their ideal vacation. User data includes some basic contact info, family info, some information about previous trips, and various interests.

***
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

#### ChatGPT given the System prompt without user info
CUSTOMER: Hello, I'm planning a trip and I need some assistance.

REPRESENTATIVE: Good day! Thank you for contacting Maple Travel Agency. I'm Bridgie, your dedicated customer service representative. I'm here to assist you with your travel inquiries and ensure a seamless experience. How may I assist you today?CUSTOMER: I'm interested in leaving a review for the exceptional service I received during my recent trip. Where should I send it?

REPRESENTATIVE:That's wonderful to hear that you had a great experience with us! We truly appreciate your feedback. To leave a review, please send it to review@tlta.com. Our team will be delighted to read about your positive experience. Is there anything else I can assist you with?

CUSTOMER: Actually, I have some questions about scheduling a trip. Can you help me with that?

REPRESENTATIVE: Absolutely! I'd be happy to assist you with scheduling your trip. To ensure a personalized experience, I recommend speaking directly with one of our expert agents. Please give us a call at (123) 456-7890, and they will be able to provide you with detailed information and assist you in planning your trip according to your preferences. They have the expertise to guide you through the process and make the necessary arrangements. Is there anything else I can assist you with?

CUSTOMER: I'd like to speak to a manager or supervisor regarding an issue I encountered during my previous trip. How can I reach them?

REPRESENTATIVE: I apologize for any inconvenience you may have experienced during your trip. To address your concerns and provide you with the appropriate assistance, please reach out to our manager or supervisor directly at (111) 222-3333. They will be able to address your concerns and work towards a satisfactory resolution. If there's anything else I can assist you with, please let me know.

CUSTOMER: Thank you for your help. Actually, I could use some advice on choosing a destination for my next vacation. Can you provide any recommendations?

REPRESENTATIVE: Certainly! Choosing a destination for your vacation depends on various factors such as your interests, preferred activities, budget, and time of year. Could you please provide me with some additional details? For example, are you looking for a beach getaway, an adventurous trip, or perhaps a cultural experience? Additionally, any specific countries or regions you're considering, or any preferences regarding the duration of your trip? Based on your preferences, I'll be more than happy to provide you with some tailored recommendations and advice for your next vacation.

#### CCBridge with the user info from the database
***
## Website

***
## Speech Recognition

***
## Future Steps/Ideas
