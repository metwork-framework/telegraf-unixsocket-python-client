# telegraf-unixsocket-python-client

## Status

[![Travis](https://img.shields.io/travis/metwork-framework/telegraf-unixsocket-python-client.svg)](https://travis-ci.org/metwork-framework/telegraf-unixsocket-python-client)
[![Code Health](https://landscape.io/github/metwork-framework/telegraf-unixsocket-python-client/master/landscape.png)](https://landscape.io/github/metwork-framework/telegraf-unixsocket-python-client/master)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://github.com/metwork-framework/docker-centos-opinionated/blob/master/LICENSE)
[![Maturity](https://img.shields.io/badge/maturity-beta-yellow.svg)](https://github.com/metwork-framework/docker-centos-opinionated)
[![Maintenance](https://img.shields.io/maintenance/yes/2018.svg)](https://github.com/metwork-framework)

## What is it ?

A tiny and very limited python client to send metrics to telegraf through an unix socket


## Example

```python
from telegraf-unixsocket-client import TelegrafUnixSocketClient

client = TelegrafUnixSocketClient("/tmp/telegraf.socket")
client.connect()
client.send_measurement("foo", {"field1": 1.23, "field2": 4.56})
client.close()
```

## Notes

This repository includes some [MIT licensed](https://github.com/influxdata/influxdb-python/blob/master/LICENSE) code about influxdb line protocol borrowed from the [influxdb-python](https://github.com/influxdata/influxdb-python) project.
