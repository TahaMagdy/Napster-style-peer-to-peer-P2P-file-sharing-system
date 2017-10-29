import rpyc
import constants


# Peer as a Client
class Peer:

    # Connect to the server
    conn = rpyc.connect(constants.SERVER, constants.PORT)


# Peer as a Server
# Other peers can connect to
class DBList(rpyc.Service):

    def exposed_obtain(self, file_name):
        '''
            * Other peers invoke this method
              to download file_name from this peer
        '''
        pass
