import rpyc
import constants
from rpyc.utils.server import ThreadedServer

peer_port = 2100

# Peer as a Client
# It the server IP and port to connect to {Peer, Centeral Server}
class Peer:

    # Connect to the central server
    conn = rpyc.connect(constants.SERVER, constants.PORT)

    # 1* Register to the centeral server
    # conn.root.exposed_registry(124, "file2", "file5")
    # conn.root.exposed_registry(125, "file2", "file4")

    # 2* Search for a file
    #    it returns the ports of peers which have got the file
    print conn.root.exposed_search("file2")

    # 3* Requesting the file from the selected peer
    # port of the requested peer
    connPeer = rpyc.connect(constants.SERVER, 11111)
    file_name = "file2"
    # peer port in the port of the requesting peer
    file_data = connPeer.root.exposed_obtain(file_name, peer_port)

    newFile = open(file_name, "w")
    newFile.write(file_data)
    newFile.close()



#
# * END CLASS
#


# Peer as a Server
# Other peers can connect to
class DBList(rpyc.Service):

    def exposed_obtain(self, file_name, _port):
        '''
            * Other peers invoke this method
              to download file_name from this peer
        '''
        file = open(file_name, "r")
        return file.read()



#
# * END CLASS
#

# Peer Server starts
#server = ThreadedServer(DBList, hostname=constants.SERVER, 2100)
#print("Peer Server starts")
#server.start()
