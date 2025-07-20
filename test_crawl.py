import unittest
from crawl import normalise_url, get_urls_from_html


class TestCrawl(unittest.TestCase):
    # normalise_url function
    def test_normalise_url_protocol(self):
        input_url = "https://blog.boot.dev/path"
        actual = normalise_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalise_url_slash(self):
        input_url = "https://blog.boot.dev/path/"
        actual = normalise_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalise_url_capitals(self):
        input_url = "https://BLOG.boot.dev/path/"
        actual = normalise_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalise_url_http(self):
        input_url = "http://BLOG.boot.dev/path/"
        actual = normalise_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalise_url_www(self):
        input_url = "http://www.blog.boot.dev/path/"
        actual = normalise_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalise_url_empty_path(self):
        input_url = "http://www.blog.boot.dev"
        actual = normalise_url(input_url)
        expected = "blog.boot.dev"
        self.assertEqual(actual, expected)

    def test_normalise_url_query(self):
        input_url = "http://www.blog.boot.dev/path/?query=1"
        actual = normalise_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalise_url_fragments(self):
        input_url = "http://www.blog.boot.dev/path#section"
        actual = normalise_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    # test_get_urls_from_html function
    def test_get_urls_from_html_absolute(self):
        input_url = "https://blog.boot.dev"
        input_html = '<html><body><a href="https://blog.boot.dev"><span>Boot.dev</span></a></body></html>'
        actual = get_urls_from_html(input_html, input_url)
        expected = ["https://blog.boot.dev"]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
