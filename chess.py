import play

class Cell(play.Box):

    def __init__(self, color='black', x=0, y=0, width=100, height=200, border_color='light blue', border_width=0, transparency=100, size=100, angle=0, row = 0, column = 0, free = True):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._border_color = border_color
        self._border_width = border_width

        self._transparency = transparency
        self._size = size
        self._angle = angle
        self._is_clicked = False
        self._is_hidden = False
        self.physics = None

        self.row = row
        self.column = column
        self.free = free

        self._when_clicked_callbacks = []

        self._compute_primary_surface()

        play.all_sprites.append(self)

class Figure(Sprite):
    can_move = False
    potentional_moves = []
    row_position = int
    column_position = int
    
    def set_free(self):
        self.free = True
    def set_using(self):
        self.free = False

def create_field():
    
    def color(i, j):

        if i%2==0 and j%2==0:
            return "white"
        if i%2==0 and j%2!=0:
            return "black"
        if i%2!=0 and j%2==0:
            return "black"
        if i%2!=0 and j%2!=0:
            return "white"

    color_desk = [[color(i, j) for i in range(8)]for j in range(8) ]
    cell_desk = [[None for i in range(8)]for j in range(8) ]

    x_pos = -200
    y_pos = 400
    step = 80

    for row in range(8):
        for column in range(8):

            color = color_desk[row][column]
            cell = Cell(color = color, x = x_pos-step, y = y_pos-step, 
                        width = step,  height = step,  row = row,         
                        column = column)

            cell_desk.append(cell)
            x_pos += step
        y_pos -= step
        x_pos = -200

    return cell_desk

play.screen.width = 1200
play.screen.height = 900
play.set_backdrop("light blue")

field = create_field()

play.start_program()