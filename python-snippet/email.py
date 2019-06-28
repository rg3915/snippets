class FeedingService(object):
    pass


class EmailFeedingService(FeedingService):

    NAME = 'email'

    def _update(self, provider, update):
        config = {}
        server = 'server'
        port = 993
        self.provider = 'provider'
        self.update = 'update'
        d = {
            'config': config,
            'server': server,
            'port': port,
            'provider': provider,
            'update': update
        }

        return d


if __name__ == '__main__':
    e = EmailFeedingService()
    print(e._update('provedor', 'atulizar'))
