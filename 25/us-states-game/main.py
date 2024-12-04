import turtle 
import pandas
is_full = False

screen = turtle.Screen()
screen.title("U.S. States Game")

# fazendo upload de novo formato (imagem)
image = "blank_states_img.gif"
screen.addshape(image)
screen.shape(image)

# definindo os objetos
pen = turtle.Turtle()

data = pandas.read_csv("50_states.csv")
state = data.state.tolist()

# mostrando os nomes dos estados no mapa e pegando as coordenadas de cada estado
pen.color("black")
pen.hideturtle()
pen.penup()
x_coor = data.x.to_list()
y_coor = data.y.to_list()

# adicionando pop up como input
answer_state = screen.textinput(title="Guess the State", prompt="Guess a state name:").lower()

# alternativa ao exitonclick() - mantém a tela aberta mesmo com o clique
screen.mainloop()



# código para encontrar as coordenadas do mouse em uma tela:

# função que recebe dois parâmetros, que representam as coordenadas x e y do clique 
# imprime as coordenadas do clique
# def click_coor(x,y):
#    print(x,y)

# ouvirá quando o mouse clicar, chamando a função e passando as coordenadas, capturando a posição do clique
# ao clicar em qualquer lugar da tela, a função click_coor é chamada
# turtle.onscreenclick(click_coor)