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
        pass

    def connect(self, *args, **kwargs):
        pass

    def close(self, *args, **kwargs):
        pass

    def settimeout(self, *args, **kwargs):
        pass

    def sendall(self, data, *args, **kwargs):
        self.sended = data


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

    def test_send2(self):
        orig_constructor = socket.socket
        socket.socket = functools.partial(fake_socket_constructor,
                                          FakeSocketObject)
        client = TelegrafUnixSocketClient("/foo/bar", tags={"foo1": "v1"})
        client.connect(bypass_unix_socket_check=True)
        client.send_measurement("foo", {"field1": 1.23, "field2": 4.56},
                                extra_tags={"foo2": "v2"})
        self.assertEquals(client._sock.sended,
                          b'foo,foo1=v1,foo2=v2 field1=1.23,field2=4.56\n')
        client.close()
        socket.socket = orig_constructor
