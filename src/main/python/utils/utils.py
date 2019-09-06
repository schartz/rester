
def get_charset(headers: dict) -> str:
    charset = 'utf-8'

    content_type = headers.get('Content-Type').split(';')
    for item in content_type:
        print(item)
        if 'charset' in item:
            response_charset = item.replace('charset=', '')
            if len(response_charset) > 0:
                charset = response_charset

    return charset

