#!/usr/bin/python

from config import BaseConfig, BoolOption, IntOption, Option, ConfigError, read_config, ListOption

class CMConfig(BaseConfig):
    listen_addr = Option('')
    listen_port = IntOption(51235)
    cadir = Option('/etc/pki/func/ca')
    certroot =  Option('/var/lib/func/certmaster/certs')
    csrroot = Option('/var/lib/func/certmaster/csrs')
    autosign = BoolOption(False)

class FuncdConfig(BaseConfig):
    overlord_server = Option('funcmaster')
    log_level = Option('INFO')
    certmaster = Option('http://certmaster:51235/')
    cert_dir = Option('/etc/pki/func')