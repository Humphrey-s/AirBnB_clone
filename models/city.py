#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):

    state_id = ""
    name = ""

    def __init__(self):

        super().__init__()
