# -*- coding: utf-8 -*-
from userdb import sessions


def test_create_session():

    sid = sessions.create()
    assert type(sid) == str


def test_get_session():

    sid = sessions.create()
    data = sessions.get(sid)
    assert data == {}


def test_get_attribute():

    sid = sessions.create()
    data = sessions.get(sid)
    data['br'] = {'123': '10/05/2016'}
    assert sessions.update(sid, data)

    data = sessions.get(sid)
    assert data['br']['123'] == '10/05/2016'

    value = sessions.get_attribute(sid, 'br')
    assert value['123'] == '10/05/2016'

    value = sessions.get_attribute(sid, 'ar')
    assert value is None


def test_update_session():

    sid = sessions.create()
    data = sessions.get(sid)
    data['br'] = {'123': '10/05/2016'}
    assert sessions.update(sid, data)

    data = sessions.get(sid)
    assert data['br']['123'] == '10/05/2016'

    data['br'] = {'123': '11/05/2016'}
    assert sessions.update(sid, data)

    data = sessions.get(sid)
    assert data['br']['123'] == '11/05/2016'


def test_update_attribute():

    sid = sessions.create()
    assert sessions.update_attribute(sid, 'br', {'123': '10/05/2016'})

    value = sessions.get_attribute(sid, 'br')
    assert value['123'] == '10/05/2016'

    assert sessions.update_attribute(sid, 'br', {'123': '11/05/2016'})

    value = sessions.get_attribute(sid, 'br')
    assert value['123'] == '11/05/2016'


def test_delete_session():

    sid = sessions.create()
    data = sessions.get(sid)
    data['br'] = {'123': '10/05/2016'}
    assert sessions.update(sid, data)

    data = sessions.get(sid)
    assert data['br']['123'] == '10/05/2016'

    assert sessions.destroy(sid)

    data = sessions.get(sid)
    assert data == {}
