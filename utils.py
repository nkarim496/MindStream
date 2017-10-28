import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MindStream.settings')

import django

django.setup()
import copy
from minder.models import Mind
from datetime import datetime, timedelta


def minds_lst_builder(username, number_of_days):
    pds = Mind.objects.filter(user__username=username).datetimes('pub_date', 'day', 'DESC')[:number_of_days]
    minds = Mind.objects.filter(user__username=username, pub_date__gte=datetime.now()-timedelta(days=7)).order_by('-pub_date')
    mind_lst = []
    info = []
    for pd in pds:
        for mind in minds:
            if pd.date() == mind.pub_date.date():
                info.append(mind)
        mind_lst.append([pd, copy.copy(info)])
        del info[:]
    return mind_lst

if __name__ == '__main__':
    print('Running utils.py as script')
    print(minds_lst_builder('nkarim496', 7))
