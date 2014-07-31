#!/usr/bin/env python

"""
* Copyright (c) 2014 Soal <soal@soal.pl>
*
* Icinga/Nagios plugin to check ActiveMQ instance (v0.1, 2014/07/31)
*
* This file is licensed under the General Public License version 2
* See the LICENCE file.
"""

from stompest.config import StompConfig
from stompest.protocol import StompSpec
from stompest.sync import Stomp
import time
import logging

stomp_config = StompConfig('tcp://localhost:61613')
stomp_queue = '/queue/icingaTestQueue'
stomp_body = str(time.time())
exit_codes = { 'ok': 0, 'warning': 1, 'critical': 2 }

def main():
    logging.basicConfig()
    logging.getLogger().setLevel(logging.WARN)

    client = Stomp(stomp_config)
    client.connect()
    client.send(stomp_queue, body=stomp_body)
    client.subscribe(stomp_queue, {StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT, 'activemq.prefetchSize': 1})
    if client.canRead(timeout=5):
        frame = client.receiveFrame()
        print 'Got %s' % frame.info()
        client.ack(frame)
        frame_body = str(frame.body)
        if frame_body == stomp_body:
            print "OK: Message received"
            status = 'ok'
        else:
            print "WARNING: Incorrect message body; is %s, should be %s" % (frame_body, stomp_body)
            status = 'warning'
    else:
        print "CRITICAL: Timed out while trying to collect the message"
        status = 'critical'
    client.disconnect()
    client.close(flush=True)
    return exit_codes[status]

if __name__ == '__main__':
    exit_code = exit_codes['critical']
    try:
        exit_code = main()
    except:
        print "CRITICAL: No connection to ActiveMQ"

    exit(exit_code)
