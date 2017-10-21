# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from arxiv_cli.core import _build_filename, _get_id


def test_build_filename():
    assert _build_filename('cond-mat/0607501v2') == 'cond-mat-0607501v2.pdf'
    assert _build_filename('1111.2011v2') == '1111.2011v2.pdf'


def test_get_id_with_old_id():
    entry_with_old_id = {'id': 'http://arxiv.org/abs/cond-mat/0607501v2'}

    expected = 'cond-mat/0607501v2'
    result = _get_id(entry_with_old_id)

    assert expected == result


def test_get_id_with_new_id():
    entry_with_new_id = {'id': 'http://arxiv.org/abs/1111.2011v2'}

    expected = '1111.2011v2'
    result = _get_id(entry_with_new_id)

    assert expected == result
