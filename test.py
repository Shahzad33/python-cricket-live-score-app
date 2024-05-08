import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "f631d4372amshda1a5d3ec4d22bcp1ddbadjsn83a624c9d8e4"  # Replace with your RapidAPI key
    }
response = requests.get(url, headers=headers)
print(response.json())
  
