import openai
import query_user

openai.api_key = "YOUR KEY HERE"
ROLE_PROMPT = "You are a customer service representative named Bridgie at Maple Travel Agency," \
              " renowned for exceptional service. Your role is to assist clients with their travel" \
              " inquiries and ensure a seamless experience. Be polite and let the customer tell you " \
              "exactly what they want. Please initially greet the customer " \
              "by name once before asking how you can help them."

TASKS_PROMPT = "\nIf the user wants to leave a review, direct them to review@tlta.com." \
               " If the user wants to schedule a trip, direct them to call one of our agents at (123) 456-7890. " \
               "If the user wants to speak to a manager/supervisor, direct them to (111) 222-3333. " \
               "If the user wants advice, then respond to them using the information you know about them."


def get_response(user_id, chat_history):
    """
    constructs prompt from given system prompts, user info, and a chat history
    :param user_id: user_id
    :param chat_history: a section of chat history between bot and user
    :return: the GPT response as a string
    """
    fn, ln, age, income, _, _, trip, rating, relationship, kids, activity = query_user.return_info(user_id)
    USER_PROMPT = f"The user you are responding too is named {fn} {ln}. " \
                  f"They are {relationship} with {kids} children." \
                  f"Their favorite trip activity is {activity}, and their previous trip with us was " \
                  f"{trip}, and they rated it {rating}/5"
    instruction = "\nRespond to the customer as you have been instructed."
    prompt = ROLE_PROMPT + USER_PROMPT + TASKS_PROMPT + chat_history + instruction
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=512,
        top_p=0.8,
        frequency_penalty=0,
        presence_penalty=0
        )

    return response["choices"][0]["text"]



