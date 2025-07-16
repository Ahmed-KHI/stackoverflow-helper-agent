import os
import requests
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
# Create your own Custom Search Engine at https://cse.google.com/
# Instructions:
# 1. Go to https://cse.google.com/
# 2. Click "Add" to create a new search engine
# 3. In "Sites to search", add: stackoverflow.com
# 4. Get your Search Engine ID and replace the one below
SEARCH_ENGINE_ID = os.getenv("GOOGLE_CSE_ID")

def search_stackoverflow(query: str, num_results=3) -> str:
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": f"site:stackoverflow.com {query}",
        "num": num_results
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json()
        
        # Debug: Print the API response to understand the structure
        print(f"API Response status: {response.status_code}")
        print(f"API Response keys: {list(results.keys())}")
        
        # Check if there's an error in the response
        if "error" in results:
            error_msg = results["error"].get("message", "Unknown API error")
            return f"❌ Google Search API Error: {error_msg}"
        
        # Check for items in the response
        items = results.get("items", [])
        print(f"Number of items found: {len(items)}")
        
        if not items:
            # More detailed error message
            search_info = results.get("searchInformation", {})
            total_results = search_info.get("totalResults", "0")
            return f"❌ No results found. Total results from Google: {total_results}. Query: '{query}'. Check your Google CSE ID and API key."
        
        snippets = []
        for i, item in enumerate(items):
            title = item.get("title", "No title")
            snippet = item.get("snippet", "No snippet")
            link = item.get("link", "No link")
            print(f"Item {i+1}: {title[:50]}...")  # Debug output
            snippets.append(f"🔹 **{title}**\n{snippet}\n🔗 {link}\n")

        return "\n\n".join(snippets)
    
    except requests.exceptions.RequestException as e:
        return f"❌ Error searching StackOverflow: {str(e)}"
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"
