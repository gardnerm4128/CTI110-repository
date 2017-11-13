#CTI 110
#M5T1B
#Matthew Gardner
#10/11/17

def main():
    import turtle
    ivan = turtle.Turtle()

    #ivan.penup()
    #ivan.forward(90)
    #ivan.left(45)
    #ivan.pendown()
    def branch():
        for i in range(3):
            for i in range(3):
                    ivan.forward(30)
                    ivan.backward(30)
                    ivan.right(45)
            ivan.left(90)
            ivan.backward(30)
            ivan.left(45)
            ivan.right(90)
            ivan.forward(90)
        for i in range(8):
                    branch()
                    ivan.left(45)




















#strt prrm
main()
