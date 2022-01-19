ans_a = "-Rearrange your priorities or change your goal"
ans_b = "-Divide your goal into smaller ones and start right away"
ans_c = "-Make a list of various benefits that you will gain when you achieve your goal"
ans_d = "-Make a plan and lay goals out sensibly in time"
ans_e = "Your motivation is in place, stop procrastinating"

while True:
    print("This is very simple motivation tool. Think of a goal you want to achieve.")
    goal = input("What is your goal?")
    game = input("Are you lack of motivation?[y/n]")
    if game == "n":
        print(ans_e)
    elif game == "y":
        answer_a = input("Is this goal important for you to achieve?[y/n]").lower()
        answer_b = input("Do you think it is possible for you to achieve the goal?[y/n]").lower()
        answer_c = input("Do you easily change your plans?[y/n]").lower()
        answer_d = input("Does your goal require much time of work?[y/n]").lower()
        print("Your goal: ", goal, "In order to achieve it you need to: ")
        if answer_a == "n":
            print(ans_a)
        if answer_b == "n":
            print(ans_b)
        if answer_c == "y":
            print(ans_c)
        if answer_d == "y":
            print(ans_d)
        if answer_a != "n" and answer_b != "n" and answer_c != "y" and answer_d != "y":
            print(ans_e)
