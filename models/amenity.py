#!/usr/bin/python3
"""Review class Module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Review for BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):

        super().__init__(self, *args, **kwargs)
