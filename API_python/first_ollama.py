from ollama import chat, ChatResponse
from bs4 import BeautifulSoup
import requests
def scrape(url):
    page = requests.get(url).text
    soup=BeautifulSoup(page, 'html.parser')
    paragraphs = soup.find_all('p')
    page_text=''
    for line in paragraphs:
        page_text+=line.text
    return page_text
def post(query):
    response: ChatResponse = chat(model='granite4:1b',messages=[{'role':'user','content':query}])
    return response.message.content


def title(post):
    query = f"Generate a title for the following content:\n{post}"
    response: ChatResponse = chat(model='granite4:1b',messages=[{'role':'user','content':query}])
    return response.message.content
while True:
    url=input("Enter URL to scrape: ")
    text=scrape(url)
    query=f"Write 200 words about the following content:\n{text}"
    response_post=post(query)
    response_title=title(text)
    print(response_title)
    print(response_post)

    with open("blog_post.html","a") as f:
        f.write(f"<h1>{response_title}</h1>\n<p>{response_post}</p>\n") 
