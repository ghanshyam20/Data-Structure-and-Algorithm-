import hashlib

class URLShortener:

    def __init__(self):
        self.code_to_url = {}
        self.url_to_code = {}
        self.click_counts = {}

    def _make_code(self, url, extra=""):
        text = url + extra
        h = hashlib.md5(text.encode()).hexdigest()
        code = h[0:6]
        return code

    def shorten(self, url):
        if url in self.url_to_code:
            return self.url_to_code[url]

        code = self._make_code(url)

        i = 1

        while True:
            if code not in self.code_to_url:
                break
            else:
                if self.code_to_url[code] == url:
                    return code
                else:
                    code = self._make_code(url, str(i))
                    i = i + 1

        self.code_to_url[code] = url
        self.url_to_code[url] = code
        self.click_counts[code] = 0

        return code

    def open_url(self, code):
        if code in self.code_to_url:
            self.click_counts[code] = self.click_counts[code] + 1
            return self.code_to_url[code]
        else:
            return None

    def get_stats(self, code):
        if code in self.code_to_url:
            result = {}
            result["code"] = code
            result["url"] = self.code_to_url[code]
            result["clicks"] = self.click_counts[code]
            return result
        else:
            return None