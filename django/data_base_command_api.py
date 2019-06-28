from django.core.management.base import BaseCommand
from optparse import make_option
from datetime import datetime, timedelta as td


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--since',
                    default='2015-06-01 00:00:00',
                    help='Since'),
        make_option('--until',
                    default='2015-06-22 23:59:59',
                    help='Until'),
    )

    def converte_data(self, arg):
        return datetime.strptime(arg, '%Y-%m-%d %H:%M:%S')

    def diff_data(self, since, until):
        data_dict = []

        delta = until - since

        for i in range(delta.days + 1):
            d1 = since + td(days=i)
            d2 = since + td(days=i, hours=23, minutes=59)
            data_dict.append(
                {'data_ini': d1, 'data_fim': d2})
        return data_dict

    def handle(self, since, until, *args, **kwargs):
        since = self.converte_data(since)
        until = self.converte_data(until)
        list_dates = self.diff_data(since, until)

        for i in list_dates:
            print(i['data_ini'], i['data_fim'])
