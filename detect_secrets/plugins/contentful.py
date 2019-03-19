"""
This plugin searches for Contentful tokens
"""
from __future__ import absolute_import

import re

from .base import RegexBasedDetector


class ContentfulDetector(RegexBasedDetector):

    secret_type = 'Contentful Token'

    blacklist = (
        re.compile(r'CFPAT-[0-9a-zA-Z]{64}', flags=re.IGNORECASE),
    )
