# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HapusBidang
                                 A QGIS plugin
 Hapus Bidang
                             -------------------
        begin                : 2017-05-13
        copyright            : (C) 2017 by PT Virtua Internasional Pratama
        email                : septinmulatsihrezki@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HapusBidang class from file HapusBidang.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .hapus_bidang import HapusBidang
    return HapusBidang(iface)
