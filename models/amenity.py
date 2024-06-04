#!/usr/bin/python3
"""Amenity module"""
from models.base_model import BaseModel


def Amenity(BaseModel):
    """Amenity class for AirBnB"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
