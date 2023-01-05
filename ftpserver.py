from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
import os

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", os.getcwd()+"/ftpserver/logged", perm="elradfmwMT")
authorizer.add_anonymous(os.getcwd()+"/ftpserver/nobody")
address = ("0.0.0.0", 21)  # listen on every IP on my machine on port 21
handler = FTPHandler
handler.authorizer = authorizer
server = servers.FTPServer(address, handler)
server.serve_forever()