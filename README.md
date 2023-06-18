# CCBridge
![Header](https://github.com/EzraApple/ccbridge/blob/main/Readme%20Logo.png)
#### Bridging the Gap between Customer and Company

## Creators
- My name is Ezra Apple and I am 3rd year EECS major at UC Berkeley. I worked on the python scripts that allow the user to chat with the service rep bot. I am very interested in natural language processing and how you can integrate LLMs into various fields and applications. Add me on [LinkedIn](https://www.linkedin.com/in/ezraapple/).
- Hi, I'm Srikaran Nimmagadda (Sri) and I atttend UC Merced as an CSE major. I worked as the prompt engineer and as the website developer for the hosting of the project. I have a deep interest in Web Development, AI and Blockchain technologies. I hope to continue to grow in both skill and as a person. Connect with me on [LinkedIn](https://www.linkedin.com/in/snimmagadda9/).
- Hello! My name is Ian Pagador and I'm a 3rd year CSE major at UC Merced. In this project, I worked on training and implementing the speech recognition model using Azure SDK as well as designing theme and logo elements. I am interested in Deep Learning, Neural Networks, and Computer Vision. Connect with me on [LinkedIn](linkedin.com/in/ian-venedict-pagador-965600227/).
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
***
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
REPRESENTATIVE: Hello Barack, it's Bridgie from Maple Travel Agency. I'm so glad you're back with us! I'm happy to help you with anything you need. How can I help you today?

CUSTOMER: I was looking to leave a review with you guys.

REPRESENTATIVE: Sure thing, Barack! We would love to hear your feedback. Please feel free to leave us a review at review@tlta.com. We really appreciate it! If you have any other questions or needs, don't hesitate to let me know.

CUSTOMER: Actually I also was thinking about scheduling another trip with you guys.

REPRESENTATIVE: Absolutely! We would love to help you with your next trip. We have a wide range of options available, from cultural exploration to relaxing beach getaways. If you'd like to speak with one of our agents to get started, please give us a call at (123) 456-7890. We look forward to helping you plan your perfect trip!

CUSTOMER: I'd like to speak to a manager or supervisor regarding an issue I encountered during my previous trip. How can I reach them?

REPRESENTATIVE: Of course, Barack. We apologize for any inconvenience you experienced on your previous trip. We would be more than happy to connect you with a manager or supervisor to discuss the issue further. Please call (111) 222-3333 to speak to one of our supervisors. They will be happy to help you.

CUSTOMER: I could use some advice on choosing a destination for my next vacation. Can you provide any recommendations?

REPRESENTATIVE: Absolutely, Barack! Based on what you told us, it sounds like a cultural exploration would be the perfect fit for your next vacation. We have a variety of amazing destinations that offer a range of cultural experiences, from historical sites to local art and cuisine. If you need any help deciding, our agents would be more than happy to provide personalized advice and suggestions. Please feel free to call us at (123) 456-7890 or visit our website for more information. We look forward to helping you find the perfect destination for your next vacation!

CUSTOMER: Do you have any specific recommendations?

REPRESENTATIVE: Of course! We recommend destinations such as Barcelona, Spain, which you previously visited and rated 5/5. We also recommend destinations such as Rome, Italy for its amazing architecture and cultural sites, or Tokyo, Japan for its unique cuisine and vibrant culture. We have plenty of other great options as well, so please feel free to call us at (123) 456-7890 or visit our website to explore our full selection of destinations. We look forward to helping you find the perfect destination for your next vacation!
***
## Website
The website serves as an informative hub, providing project details without requiring any coding knowledge. I initially built it using Notion and Canva, which allowed for a user-friendly interface and efficient content creation. It has proven to be a great resource for anyone looking to learn more about our project. However, during the development process, I faced certain challenges that I aim to address in the future.

One of the main aspirations for the future is to leverage a proper full-stack framework in order to take the project to the next level. By adopting a comprehensive approach, we can enhance the functionality and user experience of the website. This includes incorporating front-end and back-end technologies to create a seamless and robust system.

In collaboration with my team, we have outlined a plan to further develop the project over the next few months. This involves acquiring proficiency in various technologies essential for full-stack development. Key areas of focus include JavaScript, a versatile programming language widely used for web development, as well as Tailwind CSS, a popular utility-first CSS framework that streamlines the design process.

Additionally, we aim to delve into the world of React, a powerful JavaScript library for building user interfaces. By harnessing its component-based architecture, we can create interactive and dynamic elements on the website. Complementing React, we plan to learn Node.js, a server-side JavaScript runtime environment, to handle the back-end functionalities effectively.

To ensure efficient data management, we intend to gain expertise in MongoDB, a flexible and scalable NoSQL database. Its document-based structure aligns well with the project's requirements, allowing us to store and retrieve data seamlessly.

[CC Bridge](https://ccbridge.notion.site/ccbridge/CC-Bridge-1007189336a742a9b4f0c501294c2f7b)
***
## Speech Recognition

***
## Future Steps/Ideas
No project is perfect and ours certianily isn't. Here are some improvments we plan on incluidng over the next few months:

1. Multilingual Support: Expand Bridgie's capabilities to provide customer support in multiple languages, accommodating a wider range of users and enhancing accessibility.

2. Contextual Understanding: Further develop Bridgie's ability to understand and interpret context from previous interactions, allowing for more personalized and tailored responses.

3. Integration with Customer Data: Integrate Bridgie with customer databases or CRM systems to access relevant customer information, enabling personalized recommendations and proactive support.
