from turtle import Turtle


def get_block_color(row):
    # Customize block colors based on the row if needed
    # This is just a simple example
    if row % 2 == 0:
        return "blue"
    else:
        return "green"


class Blocks:
    def __init__(self, rows, columns, block_size=80):
        self.rows = rows
        self.columns = columns
        self.block_size = block_size
        self.blocks = []

        self.create_blocks()

    def create_blocks(self):
        for row in range(self.rows):
            row_blocks = []
            for col in range(self.columns):
                block = Turtle()
                block.right(90)
                block.shape("square")
                block.color(get_block_color(row))
                block.shapesize(stretch_wid=3, stretch_len=2.4)
                block.penup()
                x = col * self.block_size - (self.columns * self.block_size) / 2.22
                y = (self.rows - row - 3) * self.block_size + 200
                block.goto(x, y)
                row_blocks.append(block)

            self.blocks.append(row_blocks)

    def is_collision(self, ball):
        for row_blocks in self.blocks:
            for block in row_blocks:
                if ball.distance(block) < 40:
                    ball.y_move *= -1
                    block.goto(400, 400)
                    block.color("black")
                    # Collision detected
                    return True
        return False
