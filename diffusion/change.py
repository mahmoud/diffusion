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
