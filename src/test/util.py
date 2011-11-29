def make_app(global_conf, app_name):
    text = '%s script_name="%%(SCRIPT_NAME)s" path_info="%%(PATH_INFO)s"'
    response_text = text % app_name
    def app(environ, start_response):
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response('200 OK', headers)
        return [(response_text % environ).encode('utf-8')]
    return app

