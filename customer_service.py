import generate_response


def main():
    EXIT_CHAT = False
    chat_history = "Please look over the following conversation between yourself and the customer to inform your response:\n"
    chat_history += "REPRESENTATIVE: Please send me your ID number for verification\n"
    init_response = input("REPRESENTATIVE: Please send me your ID number for verification\nCUSTOMER: ")
    chat_history += f"CUSTOMER: {init_response}\n"
    user_id = int(''.join(c for c in init_response if c.isdigit()))

    while not EXIT_CHAT:
        response = generate_response.get_response(user_id, chat_history)
        print(f"REPRESENTATIVE: {response}\n")
        chat_history += f"REPRESENTATIVE: {response}"
        user_response = input("CUSTOMER: ")
        chat_history += f"CUSTOMER: {user_response}"
        if user_response.lower().find("exit") > -1:
            EXIT_CHAT = True


if __name__ == "__main__":
    main()
