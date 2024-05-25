from openai import OpenAI
client = OpenAI()

# user_input = "summarize the event name, start time, end time and elapsed time for each event"
user_input = "list all the exceptions"
top_result = ""
with open("D:/log_sample.txt","r") as f:
    top_result = f.read()

#print(top_result)
print(user_input)

analysis_input = f"With the following user input {user_input} please analyze the following this log messages: {top_result}"
analysis = [{"role": "system",
             "content": "You are a Site Reliability Engineer, please review logs messages and suggest the root cause."},
            {"role": "user", "content": analysis_input}]

analysis_response = client.chat.completions.create(
  model="gpt-4",
  messages=analysis,
  temperature=0,
)

print(analysis_response)