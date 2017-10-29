import rpyc
import constants
from rpyc.utils.server import ThreadedServer


class DBList(rpyc.Service):


if __name__ == "__main__":
    server = ThreadedServer(DBList, hostname = constants.SERVER, port = constants.PORT)
    print("Server starts")
    server.start()
