import functools
import xmlrpclib
HOST = 'localhost'
PORT = 8069
DB = 'odoo_curso'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
sessions = call('openacademy.session','search_read', [], ['name','seats'])
for session in sessions:
    print "Session %s (%s seats)" % (session['name'], session['seats'])
# 3.create a new session

course_id = call('openacademy.course','search',[('name','=','Course 1')])[0]

print "course_id",course_id

session_id = call('openacademy.session', 'create', {
    'name' : 'My session 1',
    'course_id' : course_id,
    'attendee_ids':[(4,7),(4,3)],
})

print "session_id",session_id
