#!/usr/bin/env python3

import os
from io import open
import socket

from buildbot_worker.bot import Worker
from twisted.application import service

import multiprocessing


def require_env(key: str) -> str:
    val = os.environ.get(key)
    assert val is not None, "val is not set"
    return val


def setup_worker(application: service.Application, id: int) -> None:
    basedir = f"{require_env('BUILDBOT_DIR')}-{id}"
    os.makedirs(basedir, mode=0o700, exist_ok=True)

    master_url = require_env("MASTER_URL")
    hostname = socket.gethostname()
    workername = f"{hostname}-{id}"

    with open(
        require_env("WORKER_PASSWORD_FILE"), "r", encoding="utf-8"
    ) as passwd_file:
        passwd = passwd_file.read().strip("\r\n")
    keepalive = 600
    umask = None
    maxdelay = 300
    numcpus = None
    allow_shutdown = None

    print(f"worker: {workername}")
    s = Worker(
        None,
        None,
        workername,
        passwd,
        basedir,
        keepalive,
        connection_string=master_url,
        umask=umask,
        maxdelay=maxdelay,
        numcpus=numcpus,
        allow_shutdown=allow_shutdown,
    )
    s.setServiceParent(application)


# note: this line is matched against to check that this is a worker
# directory; do not edit it.
application = service.Application("buildbot-worker")

for i in range(min(multiprocessing.cpu_count(), 8)):
    setup_worker(application, i)
