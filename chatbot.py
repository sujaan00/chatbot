import webbrowser
from datetime import datetime
import urllib.request as url
import bs4
from languages import helloIntent, byeIntent 

chat = True

while chat:
    msg = input("Enter Msg: ").strip().lower()
    if msg in helloIntent:
        print("Hey....")
    elif msg in byeIntent:
        print("Bye....")
    elif msg.startswith("open"):
        site = msg.split()[-1]
        if "." not in site:
            print("Please provide a valid site name (e.g., 'open google').")
        else:
            webbrowser.open(site if site.startswith("http") else f"https://{site}.com")
    elif "time" in msg:
        dt = datetime.now()
        print(dt.strftime("%I:%M:%S,%p"))
    elif "date" in msg:
        dt = datetime.now()
        print(dt.strftime("%d/%m/%y,%a"))
    elif "news" in msg:
        try:
            response = url.urlopen("https://indianexpress.com/")
            data = bs4.BeautifulSoup(response, features="html.parser")
            news_list = data.findAll("div", class_="top-news")[1]
            h3_data = news_list.findAll("h3")
            for i, headline in enumerate(h3_data, 1):
                print(f"{i}. {headline.text}\n\n")
        except Exception as e:
            print("Sorry, couldn't fetch news right now.")
    elif msg in ["exit", "quit"]:
        print("Goodbye!")
        chat = False
    else:
        print("Sorry I didn't understand that. Try 'hello', 'bye', 'news', or 'time'.")