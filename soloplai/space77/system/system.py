from dataclasses import dataclass
from random import SystemRandom
from importlib import resources as rsrc
import json

from . import tables

@dataclass
class World:
    coords: tuple[int, int]
    starport_class:str
    planet_size:str
    atmosphere:str
    hydrography:str
    population:str
    government:str
    law_enforcement:str
    tech_level:str
    name:str
    description:str

    @classmethod
    def random_world(cls, coords:tuple[int, int]):#->"World":
        rand = SystemRandom()
        params = {}
        with open(str(rsrc(tables)/'starport_classes.json')) as FILE:
            params['starport_class'] = json.load(FILE)[rand.randint(1, 6)+rand.randint(1, 6)]
        return params
