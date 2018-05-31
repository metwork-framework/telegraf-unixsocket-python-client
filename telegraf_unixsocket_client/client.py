import os
import stat
import socket
from telegraf_unixsocket_client import line_protocol

DEFAULT_UNIX_SOCKET_TIMEOUT = 10


def check_unix_socket(unix_socket_path):
    try:
        mode = os.stat(unix_socket_path).st_mode
        return stat.S_ISSOCK(mode)
    except Exception:
        return False


class TelegrafUnixSocketClientException(Exception):

    pass


class TelegrafUnixSocketClient(object):

    unix_socket_path = None
    unix_socket_timeout = DEFAULT_UNIX_SOCKET_TIMEOUT
    tags = None
    _sock = None

    def __init__(self, unix_socket_path,
                 unix_socket_timeout=DEFAULT_UNIX_SOCKET_TIMEOUT,
                 tags={}):
        self.unix_socket_path = unix_socket_path
        self.unix_socket_timeout = unix_socket_timeout
        self.tags = tags

    def connect(self, bypass_unix_socket_check=False):
        if not bypass_unix_socket_check:
            if not check_unix_socket(self.unix_socket_path):
                raise TelegrafUnixSocketClientException(
                    "The path: %s is not an unix socket" %
                    self.unix_socket_path)
        if self._sock is not None:
            return True
        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._sock.settimeout(self.unix_socket_timeout)
        self._sock.connect(self.unix_socket_path)

    def close(self):
        if self._sock:
            self._sock.close()
            self._sock = None

    def send_measurement(self, name, fields_dict, extra_tags={},
                         timestamp=None, precision=None):
        if not self._sock:
            raise TelegrafUnixSocketClientException(
                "This client is not connected, please call connect() method "
                "before sending measurements")
        data = {}
        if len(self.tags) > 0:
            data['tags'] = self.tags.copy()
            data['tags'].update(extra_tags)
        else:
            if len(extra_tags) > 0:
                data['tags'] = extra_tags
        data['measurement'] = name
        point = {}
        point['fields'] = fields_dict
        if timestamp is not None:
            point['time'] = timestamp
        data['points'] = [point]
        msg = line_protocol.make_lines(data, precision)
        self._sock.sendall(msg.encode('utf8'))
