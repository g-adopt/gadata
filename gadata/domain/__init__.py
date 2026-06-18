"""Pure domain layer: value objects and entities with no I/O or HTTP."""
from gadata.domain.region import Region
from gadata.domain.borehole import Borehole, BoreholeCollection
from gadata.domain.stratigraphy import EarthMaterialInterval, StratigraphyInterval
from gadata.domain.construction import ConstructionInterval
from gadata.domain.hydrogeology import HydrogeologyUnit

__all__ = [
    "Region",
    "Borehole",
    "BoreholeCollection",
    "StratigraphyInterval",
    "EarthMaterialInterval",
    "ConstructionInterval",
    "HydrogeologyUnit",
]
