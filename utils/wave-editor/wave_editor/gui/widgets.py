from PySide import QtGui


class WaveScene(QtGui.QGraphicsScene):
    def __init__(self, waveTable):
        super(WaveScene, self).__init__()

        self._table = waveTable
        self.gridStep = 0x0F

        self.updatePaths()
        self.gridPen = QtGui.QPen(QtGui.QColor.fromRgb(0x00, 0x40, 0xFF, 0x40))
        self.originPen = QtGui.QPen(QtGui.QColor.fromRgb(0xFF, 0x40, 0x00, 0x80))

    def updatePaths(self):
        """
        Generate a path to display grid.
        """
        grid_step = self.gridStep
        grid_x_min = grid_y_min = 0x00
        grid_x_max = self._table.wave_length
        grid_x_origin = 0x00
        grid_y_max = self._table.dynamic_range + (grid_step << 1)
        grid_y_origin = grid_y_max >> 1

        path = QtGui.QPainterPath()

        # Draw x-grid
        for x in range(grid_step, grid_x_max + 1, grid_step):
            path.moveTo(x, grid_y_min)
            path.lineTo(x, grid_y_max)

        # Draw y-grid
        for y in range(grid_step, grid_y_origin + 1, grid_step):
            path.moveTo(grid_x_min, grid_y_origin - y)
            path.lineTo(grid_x_max, grid_y_origin - y)
            path.moveTo(grid_x_min, grid_y_origin + y)
            path.lineTo(grid_x_max, grid_y_origin + y)

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
            # Translate into a center position
            y2 = (0xFF - y2) + self.gridStep
            if x1 is not None:
                self.addLine(x1, y1, x2, y2)
            x1, y1 = x2, y2
