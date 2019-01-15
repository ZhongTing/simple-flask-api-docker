def try_get(data_dict, *keys_or_indexes, default=None):
    # noinspection PyBroadException
    try:
        current = data_dict
        for key_or_index in keys_or_indexes:
            current = current[key_or_index]
        return current
    except Exception:
        return default
