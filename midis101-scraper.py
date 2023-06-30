import requests
from bs4 import BeautifulSoup

def download_midi(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    midi_links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and "/free-midi/" in href:
            midi_id = href.split("/")[-1]
            download_link = f"https://www.midis101.com/download/{midi_id}"
            midi_links.append(download_link)

    for link in midi_links:
        response = requests.get(link)
        filename = link.split("/")[-1] + ".mid"
        with open(filename, "wb") as f:
            f.write(response.content)

base_url = "https://www.midis101.com/search//pg-"
page_num = 1
while True:
    url = base_url + str(page_num)
    download_midi(url)
    page_num += 1
