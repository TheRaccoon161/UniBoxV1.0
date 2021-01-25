def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('default', '/default')
    config.add_route('home_info', '/info')
    config.add_route('admin', '/admin')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('tables', '/tables')
    config.add_route('redact', '/redact')
    config.add_route('delete', '/delete')
    config.add_route('update', '/update')
