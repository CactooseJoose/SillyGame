name = input ('Please enter your name:')
print(f'Well, good morning{name},')
start = input('Would you like to get out of bed? Say play if so: ')
if start == 'play':
        print('Great, get on up then!')
        setting = input('Will you get some breakfast or go moderate?: ')
else:
        print('Womp womp, you stayed in bed until you died. Silly ending')
        quit()

if setting == 'breakfast':
        print("Sweet! You get out of bed and head to the kitchen.")
        response = input("You look in your pantry and see you have either oatmeal or cereal:")
        if response == 'oatmeal' :
            print("You grab yourself some oatmeal and preapare it using a: ")
            transport = input('mircrowave or stove":')
            if transport == 'microwave':
                  print("You fucking explode because you tried to use that handheld microwave you made based off of a youtube video 1/7")
                  quit()
            elif transport == 'stove':
                  print("You forgot you don't know how to cook and end up in the hospital with 3rd degree burns 2/7")
                  quit()
       
        elif response == 'cereal':
            print ("You grab the box of cereal along with a bowl and some milk. Which goes first?:")
            transport = input('bowl or milk?:')
            if transport == 'bowl':
                  print("You make a correct bowl of cereal and live out the rest of your days happy and not stupid. 3/7")
                  quit()
            elif transport == 'milk':
                  print("You proceed to poor milk on your counter and floor, slipping on it and killing yourself instantly 4/7")
                  quit()
        
        else: 
           print ("Being unable to decide you rot standing in place. L 5/7")
        quit()

elif setting == 'moderate':
    print("You get up and sit at your computer and stare at Discord")
    response = input("Do you message an egirl or punish a no-good gooner?:")
    if response == 'punish':
         print ("You ban the gooner with ferious clicking and tapping, but still die because you wasted your life because you're on discord you fucking loser.")
    elif response == 'egirl':
         print("You instantly gain 300 pounds and die with an ugly ass beard. 6/7")
    quit()

else:
        print("Womp womp, you didn't choose and the egirl is efucking the gooner 7/7")
        quit() 
