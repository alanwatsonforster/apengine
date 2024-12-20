import apxo.draw as apdraw
import apxo.element as apelement
import apxo.log as aplog

##############################################################################


class marker(apelement.element):

    ############################################################################

    def __init__(
        self, type, hexcode, azimuth=0, speed=0, altitude=0, name=None, color="black"
    ):
    
        self._name = ""

        aplog.clearerror()
        try:

            if not isinstance(name, str) and name is not None:
                raise RuntimeError("the name argument must be a string or None.")
            if name is None:
                self.logwhenwhat("", "creating marker.")
            else:
                self.logwhenwhat("", "creating marker %s." % name)

            if not type in ["dot", "circle", "square", "blastzone", "barragefire"]:
                raise RuntimeError("invalid marker type.")

            super().__init__(
                name,
                hexcode=hexcode,
                azimuth=azimuth,
                altitude=altitude,
                speed=speed,
                color=color,
            )

            self._type = type

        except RuntimeError as e:
            aplog.logexception(e)
        self.logbreak()

    #############################################################################

    def ismarker(self):
        return True

    #############################################################################

    def _startgameturn(self):
        pass

    def _endgameturn(self):
        pass

    ############################################################################

    def _draw(self):

        zorder = self.altitude() + 1
        if self._type == "dot":

            apdraw.drawdot(*self.xy(), size=0.1, fillcolor=self.color(), zorder=zorder)

        elif self._type == "circle":

            apdraw.drawcircle(
                *self.xy(), size=0.65, linecolor=self.color(), linewidth=2
            )
            if self.name() is not None:
                apdraw.drawtext(
                    *self.xy(),
                    self.facing(),
                    self.name(),
                    color=self.color(),
                    zorder=zorder
                )

        elif self._type == "square":

            apdraw.drawsquare(
                *self.xy(),
                size=0.65,
                linecolor=self.color(),
                linewidth=2,
                facing=self.facing(),
                zorder=zorder
            )
            if self.name() is not None:
                apdraw.drawtext(
                    *self.xy(), self.facing(), self.name(), color=self.color()
                )

        elif self._type == "blastzone":

            apdraw.drawblastzone(
                *self.xy(),
                self.altitude()
            )

        elif self._type == "barragefire":

            apdraw.drawbarragefire(
                *self.xy(),
                self.altitude()
            )
