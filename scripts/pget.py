#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "duy <duy at rhizoma dot tk>"
__copyright__ = "GPL v3"

from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.task import react
from twisted.web.client import readBody
from twisted.web.http_headers import Headers

from txsocksx.http import SOCKS5Agent
import argparse

#FIXME: add option to choose headers
common_header = {'User-Agent': [
    		'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0']}

def save_body_to_file(filepath, body):
    with open(filepath, 'w' ) as f:
        f.write(body)

partial = lambda f,  a: lambda b: f(a, b)


def main(reactor):
    parser = argparse.ArgumentParser()
    parser.add_argument('url',  help='url to download')
    parser.add_argument('filepath', nargs='?', help='file path to save the url content')
    args = parser.parse_args()
    # FIXME: filename when url ends in / or doesn't have /
    if not args.filepath:
        filepath = args.url.split('/')[-1] or 'index.html'
 
    #FIXME: detect tor port or add argument option
    torEndpoint = TCP4ClientEndpoint(reactor, '127.0.0.1', 9050)
    agent = SOCKS5Agent(reactor, proxyEndpoint=torEndpoint)
    deferred = agent.request('GET',  args.url,
		Headers(common_header),
		None)
    print "Fetching %s" % args.url
    deferred.addCallback(readBody)
    deferred.addCallback(partial(save_body_to_file,  filepath))
    print "%s saved to file %s" % (args.url,  filepath)
    return deferred

react(main, [])
