from __future__ import absolute_import, unicode_literals

import logging

from PySide import QtCore
from zeroconf import ServiceBrowser, Zeroconf

logger = logging.getLogger(__name__)
zeroconf = Zeroconf()


class Devices(QtCore.QObject):
    """
    Listener object that listens for new Funktion Gen devices
    """
    serviceAdd = QtCore.Signal((str, ))
    serviceRemove = QtCore.Signal((str, ))

    def __init__(self):
        super(Devices, self).__init__()

        self.browser = ServiceBrowser(zeroconf, "_wave._udp.local.", self)
        self._devices = []

    def _populate(self):
        pass

    def remove_service(self, zeroconf, type_, name):
        logger.info("Service %s removed", name)
        self.serviceRemove.emit(name)

    def add_service(self, zeroconf, type_, name):
        info = zeroconf.get_service_info(type_, name)
        print("Service %s added, service info: %s" % (name, info))
        self.serviceAdd.emit(name)

