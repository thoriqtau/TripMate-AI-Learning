from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# res = tavily_search("Best hotels in Indonesia")
# print(res)

# res = search_flights("Rencanakan perjalanan 7 hari ke Australia dari Indonesia")
# print(res)

user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input,
    thread_id="test_user"
)

print("\n FINAL RESPONSE:\n")
print(response["answer"])
