import rpyc
import constants


class Client:

    # Connect to the server
    conn = rpyc.connect(constants.SERVER, constants.PORT)
