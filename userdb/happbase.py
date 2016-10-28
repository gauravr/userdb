import hug
import redis

from settings import REDIS_HOST, REDIS_PORT, REDIS_SESSIONS_DB

def echo(text: hug.types.text=''):
    return {'text': text}


def enable_echo(api, endpoint='/echo'):
    hug.get(endpoint, api=api)(echo)
    hug.get(endpoint, api=api)(echo)
    hug.post(endpoint, api=api)(echo)
    hug.put(endpoint, api=api)(echo)
    hug.patch(endpoint, api=api)(echo)


def add_resthandlers(url, handlers):
    # get_collection, add_resource, replace_resource, get_resource, edit_resource, delete_resource = handlers
    hug.get(endpoint, api=api)(echo)
    hug.get(endpoint, api=api)(echo)
    hug.post(endpoint, api=api)(echo)
    hug.put(endpoint, api=api)(echo)
    hug.patch(endpoint, api=api)(echo)


#TODO: this will be part of redisutils later
rconn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_SESSIONS_DB)
