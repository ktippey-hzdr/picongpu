class pre_foil_plasma:

    def __init__(self, 
                 PlasmaLength: float,
                 PlasmaCutoff: float):
        self.PlasmaLength = PlasmaLength
        self.PlasmaCutoff = PlasmaCutoff

    def check(self) -> None:
        if self.PlasmaLength <= 0:
            raise ValueError("prePlasmaLength must be >0")
        if self.PlasmaCutoff < 0:
            raise ValueError("prePlasmaCutoff must be >=0")

    def _get_serialized(self) -> dict:
        self.check()

        return {
            "PlasmaLength": self.PlasmaLength,
            "PlasmaCutoff": self.PlasmaCutoff
        }

class post_foil_plasma:

    def __init__(self, 
                 PlasmaLength: float,
                 PlasmaCutoff: float):
        self.PlasmaLength = PlasmaLength
        self.PlasmaCutoff = PlasmaCutoff

    def check(self) -> None:
        if self.PlasmaLength <= 0:
            raise ValueError("postPlasmaLength must be >0")
        if self.PlasmaCutoff < 0:
            raise ValueError("postPlasmaCutoff must be >=0")

    def _get_serialized(self) -> dict:
        self.check()

        return {
            "PlasmaLength": self.PlasmaLength,
            "PlasmaCutoff": self.PlasmaCutoff
        }