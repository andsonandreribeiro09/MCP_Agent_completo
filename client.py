import requests

class MCPClient:
    def __init__(self, url):
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
