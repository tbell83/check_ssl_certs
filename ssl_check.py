#!/usr/local/bin/python
from socket import socket
from OpenSSL import SSL
import argparse
from sys import exit
import json
from datetime import datetime
from re import search

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', action='store', type=str)
parser.add_argument('-w', '--show-warnings', action='store_true')
args = parser.parse_args()

try:
    with open(args.config, 'r') as config_file:
        config = json.load(config_file)
except:
    exit('No valid config file.')

hostnames = config['hosts']
current_date = datetime.now()

for hostname in hostnames:
    print '\n{}\n-----------'.format(hostname)
    port = hostnames[hostname]
    ctx = SSL.Context(SSL.TLSv1_METHOD)
    sock = socket()
    ssl_sock = SSL.Connection(ctx, sock)
    ssl_sock.set_tlsext_host_name(str(hostname))
    ssl_sock.connect((hostname, port))
    ssl_sock.do_handshake()
    cert_chain = ssl_sock.get_peer_cert_chain()
    for cert in cert_chain:
        if args.show_warnings:
            printing = False
        else:
            printing = True
        sig = 'Signature Algorithm: {}'.format(cert.get_signature_algorithm())
        if search('sha1', sig):
            printing = True
            sig = 'Warning, SHA1 signature:\n' + sig
        tz = cert.get_notAfter()[14:]
        date = datetime.strptime(cert.get_notAfter()[:14], '%Y%m%d%H%M%S')
        expiration = 'Expiration: {}{}\n'.format(date, tz)
        if (date - current_date).days < 90:
            printing = True
            expiration = 'Warning, Certificate expiring soon:\n' + expiration

        if printing:
            print 'Common Name: {}'.format(cert.get_subject().commonName)
            print sig
            print expiration
