import requests
from bs4 import BeautifulSoup

target_url = "https://saimahadasa.vercel.app/"

# Adding headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

response = requests.get(target_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ""

    # Extract text from both <p> and <span> tags
    for element in soup.find_all(['p', 'span']):
        text += element.get_text()

    # Write the extracted text to a file with UTF-8 encoding
    with open('website_text.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(text)

    print("Text extracted and saved successfully!")

else:
    print(f"Error: Failed to retrieve website content. Status code: {response.status_code}")
