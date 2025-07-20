from urllib.parse import urlparse


def normalise_url(url):
    parsed_url = urlparse(url)
    normalised_url = f"{parsed_url.netloc.removeprefix('www.')}{parsed_url.path}"
    normalised_url = normalised_url.rstrip("/")
    return normalised_url.lower()
