import os

from mitmproxy.tools import (
    cmdline,
    dump)
from mitmproxy.tools._main import run

import http_tools.settings as settings


def run_module(mode, project_name, host, port, upstream):
    flow_file = os.path.join(settings.FLOWS_DIR, project_name + '.flow')
    arguments = [
        '--listen-host', host,
        '--listen-port', str(port)]
    if upstream:
        arguments.extend([
            '-k', '-m',
            'upstream:{}'.format(upstream)])
    if mode == 'capture':
        arguments.extend([
            '--scripts', 'http_tools/modules/capture.py',
            '--save-stream-file', flow_file,
            '--flow-detail', '0'])
    elif mode == 'intercept':
        arguments.extend([
            '--scripts', 'http_tools/modules/interceptor.py'])
    elif mode == 'repeat':
        arguments = [
            '-n',
            '--client-replay', flow_file]
        if upstream:
            arguments.extend([
                '-k', '-m',
                'upstream:{}'.format(upstream)])
    run(dump.DumpMaster, cmdline.mitmdump, arguments, {})
