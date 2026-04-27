# client.py
import requests

class MCPClient:
    def __init__(self, url="http://127.0.0.1:8000"):
        self.url = url

    def call_tool(self, tool_name, input_data):
        response = requests.post(
            f"{self.url}/execute",
            json={
                "tool_name": tool_name,
                "input": input_data
            }
        )
        return response.json()["result"]