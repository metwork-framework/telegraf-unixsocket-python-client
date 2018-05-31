import functools
import unittest
import socket
from telegraf_unixsocket_client import TelegrafUnixSocketClient
from telegraf_unixsocket_client import TelegrafUnixSocketClientException


def fake_socket_constructor(cls, *args, **kwargs):
    return cls(*args, **kwargs)


class FakeSocketObject(object):

    sended = None

    def __init__(self, *args, **kwargs):
        print("plop")
        pass

    def connect(self, *args, **kwargs):
        return True

    def close(self, *args, **kwargs):
        return True

    def settimeout(self, *args, **kwargs):
        return True

    def sendall(self, data, *args, **kwargs):
        self.sended = data
        return True


class TelegrafUnixSocketClientTestCase(unittest.TestCase):

    def test_connect_not_socket(self):
        client = TelegrafUnixSocketClient("/foo/bar")
        try:
            client.connect()
            raise Exception("TelegrafUnixSocketClientException not raised")
        except TelegrafUnixSocketClientException:
            pass

    def test_connect(self):
        orig_constructor = socket.socket
        socket.socket = functools.partial(fake_socket_constructor,
                                          FakeSocketObject)
        client = TelegrafUnixSocketClient("/foo/bar")
        client.connect(bypass_unix_socket_check=True)
        client.close()
        socket.socket = orig_constructor
        self.assertTrue(client._sock is None)

    def test_send1(self):
        orig_constructor = socket.socket
        socket.socket = functools.partial(fake_socket_constructor,
                                          FakeSocketObject)
        client = TelegrafUnixSocketClient("/foo/bar")
        client.connect(bypass_unix_socket_check=True)
        client.send_measurement("foo", {"field1": 1.23, "field2": 4.56})
        self.assertEquals(client._sock.sended,
                          b'foo field1=1.23,field2=4.56\n')
        client.close()
        socket.socket = orig_constructor
