# -*- coding: utf-8 -*-
'''
This is the default pillar exact matcher.
'''
from __future__ import absolute_import, print_function, unicode_literals

import logging
import salt.utils.data  # pylint: disable=3rd-party-module-not-gated

log = logging.getLogger(__name__)


def match(tgt, delimiter=':'):
    '''
    Reads in the pillar match, no globbing, no PCRE
    '''
    log.debug('pillar target: %s', tgt)
    if delimiter not in tgt:
        log.error('Got insufficient arguments for pillar match '
                  'statement from master')
        return False
    return salt.utils.data.subdict_match(__opts__['pillar'],
                                         tgt,
                                         delimiter=delimiter,
                                         exact_match=True)
