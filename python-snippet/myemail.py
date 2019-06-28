from email import EmailFeedingService


class MyEmail(EmailFeedingService):

    def _update(self, provider, update):
        self.provider = provider
        self.update = update
        d = {
            'provider': provider,
            'update': update,
        }
        return d


if __name__ == '__main__':
    m = MyEmail()
    print(m._update('provedor', 'atualizar'))
