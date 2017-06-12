# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HapusBidangDialog
                                 A QGIS plugin
 Hapus Bidang
                             -------------------
        begin                : 2017-05-13
        git sha              : $Format:%H$
        copyright            : (C) 2017 by PT Virtua Internasional Pratama
        email                : septinmulatsihrezki@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtGui import *
from qgis.gui import QgsMessageBar
import urllib
import urllib2
import json

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'hapus_bidang_dialog_base.ui'))


class HapusBidangDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(HapusBidangDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def accept(self):
        granted_user = self.cek_user()
        if granted_user:
            self.done(1)

    def cek_user(self):
        # if self.lineEdit_user.text() == "sasa" and self.lineEdit_pas.text() == "ncepncep#1":
        url = 'http://192.168.0.153/wspalu/api/json/reply/UserAppl_Login'
        params = urllib.urlencode({
            'UserName': self.lineEdit_user.text(),
            'Password': self.lineEdit_pas.text(),
            'ApplicationId': '1'
        })
        response = urllib2.urlopen(url, params).read()
        j = json.loads(response)
        hasil = j['Message']

        if hasil == 'Username Tidak Ditemukan':
            QMessageBox.critical(self, "Error", hasil)
            return False
        elif hasil == 'Password Salah':
            QMessageBox.critical(self, "Error", hasil)
            return False
        return True