from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0) #posición inicial de la comida
snake = [vector(10, 0)] #posición inicial de la serpiente
aim = vector(0, -10) #dirección inicial (va hacia abajo)
colors_list = ('black', 'green', 'darkorange', 'navy', 'blue') #lista de colores 
color_snake = None #color de la serpiente (posteriormente sera asignado un color de la lista)
color_food = None

def change(x, y): #funcion que cambia la direccion de la serpiente
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head): #revisa si se encuentra dentro de los limites
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food(): #función para mover la comida de forma aleatoria
    directions=[vector(10,0),vector(-10,0),vector(0,10),vector(0,-10)]
    move_direction=directions[randrange(len(directions))]
    new_food_pos=food + move_direction  #la nueva posición de la comida

    if inside(new_food_pos): #mueve la comida si esta dentro de los rangos
        food.move(move_direction)

    ontimer(move_food,1000)

def color(): #se le asigna un color a la serpiente y a la comida --> de la lista de colores
    global color_snake, color_food
    color_snake = choice(colors_list)  
    color_food = choice(colors_list)

    # Asegurar que la comida y la serpiente no tengan el mismo color
    while color_food == color_snake:
        color_food = choice(colors_list)


def move(): #mueve la serpiente
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake: #si la cabeza choca contra los limites o contra su mismo cuerpo
        square(head.x, head.y, 9, 'red') #pinta la cabeza en rojo
        update()
        return #finaliza el juego --> endgame

    snake.append(head) #se le agrega una unidad al cuerpo de la serpiente

    if head == food: #si la serpiente come la comida
        print('Snake:', len(snake)) # se imprime en consola el tamaño (similar a un puntaje)
        food.x = randrange(-15, 15) * 10 #la comida busca una pos aleatoria en el eje x
        food.y = randrange(-15, 15) * 10 #la comida busca una pos aleatoria en el eje y
    else:
        snake.pop(0)

    clear()
    

    for body in snake: #dibuja el cuerpo de la serpiente
        square(body.x, body.y, 9, color_snake)

    
    
    square(food.x, food.y, 9, color_food)
    update()
    ontimer(move, 100)



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
#teclas de movimiento de la serpiente (entrada del usuario)
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

color()
move()
move_food()
done()
 
