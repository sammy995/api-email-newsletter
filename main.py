import requests as rq
import send_email

api_key ="7086aa9d73504abb8e735d5ce9ac2ee7"
url = "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey="+ api_key

# make request to url
request = rq.get(url)

# Get contents
content = request.json()

email_body = ""

# iterate over each article
for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None and article["url"] is not None:
        email_body = email_body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + "\n\n"

email_body = email_body.encode("utf-8")

send_email.send_email(email_body)