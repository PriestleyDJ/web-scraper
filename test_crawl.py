import unittest
from crawl import normalise_url


class TestCrawl(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
