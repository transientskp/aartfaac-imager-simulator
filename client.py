#!/usr/bin/env python

import socket
import StringIO

import astropy.io.fits.header
import astropy.io.fits

HOSTNAME = 'localhost'
PORT = 2013


def getbytes(socket_, bytes_):
    """Read an amount of bytes from the socket"""
    result = StringIO.StringIO()
    count = bytes_
    while count > 0:
        recv = socket_.recv(count)
        if len(recv) == 0:
            raise Exception("Server closed connection")
        count -= len(recv)
        result.write(recv)
    return result.getvalue()


def main():
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect((HOSTNAME, PORT))
    length = int(getbytes(socket_, 4))
    payload = getbytes(socket_, length)
    fits_ding = astropy.io.fits.PrimaryHDU()
    fits_ding.header = astropy.io.fits.header.Header.fromstring(payload)

if __name__ == '__main__':
    main()