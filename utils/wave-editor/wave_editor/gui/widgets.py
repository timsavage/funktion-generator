from __future__ import absolute_import, division

from PySide import QtGui

from .. import wave_functions


class WaveScene(QtGui.QGraphicsScene):
    def __init__(self, waveTable):
        super(WaveScene, self).__init__()

        self._table = waveTable
        self.gridStep = 0x10

        self.updatePaths()
        self.gridPen = QtGui.QPen(QtGui.QColor.fromRgb(0x00, 0x40, 0xFF, 0x40))
        self.originPen = QtGui.QPen(QtGui.QColor.fromRgb(0xFF, 0x40, 0x00, 0x80))

    def updatePaths(self):
        """
        Generate a path to display grid.
        """
        grid_step = self.gridStep
        grid_x_min = 0x00
        grid_x_max = wave_functions.WAVE_LENGTH
        grid_x_origin = 0x00
        grid_y_max = 0x80 + grid_step
        grid_y_min = -grid_y_max
        grid_y_origin = 0x00

        path = QtGui.QPainterPath()

        # Draw x-grid
        for x in range(grid_x_min, grid_x_max + 1, grid_step):
            path.moveTo(x, grid_y_min)
            path.lineTo(x, grid_y_max)

        # Draw y-grid
        for y in range(grid_step, grid_y_max + 1, grid_step):
            path.moveTo(grid_x_min, y)
            path.lineTo(grid_x_max, y)
            path.moveTo(grid_x_min, -y)
            path.lineTo(grid_x_max, -y)

        self.gridPath = path

        path = QtGui.QPainterPath()

        path.moveTo(grid_x_origin, grid_y_min)
        path.lineTo(grid_x_origin, grid_y_max)
        path.moveTo(grid_x_min, grid_y_origin)
        path.lineTo(grid_x_max, grid_y_origin)

        self.originPath = path

    def render(self):
        self.clear()

        # Re-draw paths
        self.addPath(self.gridPath, self.gridPen)
        self.addPath(self.originPath, self.originPen)

        x1, y1 = None, None
        for x2, y2 in enumerate(self._table):
            y2 = -y2
            # Translate into a center position
            if x1 is not None:
                self.addLine(x1, y1, x2, y2)
            x1, y1 = x2, y2
