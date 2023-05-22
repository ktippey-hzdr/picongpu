
from .densityprofile import DensityProfile
from .... import util
from typeguard import typechecked

from plasmas.preplasma import exponential_pre_plasma
from plasmas.postplasma import exponential_post_plasma


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

    exponential_pre_plasma.prePlasmaLength = util.build_typesafe_property(float)
    exponential_pre_plasma.prePlasmaCutoff = util.build_typesafe_property(float)
    exponential_post_plasma.postPlasmaLength = util.build_typesafe_property(float)
    exponential_post_plasma.postPlasmaCutoff = util.build_typesafe_property(float)


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
        if self.exponential_pre_plasma.prePlasmaLength < 0:
            raise ValueError("prePlasmaLength must be > or = 0")
        if self.exponential_pre_plasma.prePlasmaCutoff < 0:
            raise ValueError("prePlasmaCutoff must be > or = 0")
        if self.exponential_post_plasma.postPlasmaLength < 0:
            raise ValueError("postPlasmaLength must be > or = 0")
        if self.exponentiexponential_post_plasma.postPlasmaCutoff < 0:
            raise ValueError("postPlasmaCutoff must be > or = 0")

    def _get_serialized(self) -> dict:
        self.check()

        return {
            "density_si": self.density_si,
            "y_value_front_foil_si": self.y_value_front_foil_si,
            "thickness_foil_si": self.thickness_foil_si,
            "prePlasmaLength": self.exponential_pre_plasma.prePlasmaLength,
            "prePlasmaCutoff": self.exponential_pre_plasma.prePlasmaCutoff,
            "postPlasmaLength": self.exponential_post_plasma.postPlasmaLength,
            "postPlasmaCutoff": self.exponential_post_plasma.postPlasmaCutoff
        }
