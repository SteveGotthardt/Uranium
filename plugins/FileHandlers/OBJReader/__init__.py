# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the AGPLv3 or higher.

#Shoopdawoop
from . import OBJReader

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("uranium")

def getMetaData():
    return {
        "plugin": {
            "name": "Wavefront OBJ Reader",
            "author": "Ultimaker",
            "version": "1.0",
            "description": i18n_catalog.i18nc("OBJ Reader plugin description", "Makes it possbile to read Wavefront OBJ files."),
            "api": 2
        },
        "mesh_reader": {
            "extension": "obj",
            "description": i18n_catalog.i18nc("OBJ Reader file format", "Wavefront OBJ File")
        }
    }

def register(app):
    return { "mesh_reader": OBJReader.OBJReader() }