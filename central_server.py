import rpyc
import constants
from rpyc.utils.server import ThreadedServer


class DBList(rpyc.Service):

    def exposed_registry(self, peer_id, file_name):
        pass

    def exposed_search(self, file_name):
        pass

if __name__ == "__main__":
    server = ThreadedServer(DBList, hostname=constants.SERVER, port=constants.PORT)
    print("Server starts")
    server.start()
