def read_file(path):
    result = {}
    if path[-4:] == 'json':
        result['data'] = open(path)
        result['format'] = 'json'
    elif path[-4:] == 'yaml' or path[-4:] == '.yml':
        result['data'] = open(path)
        result['format'] = 'yaml'
    return result
