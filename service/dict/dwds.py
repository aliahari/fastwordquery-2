# -*- coding:utf-8 -*-
import re
import os
from ..base import *



@register([u'DWDS', u'DWDS'])
class DWDC(WebService):

    def __init__(self):
        super(DWDC, self).__init__()

    def _get_from_api(self):
        
        result = {
            'def': [],
            'pron': [],
        }

        # definition
        data = self.get_response(
            u"https://www.dwds.de/wb/{}".format(self.quote_word))
        soup = parse_html(data)
        element = soup.find('div', attrs={"class": "bedeutungsuebersicht"})
        if element:
            result['def'] = u''.join(str(e) for e in element.contents)
        
        #pronounciation
        element = soup.find('source', attrs={"type": "audio/mpeg"})
        if element:
            audio_url = element.get("src")
            if audio_url:
                result['pron'] = audio_url
     

        return self.cache_this(result)

    @export([u'definition', u'definition'])
    def fld_definate(self):
        return self._get_field('def')

   
    @export([u'pron', u'pron'])
    def fld_pron(self):
        audio_url = self._get_field('pron')
        filename = get_hex_name('TFD', audio_url, 'mp3')
        if os.path.exists(filename) or self.net_download(filename, audio_url):
            return self.get_anki_label(filename, 'audio')
        return ''
