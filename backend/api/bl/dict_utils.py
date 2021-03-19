
def get_attr_by_keys(attr, keys):
    for k in keys:
        if attr.get(k):
            return attr[k]
    raise KeyError('Key not found')
