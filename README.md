# httptools

## capture | intercept | repeat
httptools helps you to capture, repeat and live intercept HTTP requests with scripting capabilities. It is built on top of [mitmproxy v5](https://mitmproxy.org/)

### Install

```
pip install http-tools
```

### Develop
```
$ git clone https://github.com/MobSF/httptools.git
$ cd httptools
$ python setup.py develop
```

### Usage

```
$ httptools
usage: httptools [-h] [-m MODE] [-p PORT] [-i IP] [-n NAME] [-u UPSTREAM]

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Supported modes
                        1. capture: Capture requests.
                        2. repeat: Repeat captured requests.
                        3. intercept: Intercept and tamper the request.
                        4. server: Start httptools server.
  -p PORT, --port PORT  Proxy Port
  -i IP, --ip IP        Proxy Host
  -n NAME, --name NAME  Project Name
  -u UPSTREAM, --upstream UPSTREAM
                        Upstream Proxy
```

1. Capture - `httptools -m capture`
   * Starts HTTPS proxy at `0.0.0.0:1337` by default.
   * Install Root CA cert from `http://mitm.it/`
2. Repeat - `httptools -m repeat`
   * Replay the captured traffic. Use --upstream to forwatd it to
     a fuzzer like BurpSuite or OWASP ZAP.
3. Intercept - `httptools -m intercept`
   * To Fiddle with HTTP request and response in live.
   * Use: `http_tools/modules/interceptor.py` (The location will be relative to where httptools is installed)
3. Server Web UI - `httptools -m server`
   * Starts the Web UI at `https://0.0.0.0:1337` by default.
