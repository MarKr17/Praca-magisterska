import sys

from vispy import scene, app, visuals

canvas = scene.SceneCanvas(keys='interactive')
width = 1000
height = 600
canvas.size = width, height

# This is the top-level widget that will hold three ViewBoxes, which will
# be automatically resized whenever the grid is resized.
grid = canvas.central_widget.add_grid()

b=grid.add_view(row=0, col=0, row_span=8)
b.bgcolor = "#dd0000"

board = scene.widgets.ViewBox(parent=b.scene, name='board',
                            margin=2, border_color='w')
board.pos = 0.5, 0.3
board.size = 500, 500
board.bgcolor = 'w'
board.camera = 'panzoom'
board.camera.rect = (0, 0, 1, 1)
board.camera.interactive = False
grid1 = scene.visuals.GridLines(parent=board.scene, scale=(0.5,0.5), color='black')
grid1.set_gl_state('translucent', cull_face=False)

control_panel = grid.add_widget(row=8, col=0)
control_panel.bgcolor = "#0000dd"



canvas.show()

if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()