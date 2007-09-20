#!/usr/bin/python

# Virt-factory backend code.
#
# Copyright 2006, Red Hat, Inc
# Michael DeHaan <mdehaan@redhat.com>
# Scott Seago <sseago@redhat.com>
# Adrian Likins <alikins@redhat.com>
#
# This software may be freely redistributed under the terms of the GNU
# general public license.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.


from codes import *
import os
import ConfigParser

CONFIG_FILE = "/etc/func/settings"

class Config:

    # this class is a Borg
    __shared_state = {}
    has_read = False

    def __init__(self):
        self.__dict__ = self.__shared_state
        if not self.has_read:
            self.read()
            Config.has_read = True

    def read(self):

        if not os.path.exists(CONFIG_FILE):
            raise FuncException(comment="Missing %s" % CONFIG_FILE)

        cp = ConfigParser.ConfigParser()

        self.ds["is_master"] = int(cp.get("general","is_master"))
        self.ds["is_minion"] = int(cp.get("general","is_minion"))
        self.ds["master_server"] = cp.get("general","master")

    def get(self):
        return self.ds


