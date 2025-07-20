from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


def normalise_url(url):
    parsed_url = urlparse(url)
    normalised_url = f"{parsed_url.netloc.removeprefix('www.')}{parsed_url.path}"
    normalised_url = normalised_url.rstrip("/")
    return normalised_url.lower()


def get_urls_from_html(html, base_url):
    urls = []
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup.find_all("a")

    for anchor in anchors:
        if href := anchor.get("href"):
            try:
                absolute_url = urljoin(base_url, href)
                urls.append(absolute_url)
            except Exception as e:
                print(f"{str(e)}: {href}")
    return urls
