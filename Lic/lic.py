from uuid import UUID, getnode
from hashlib import md5


# return md5 value
def lic_value(key):
    mac = UUID(int=getnode()).hex[-12:]
    mac = ":".join([mac[e:e+2] for e in range(0, 11, 2)])
    md5_key = key + mac

    h = md5()
    h.update(md5_key.encode('utf-8'))
    return h.hexdigest()

