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


def get(sid):

    s_values = rconn.hgetall(skey(sid))
    if not s_values:
        return {}

    data = {k.decode('ascii'):pickle.loads(v) for k,v in s_values.items()}
    return data


def destroy(sid):

    rconn.delete(skey(sid))
    return True


def update(sid, mod_data):

    key = skey(sid)
    mod_data = {k:pickle.dumps(v) for k,v in mod_data.items() if k in settings.SESSION_KEYS}
    rconn.hmset(key, mod_data)
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
