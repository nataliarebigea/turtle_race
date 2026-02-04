import turtle

 WIDTH,HEIGHT=500,500
 
def get_number_of_races():
races=0
while True:
    racers=imput('Enter numarul de races (2-10): ')
    if racers.isdigit():
        racers=int(racers)
    else:
        print ('Inputul nu e numeric...mai incerca!')
        continue

    if 2<=racers<=10:
        return racers
    else:
        print ('Numarul nu este intre 2 si 10 , incearca altceva!')

 def init_turtle();
        screen=turtle.Screen()
         screen.setup(WIDTH,HEIGHT)
        screen.title('Turtle Racing')
racers=get_number_of_races()
init_turtle()