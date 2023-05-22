
from .densityprofile import DensityProfile
from .... import util
from typeguard import typechecked

from plasmas import pre_foil_plasma
from plasmas import post_foil_plasma


@typechecked
class Foil(DensityProfile):
    """
    Directional density profile wth thickness and pre- and 
    post-plasma lengths and cutoffs
    """

    density_si = util.build_typesafe_property(float)
    """density at every point in space (kg * m^-3)"""

    y_value_front_foil_si = util.build_typesafe_property(float)
    thickness_foil_si = util.build_typesafe_property(float)

    pre_foil_plasma.PlasmaLength = util.build_typesafe_property(float)
    pre_foil_plasma.PlasmaCutoff = util.build_typesafe_property(float)
    post_foil_plasma.PlasmaLength = util.build_typesafe_property(float)
    post_foil_plasma.PlasmaCutoff = util.build_typesafe_property(float)


    def __init__(self):
        # (nothing to do, overwrite from abstract parent)
        pass

    def check(self) -> None:
        if self.density_si <= 0:
            raise ValueError("density must be > 0")
        if self.y_value_front_foil_si < 0:
            raise ValueError("y-value_front must be > or = 0")
        if self.thickness_foil_si <= 0:
            raise ValueError("thickness must be > 0")
        if self.pre_foil_plasma.PlasmaLength < 0:
            raise ValueError("prePlasmaLength must be > or = 0")
        if self.pre_foil_plasma.PlasmaCutoff < 0:
            raise ValueError("prePlasmaCutoff must be > or = 0")
        if self.post_foil_plasma.PlasmaLength < 0:
            raise ValueError("postPlasmaLength must be > or = 0")
        if self.post_foil_plasma.PlasmaCutoff < 0:
            raise ValueError("postPlasmaCutoff must be > or = 0")

    def _get_serialized(self) -> dict:
        self.check()

        return {
            "density_si": self.density_si,
            "y_value_front_foil_si": self.y_value_front_foil_si,
            "thickness_foil_si": self.thickness_foil_si,
            "prePlasmaLength": self.pre_foil_plasma.PlasmaLength,
            "prePlasmaCutoff": self.pre_foil_plasma.PlasmaCutoff,
            "postPlasmaLength": self.post_foil_plasma.PlasmaLength,
            "postPlasmaCutoff": self.post_foil_plasma.PlasmaCutoff
        }
