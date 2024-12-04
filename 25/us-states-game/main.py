import turtle 
import pandas
guessed_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")

# fazendo upload de novo formato (imagem)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# definindo os objetos
pen = turtle.Turtle()

# mostrando os nomes dos estados no mapa
pen.color("black")
pen.hideturtle()
pen.penup()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

while len(guessed_states) < 50:
    # adicionando pop up como input
    answer_state = screen.textinput(f"{len(guessed_states)}/50 states correct", prompt="Guess a state name:").title() # title Case
    if answer_state == "Exit":
        not_guessed_states = []
        # criando novo dataframe contendo apenas os estados que não foram adivinhados
        for state in states:
            if state not in guessed_states:
                not_guessed_states.append(state)
        df = pandas.DataFrame(not_guessed_states)
        df.to_csv("missing_states.csv")
        break
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state] 
        pen.goto(state_data.x.item(), state_data.y.item()) # acessando os atributos das colunas x e y dos respectivos estados e usando item para extrair um único item na series
        # item pega o primeiro elemento
        pen.write(answer_state)

    

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