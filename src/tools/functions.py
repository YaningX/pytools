import json, requests, urllib2


try:
    from config import Config
except ImportError:
    from config_sample import Config



def get_config(key):
    ret = Config
    for arg in key.split("."):
        if arg in ret and isinstance(ret, dict):
            ret = ret[arg]
        else:
            return None
    return ret


def safe_get_config(key, default_value):
    r = get_config(key)
    return r if r is not None else default_value


def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


def post_to_remote(url, post_data, headers=None):
    default_headers = {"content-type": "application/json"}
    if headers is not None and isinstance(headers, dict):
        default_headers.update(headers)
    req = requests.post(url, data=json.dumps(post_data), headers=default_headers)
    resp = json.loads(req.content)

    return convert(resp)


def put_to_remote(url, post_data, headers=None):
    default_headers = {"content-type": "application/json"}
    if headers is not None and isinstance(headers, dict):
        default_headers.update(headers)
    req = requests.put(url, data=json.dumps(post_data), headers=default_headers)
    resp = json.loads(req.content)

    return convert(resp)


def get_remote(url, headers={}):
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url, None, headers)
    resp = opener.open(request)
    return resp.read()


def delete_remote(url, headers=None):
    default_headers = {"content-type": "application/json"}
    if headers is not None and isinstance(headers, dict):
        default_headers.update(headers)

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url, headers=default_headers)
    request.get_method = lambda: 'DELETE'
    opener.open(request)

    return "OK"