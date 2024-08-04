import turtle
import math

def draw_pythagoras_tree(branch_length, level):
    if level == 0:
        return

    # Малюємо гілку
    turtle.forward(branch_length)

    # Зберігаємо поточне положення
    position = turtle.pos()
    heading = turtle.heading()

    # Малюємо ліву гілку
    turtle.left(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)

    # Відновлюємо початкове положення
    turtle.penup()
    turtle.setpos(position)
    turtle.setheading(heading)
    turtle.pendown()

    # Малюємо праву гілку
    turtle.right(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)

    # Відновлюємо початкове положення
    turtle.penup()
    turtle.setpos(position)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.backward(branch_length)

def main():
    # Введення рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
    branch_length = 100  # Початкова довжина гілки

    # Налаштування turtle
    turtle.speed('fastest')
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()

    # Малювання дерева Піфагора
    draw_pythagoras_tree(branch_length, level)
    turtle.done()

if __name__ == "__main__":
    main()
