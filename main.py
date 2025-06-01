import os
from autogen import ConversableAgent, UserProxyAgent, AssistantAgent
from dotenv import load_dotenv

load_dotenv()
# llm_config = {
#     "config_list": [
#         {
#             "model": "phi3:mini",
#             "base_url": "http://localhost:11434",
#             "api_type": "ollama",
#         }
#     ],
#     "temperature": 0.1,
#     "max_tokens": 4048,
#     "top_p": 0.95,
# }
llm_config = {
    "config_list": [
        {
            "model": "gemini-1.5-pro",
            "api_type": "google",
            "api_key": os.getenv("GOOGLE_API_KEY"),
        }
    ],
    "temperature": 0.1,
    "max_tokens": 4048
}
# agent = ConversableAgent(
#     name="Mistral Agent",
#     system_message=f"You are a helpful assistant using the {model} model.",
#     llm_config=llm_config,
#     code_execution_config=False,
#     human_input_mode="ALWAYS"
# )
# print("Agent initialized with model:", model)
# response = agent.generate_reply(messages=[{"role": "user", "content": "What is the capital of France? Give me a brief answer."}])
# print("Response from agent:")
# print(response["content"])
assistant = AssistantAgent(
    name="Assistant",
    llm_config=llm_config
)

user_proxy_agent = UserProxyAgent(name="user",
                                  llm_config=llm_config,
                                  system_message="You are a user who interacts with the assistant to perform tasks. You will never do unnecssary discussions, always have the end goal in mind.",
                                  human_input_mode="NEVER",
                                  code_execution_config={
                                      "work_dir": "coding",
                                      "use_docker": False
                                  })
user_proxy_agent.initiate_chat(assistant, message="Plot a chart of Microsoft, META and TESLA stock prices for the last 30 days. show the chart in a popup using PySimpleGUI. Finally tell me which has the best P/E ratio")
