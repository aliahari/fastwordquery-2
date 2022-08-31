# -*- coding:utf-8 -*-
import re
import os
from ..base import *



@register([u'Biamooz', u'Biamooz'])
class Biamooz(WebService):

    def __init__(self):
        super(Biamooz, self).__init__()

    def _get_from_api(self):
                
        result = {
            'tranFa': [],
        }

        # farsi translation
        
        data = self.get_response(
            u"https://dic.b-amooz.com/de/dictionary/w?word={}".format(self.quote_word))
        soup = parse_html(data)
        contents = []
        elements = soup.find_all('h2', attrs={"class": "mdc-typography--headline6"})
        for element in elements:
            contents += (element.contents + ["<br>"])
        result['tranFa'] = u''.join((str(e)) for e in contents)
        
        return self.cache_this(result)


    @export([u'tranFa', u'tranFa'])
    def fld_tranFa(self):
        return self._get_field('tranFa')
