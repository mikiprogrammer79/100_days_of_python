print('''
                                          _.-.._         _._
                                     _,/^^,y./  ^^^^"""^^\= \
                                     \y###XX;/  /     \    ^\^\
                                       `\Y^   /   .-==||==-.)^^
                   ,.-=""""=-.__       /^ (  (   -/<0>++<0>(
                 .^      .: . . :^===(^ \ (  (  /```^^^^^^^)
                /      .: .,GGGGp,_ .(   \   /    /-(o'~'o))
              .^      : . gGG"""YGG}. \   )   / /  _/-====-\
             /       (. .gGP  __ ~~ . .\  \  (    (  _.---._)
            /        (. (GGb,,)GGp. . . \_-^-.__(_ /______./
           (          \ . `"!GGP^ . . . . ^=-._--_--^^^^^~)
           (        /^^^\_. . . . . . . . . . . . . . . . )
           )       /     /._. . . . . . . . . . . . . ._.=)
           \      /      |  ^"=.. . . . . . . ._++""\"^    \
            \    |       |       )^|^^~'---'~^^      \     )
            )   /        )      /   \                 \    \
            |`  |        \     /\    \                (    /
            |   |         (   (  \ . .\               |   (
            )   |         )   )   ^^^^^^              |   |
           /. . \         |  '|                       )   (
           ^^^^^^         )    \                      /. . \
                          / . . \                     ^^^^^^
                          ^^^^^^^

Allen Mullen
      ''')

# Greetings and instructions
print('''
      Welcome to Find The Bulldog!!
      Rex is a missing bulldog. Answer the questions right and bring Rex to its owners.
      You have been assigned to capture Rex alive. Be careful Rex is very aggressive.
      ''')

# Prompt user with questions and create conditional statements
answer1 = input("You are in front of Rex owner's house. Would you go to the \"park\" or to the \"city\"? ").lower()
if answer1 == "park":
    answer2 = input("You see a man walking a doberman. Would you ask him for help? \"Y\" or \"N\" ").lower()
    if answer2 == "y":
        print("Game over! The doberman dog has bitten your leg")
    elif answer2 == "n":
        answer3 = input("There's a man training a dog in the park. Would you go there? \"Y\" or \"N\": ").lower()
        if answer3 == "n":
            print("Game over!! The owner of Rex fired you")
        elif answer3 == "y":
            print("He said he saw a drug dealer walking a bulldog around the city.")
            answer4 = input("Type \"GO\" to have a word with the drug dealer or \"WAIT\" to find out more witnesses: ").lower()
            if answer4 == "go":
                print("Game over!! You have been attacked and seriously injured.")
            elif answer4 == "wait":
                print('''A woman told you there's a dog in a farm nearby. When you get there, you see Rex.
                      Rex is in a stable closed by an electric fence with three different cables:''')
                answer5 = input("What wire would you cut? \"GREEN\", \"RED\", \"BLUE\": ").lower()
                if answer5 == "green":
                    print("Congratulations!! You safe Rex. You win!")
                elif answer5 == "red" or answer5 == "blue":
                    print("Game over!! Short-circuit.")
                else:
                    print("Not the right answer. Game Over!!")
        else:
            print("Not the right answer. Game Over!!")
    else:
        print("Not the right answer. Game Over!!")
elif answer1 == "city":
    print("You see a drug dealer walking a bulldog around the city.")
    answer4 = input("Type \"GO\" to have a word with the drug dealer or \"WAIT\" to find out more: ").lower()
    if answer4 == "go":
        print("Game over!! You have been attacked and seriously injured.")
    elif answer4 == "wait":
        print('''A woman told you there's a dog in a farm nearby. When you get there, you see Rex.
Rex is in a stable closed by an electric fence with three different cables:''')
        answer5 = input("What wire would you cut? \"GREEN\", \"RED\", \"BLUE\": ").lower()
        if answer5 == "green":
            print("Congratulations!! You safe Rex. You win!")
        elif answer5 == "red" or answer5 == "blue":
            print("Game over!! Short-circuit.")
        else:
            print("Not the right answer. Game Over!!")

else:
    print("Not the right answer. Game Over!!")