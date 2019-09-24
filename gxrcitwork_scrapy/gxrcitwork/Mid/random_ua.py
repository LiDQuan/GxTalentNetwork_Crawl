import fake_useragent

class RandomUserAgentMiddleware(object):
    def __init__(self, crwaler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = fake_useragent.UserAgent()
        self.ua_type = crwaler.settings.get('RANDOM_UA_TY', 'random')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)
        request.headers.setdefault('User_Agent', get_ua())
        pass