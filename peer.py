import rpyc
import constants


class Peer:

    # Connect to the server
    conn = rpyc.connect(constants.SERVER, constants.PORT)
