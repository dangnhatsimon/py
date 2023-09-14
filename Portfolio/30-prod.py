#!/usr/bin/env python3

import bottle

@bottle.route('/')
def start():
    return  f'<html>' \
            '<head><title>Main Page</title></head>' \
            '<body>Welcome!</body>' \
            '</html>'
            
@bottle.route('/users')
def users(usernames):
    return  f'<html>' \
            f'<head><title>Users</title></head>' \
            f'<body>These are our users: {usernames}</body>' \
            f'</html>'   
        
# This is the log file used by the /logs site to display logs
LOGFILE = '/var/log/site.log'

@bottle.route('/logs')
def logs():
    with open(LOGFILE) as f:
        return  f'<html>' \
                f'<head><title>Logs</title></head>' \
                f'<body><h1>Recent Logs</h1>' \
                f'<hr/>' \
                f'<pre>{f.read()}</pre>' \
                f'<hr/>' \
                f'</body>' \
                f'</html>'  

# This starts the webserver with all of the configured pages
app=bottle.default_app()

# To enable debugging information, uncomment this line and reload uwsgi
# bottle.debug()
