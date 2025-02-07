import requests
import json

class PerplexityAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.perplexity.ai/chat/completions"

    def custom_query(self, query):
        """
        Send a custom query to the Perplexity API
        
        Args:
            query (str): The query to send to the API
            
        Returns:
            str: The response from the API
        """
        if not self.api_key:
            return "Error: Perplexity API key not found. Please set the PERPLEXITY_API_KEY environment variable."

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "pplx-7b-online",
            "messages": [{"role": "user", "content": query}]
        }

        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=data
            )
            response.raise_for_status()
            
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content']
            else:
                return "Error: Unable to parse API response"

        except requests.exceptions.RequestException as e:
            return f"Error making request to Perplexity API: {str(e)}"
        except json.JSONDecodeError:
            return "Error: Invalid response from API"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
