from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
import os

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", os.getcwd()+"/TPBINOME/get_ftp", perm="elradfmwMT")
authorizer.add_anonymous(os.getcwd()+"/TPBINOME/post_ftp")
address = ("0.0.0.0", 21)  # listen on every IP on my machine on port 21
handler = FTPHandler
handler.authorizer = authorizer
server = servers.FTPServer(address, handler)
server.serve_forever()