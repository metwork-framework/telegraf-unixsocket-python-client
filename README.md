# telegraf-unixsocket-python-client

## Status

[![GitHub CI](https://github.com/metwork-framework/telegraf-unixsocket-python-client/workflows/CI/badge.svg?branch=master)](https://github.com/metwork-framework/telegraf-unixsocket-python-client/actions?query=workflow%3ACI+branch%3Amaster)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://github.com/metwork-framework/telegraf-unixsocket-python-client/blob/master/LICENSE)

## What is it ?

A tiny and very limited python client to send metrics to telegraf through an unix socket


## Example

```python
from telegraf_unixsocket_client import TelegrafUnixSocketClient

client = TelegrafUnixSocketClient("/tmp/telegraf.socket")
client.connect()
client.send_measurement("foo", {"field1": 1.23, "field2": 4.56})
client.close()
```

## Notes

This repository includes some [MIT licensed](https://github.com/influxdata/influxdb-python/blob/master/LICENSE) code about influxdb line protocol borrowed from the [influxdb-python](https://github.com/influxdata/influxdb-python) project.
