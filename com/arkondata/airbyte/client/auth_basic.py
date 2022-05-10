import urllib3


class Urllib3AuthBasic:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def make_auth_basic(self, headers: dict = None):
        invalid = ["", None, {}]
        user = self.user
        password = self.password
        if user not in invalid and password not in invalid:
            fmt_auth = f'{user}:{password}'
            header = urllib3.make_headers(basic_auth=fmt_auth)
            ###header['Content-Type'] = self.content_type if self.content_type not in invalid else 'application/json'
            if headers not in invalid:
                if 'authorization' in headers:
                    del headers['authorization']
                header.update(headers)
            return header
        else:
            raise Exception("No user or password was found")
