# -*- coding: utf-8 -*-
import json
from collections import namedtuple


class json2obj():

    def __init__(self,data):
        return json.loads(data, object_hook=self._json_object_hook)

    def _json_object_hook(d):
        return namedtuple('X', d.keys())(*d.values())
