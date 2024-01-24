import openai
import csv

# Initialize the OpenAI client with your API key
client = openai.OpenAI(api_key="")

def load_grant_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def find_matching_grants(user_input, grants_data):
    messages = [
        {"role": "system", "content": "Match the following user query with suitable grants based on their summaries. "
                                      "Return their title and URL(s) in the format 'title - url'"
                                      "If the user input does not match a grant, return 'invalid input"},
        {"role": "user", "content": user_input}
    ]

    for grant in grants_data:
        grant_info = f"Grant Name: {grant['Name']}, Summary: {grant['Summary']}, URL: {grant['URL']}"
        messages.append({"role": "system", "content": grant_info})

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )


    output_message = completion.choices[0].message.content
    return output_message


# Main Execution
grant_data = load_grant_data('grants_data.csv')
user_input = input("Enter your grant search description or keywords: ")
matching_grants = find_matching_grants(user_input, grant_data)
print(matching_grants)
