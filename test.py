from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

# res = tavily_search("Best hotels in Indonesia")
# print(res)

res = search_flights("Rencanakan perjalanan 7 hari ke Australia dari Indonesia")
print(res)
