capital = {'canada' : 'Ottawa', 
           'austria' : 'Vienna',
           'belguim'  : 'Brussels'}
question = input("What Captail to want to know: ").lower()
print(capital.get(question, "Not in Dictionary"))