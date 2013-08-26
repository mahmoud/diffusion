# -*- coding: utf-8 -*-

"""
# TODO: Maybe separate Base/Registered/UnregisteredUser classes?
"""


class User(object):
    is_registered = None
    name = None


class StructuredDiff(object):
    # includes size?
    pass


class PageInfo(object):  # In actuality, a WapitiModel
    # title, page_id, ns, source (wiki), subject_id, talk_id
    pass


class Change(object):
    user = None
    diff = None
    diff_size = None
    timestamp = None
    page_info = None  # Wapiti model
    flags = None  # new/bot/minor/unpatrolled
    old_rev_id = None
    cur_rev_id = None
    summary = None

from xml.etree import cElementTree as ET
from HTMLParser import HTMLParser

class ContentDelta(object):
    def __init__(self, html):
        self.html = html

    @classmethod
    def from_html(cls, html_diff):
        html_diff = u'\n'.join([u'<html>', html_diff, u'</html>'])
        et = ET.fromstring(html_diff.encode('utf-8'))
        return cls(et)

    @classmethod
    def from_esc_html(cls, esc_html_diff):
        if not isinstance(esc_html_diff, unicode):
            esc_html_diff = esc_html_diff.decode('utf-8')
        hp = HTMLParser()
        unesc_html = hp.unescape(esc_html_diff)
        return cls.from_html(unesc_html)


def _main():
    with open('../tmp_diff_esc.html') as f:
        esc_html_diff = f.read()
    cd = ContentDelta.from_esc_html(esc_html_diff)
    import pdb;pdb.set_trace()


if __name__ == '__main__':
    _main()
