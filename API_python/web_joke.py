import requests
url = 'https://official-joke-api.appspot.com/random_joke'
response =requests.get(url).json()
print(response)
with open('web_joke.html', 'w') as f:
    f.write('<h1>Joke page</h1>\n')
    f.write(f'<p>{response["setup"]}</p>')
    f.write('<hr>')
    f.write(f'<p>{response["punchline"]}</p>')
    f.write('<p>HAHAHAHAHAHA)</p>')
