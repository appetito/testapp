# -*- coding: utf-8 -*-

from pyramid.view import view_config
from datetime import datetime, date

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'testapp'}


class Model(object):
    def __init__(self, data):
        self.data = data

    def __json__(self, request):
        return self.data


test_data = {
    'now': datetime.now(),
    'some_list': ['Python', 'XML', 'Pyramid'],
    'some_dict': {
        'a': 'string value',
        'b': ['list', 'value'],
        'c': {'nested': 'dictionary'},
        'd': ('a', 3, 'tuple', )
    },
    'some_object': Model('object data')
}


@view_config(name='json_view', renderer='json')
def josn_view(request):
    return test_data


@view_config(name='xml_view', renderer='xml')
def xml_view(request):
    return test_data
