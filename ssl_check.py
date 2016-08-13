#!/usr/local/bin/python
from socket import socket
from OpenSSL import SSL
import argparse
from sys import exit
import json

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', action='store', type=str)
args = parser.parse_args()

try:
    with open(args.config, 'r') as config_file:
        config = json.load(config_file)
except:
    exit('No valid config file.')

hostnames = config['hosts']

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
        print 'Common Name: {}'.format(cert.get_subject().commonName)
        print 'Signature Algorithm: {}'.format(cert.get_signature_algorithm())
        year = cert.get_notAfter()[0:4]
        month = cert.get_notAfter()[4:6]
        day = cert.get_notAfter()[6:8]
        hour = cert.get_notAfter()[8:10]
        minute = cert.get_notAfter()[10:12]
        second = cert.get_notAfter()[12:14]
        date = '{}/{}/{} {}:{}:{}'.format(month, day, year, hour,
                                          minute, second)
        print 'Expiration: {}\n'.format(date)
