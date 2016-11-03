import uuid
import pickle
import settings
import redis


rconn = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_SESSIONS_DB
    )
skey = lambda sid: settings.SEP.join((settings.KEY_PREFIX, sid))


def gen_sid():

    return str(uuid.uuid4())


def create():

    sid = gen_sid()
    return sid


def exists(sid):

    return rconn.exists(sid)


def get(sid, keys=[]):

    if keys:
        s_values = rconn.hmget(skey(sid), keys)
        data = {k:pickle.loads(v) if v else v for k,v in zip(keys, s_values)}
    else:
        s_values = rconn.hgetall(skey(sid))
        if s_values is None:
            s_values = {}
        data = {k.decode('ascii'):pickle.loads(v) for k,v in s_values.items()}
    return data


def get_attribute(sid, attribute):

    value = rconn.hget(skey(sid), attribute)
    return pickle.loads(value) if value else None


def destroy(sid):

    rconn.delete(skey(sid))
    return True


def update(sid, mod_data):

    key = skey(sid)
    mod_data = {k:pickle.dumps(v) for k,v in mod_data.items() if k in settings.SESSION_KEYS}
    rconn.hmset(key, mod_data)
    rconn.expire(key, settings.TTL)
    return True


def update_attribute(sid, attribute, value):

    key = skey(sid)
    rconn.hset(key, attribute, pickle.dumps(value))
    rconn.expire(key, settings.TTL)
    return True


if __name__ == "__main__":

    sid = create()
    print(sid)
    val = get(sid)
    print(val)
    update(sid, {'br': {'9': "h"}})
    print((get(sid)))
    val = get(sid)
    print(val)
