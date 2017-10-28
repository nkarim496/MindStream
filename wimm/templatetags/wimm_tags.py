from django import template
from wimm.models import Wimm


register = template.Library()


@register.inclusion_tag('wimm/nav_days.html')
def navigation(current_day):
    data = {}
    if current_day:
        data['days'] = Wimm.objects.filter(pub_date__year=current_day.year, pub_date__month=current_day.month, show=True).datetimes('pub_date', 'day', 'ASC')
        data['months'] = Wimm.objects.filter(pub_date__year=current_day.year, show=True).datetimes('pub_date', 'month', 'ASC')
        data['current_day'] = current_day
    return data
