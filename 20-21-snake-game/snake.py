from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]
MOVE_FORWARD = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # criando o atributo e chamando método create_snake
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self): # toda a vez que for criado um objeto, essa função será executada
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def snake_extend(self):
        # adiciona um novo segmento à cobra
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1): # inicia pelo último segmento da cobra e vai até o índice 1 (não inclui o 0)
            # pega as coordenadas dos segmentos à frente
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # atualiza a posição do segmento atual
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_FORWARD)

    # a ordem inversa é necessária porque cada segmento precisa assumir a posição do segmento imediatamente anterior antes que o anterior se mova.

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

