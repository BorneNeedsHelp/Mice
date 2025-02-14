from datetime import datetime, timedelta, UTC
import base64
import json
import urllib.parse

class MiceError_IntError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)
class MiceError_StrError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)
class MiceError_BoolError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)
class MiceError_DictError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

class Mice:
    @staticmethod
    def create_cookie(user_id: str, max_age_seconds=None, domain=None, path="/", http_only=True, secure=True,
                      same_site="Lax", **extra_data):

        if not isinstance(user_id, str):
            raise ValueError('user_id must be a str')

        if max_age_seconds is not None and not isinstance(max_age_seconds, int):
            raise ValueError('max_age_seconds must be an int')

        if domain is not None and not isinstance(domain, str):
            raise ValueError('domain must be a str')

        if not isinstance(http_only, bool):
            raise ValueError('http_only must be a bool')

        if not isinstance(secure, bool):
            raise ValueError('secure must be a bool')

        if not isinstance(same_site, str):
            raise ValueError('same_site must be a str')

        cookie = f"Set-Cookie: user_id={urllib.parse.quote(user_id)}; Path={path}"

        if max_age_seconds:
            expiry_time = (datetime.now(UTC) + timedelta(seconds=max_age_seconds)).strftime("%a, %d %b %Y %H:%M:%S GMT")
            cookie += f"; Expires={expiry_time}; Max-Age={max_age_seconds}"

        if domain:
            cookie += f"; Domain={domain}"

        if secure:
            cookie += "; Secure"

        if http_only:
            cookie += "; HttpOnly"

        if same_site:
            cookie += f"; SameSite={same_site}"

        for key, value in extra_data.items():
            cookie += f"; {key}={urllib.parse.quote(str(value))}"

        return cookie

    @staticmethod
    def encode_cookie_data(data: str):
        json_data = json.dumps(data)
        encoded_data = base64.b64encode(json_data.encode()).decode()

        return encoded_data

    @staticmethod
    def decode_cookie_data(data: str):
        decoded_json = base64.b64decode(data).decode()
        decoded_data = json.loads(decoded_json)

        return decoded_data
