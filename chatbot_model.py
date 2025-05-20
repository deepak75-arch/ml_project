# chatbot_model.py

def get_chatbot_response(user_input):
    """
    Returns a response explaining the project concept based on user queries.
    """
    user_input = user_input.lower()

    if "project" in user_input or "overview" in user_input:
        return ("Our project analyzes consumer buying patterns using clustering. "
                "It segments customers based on features like Annual Income, Number of Purchases, "
                "Time Spent on Website, and Discounts Availed, providing insights for targeted marketing.")
    elif "clustering" in user_input:
        return ("Clustering is an unsupervised machine learning technique that groups similar data points together. "
                "We use K-Means clustering to identify distinct customer segments in our dataset.")
    elif "annual income" in user_input:
        return (
            "Annual Income is used to gauge a customer's spending power and to differentiate high-value customers from budget-conscious ones.")
    elif "number of purchases" in user_input:
        return (
            "The Number of Purchases indicates how frequently a customer buys products, suggesting their loyalty or engagement level.")
    elif "time spent" in user_input or "website" in user_input:
        return (
            "Time Spent on Website measures customer engagement and helps us understand how interested users are in our offerings.")
    elif "discounts" in user_input:
        return (
            "Discounts Availed shows how responsive customers are to promotions, which can help identify price-sensitive segments.")
    else:
        return ("I'm sorry, I didn't understand that. Please ask another question about the project.")


# For quick local testing:
if __name__ == "__main__":
    while True:
        user_in = input("You: ")
        if user_in.lower() in ["exit", "quit"]:
            break
        print("Bot:", get_chatbot_response(user_in))
