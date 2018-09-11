
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from character import Character
from enemy import Enemy
import random

# Create root frame and initialize saving ability, setup blank character
root = tk.Tk()
can_save = False
your_player = Character("")
main_frame = tk.Frame(master=root, bg='black')
main_frame.pack_propagate(0)
main_frame.pack(fill=tk.BOTH, expand=1)

# Grab from players.txt initial data about all players
f = open("players.txt", "r")
players_info = f.readlines()
f.close()

# Create arrays of all enemies
enemy_messages = ["You leave your house to begin your" + "\n" + "quest and a bear jumps out to fight you!", "As you enter the dark woods \n" + "A tiger leaps at you!", "You sit in the middle of the woods \n" + "then, you hear an odd sound \n" + "a beaver attacks!", "After the beaver's defeat, a brunette river becomes open \n" + "As you ride down it, a serpent attacks!", "You conquered the river, and arrive at a fortress \n" + "A guard approaches you with his sword out!", "You see your father atop the tower, yelling for you\n" + "You race up the tower, but a royal guard blocks the main hall!", "You finally can see you father in front of you, \n" + "but the Emperor is your final enemy!"]
enemy_names = ["Bear", "Tiger", "Beaver", "Serpent", "Guard", "Royal Guard", "Emperor"]
enemy_healths = [10, 13, 15, 18, 21, 27, 38]
enemy_damages = [1, 2, 4, 5, 7, 8, 11]


# Create initial frame
def clear_frame(main_frame1):
    for a in main_frame1.winfo_children():
        a.destroy()


# Saving options
def save_options(progress):
    answer1 = 5
    while answer1 is None or answer1 > 3 or answer1 < 1:
        answer1 = tk.simpledialog.askinteger("Choose a save (1-3)", "Which save to overwrite?" + "\n\nSave 1: " + players_info[0].rstrip() + "\n\nSave 2: " + players_info[1].rstrip() + "\n\nSave 3: " + players_info[2].rstrip() + "\n")
    save_option_choice(answer1, progress)


def save_option_choice(choice, num):
    if choice == 1:
        players_info[0] = your_player.get_name().rstrip()
        players_info[3] = str(num).rstrip()
        players_info[6] = str(your_player.get_health()).rstrip()
        players_info[7] = str(your_player.get_stamina()).rstrip()
        players_info[8] = str(your_player.get_max_health()).rstrip()
        players_info[9] = str(your_player.get_max_stamina()).rstrip()
        players_info[10] = str(your_player.get_rest_up()).rstrip()
    elif choice == 2:
        players_info[1] = your_player.get_name().rstrip()
        players_info[4] = str(num).rstrip()
        players_info[11] = str(your_player.get_health()).rstrip()
        players_info[12] = str(your_player.get_stamina()).rstrip()
        players_info[13] = str(your_player.get_max_health()).rstrip()
        players_info[14] = str(your_player.get_max_stamina()).rstrip()
        players_info[15] = str(your_player.get_rest_up()).rstrip()
    elif choice == 3:
        players_info[2] = your_player.get_name().rstrip()
        players_info[5] = str(num).rstrip()
        players_info[16] = str(your_player.get_health()).rstrip()
        players_info[17] = str(your_player.get_stamina()).rstrip()
        players_info[18] = str(your_player.get_max_health()).rstrip()
        players_info[19] = str(your_player.get_max_stamina()).rstrip()
        players_info[20] = str(your_player.get_rest_up()).rstrip()
    with open("players.txt", "w") as b:
        for item in players_info:
            b.write("%s\n" % item.rstrip())


# Save button
def ask_save():
    if can_save:
        if tk.messagebox.askyesno('Save', 'Do you want to save?'):
            save_options(your_player.get_progress())
            root.destroy()
        else:
            root.destroy()
    else:
        root.destroy()


# Add label to main_frame
def add_label(text2):
    return tk.Label(main_frame, bg="black", text=text2, fg="blue", font=("System", 35))


# Add smaller label to main_frame
def add_small_label(text2):
    return tk.Label(main_frame, bg="black", text=text2, fg="blue", font=("System", 20))


# Add smaller label to main_frame
def add_big_label(text2):
    return tk.Label(main_frame, bg="black", text=text2, fg="blue", font=("System", 55))


# Add button to main_frame
def add_button(text2, command2):
    return tk.Button(master=main_frame, bg="black", text=text2, fg="blue", font=("System", 35), width=25,
                     command=command2)


def add_button_two_param(text2, command2, enemy, num):
    return tk.Button(master=main_frame, bg="black", text=text2, fg="blue", font=("System", 35), width=25,
                     command=lambda: command2(enemy, num))


def add_button_four_param(text2, command2, label_text, enemy_name, enemy_health, enemy_damage):
    return tk.Button(master=main_frame, bg="black", text=text2, fg="blue", font=("System", 35), width=25,
                     command=lambda: command2(label_text, enemy_name, enemy_health, enemy_damage))


# New game ask for player's name
def ask_name():
    answer0 = None
    while answer0 is None:
        answer0 = tk.simpledialog.askstring("Name Your Character", "What is your name?")
    global your_player
    your_player = Character(answer0)


def attack(enemy, num):
    clear_frame(main_frame)
    damage = random.randint(0, your_player.get_stamina())
    to_you = random.randint(0, enemy.get_damage())
    enemy.minus_health(damage)
    your_player.minus_health(to_you)
    your_player.minus_stamina(damage)
    attack1 = add_big_label("You did " + str(damage) + " damage to the" + "\n" + enemy.get_name() + "!")
    attack1.pack(pady=30)
    attack4 = add_big_label("The " + enemy.get_name() + " did " + str(to_you) + " to you!")
    attack4.pack(pady=10)
    if your_player.get_health() <= 0:
        tk.messagebox.showinfo("You died!", "The " + enemy.get_name() + " has killed you!")
        your_player.minus_health(-to_you)
        your_player.minus_stamina(-damage)
        save_options(your_player.get_progress())
        global can_save
        can_save = False
        start()
        return None
    if enemy.get_health() <= 0:
        attack3 = add_big_label("The " + enemy.get_name() + " is defeated!" + "\n\nsaving...")
        attack3.pack(pady=10)
        save_options(num)
    attack2 = add_button_two_param("Continue", fight, enemy, num)
    attack2.pack(pady=10)


def rest(enemy, num):
    clear_frame(main_frame)
    to_you = random.randint(0, enemy.get_damage())
    gained = random.randint(0, your_player.get_rest_up())
    your_player.minus_stamina(-gained)
    your_player.minus_health(to_you)
    rest1 = add_big_label("You gained " + str(gained) + "\nStamina!")
    rest1.pack(pady=50)
    attack4 = add_big_label("The " + enemy.get_name() + " did " + str(to_you) + " to you!")
    attack4.pack(pady=10)
    if your_player.get_health() <= 0:
        tk.messagebox.showinfo("You died!", "The " + enemy.get_name() + " has killed you!")
        your_player.minus_stamina(gained)
        your_player.minus_health(-to_you)
        save_options(your_player.get_progress())
        global can_save
        can_save = False
        start()
        return None
    rest2 = add_button_two_param("Continue", fight, enemy, num)
    rest2.pack(pady=50)


def fight(enemy, num):
    if enemy.get_health() > 0:
        clear_frame(main_frame)
        fight1 = add_label("The " + enemy.get_name() + " faces you!")
        fight1.pack(pady=50)
        fight2 = add_small_label("Your health: " + str(your_player.get_health()))
        fight2.pack(pady=10)
        fight3 = add_small_label("Your stamina: " + str(your_player.get_stamina()))
        fight3.pack(pady=10)
        fight4 = add_small_label("Enemy health: " + str(enemy.get_health()))
        fight4.pack(pady=10)
        fightop1 = add_button_two_param("Attack!", attack, enemy, num)
        fightop1.pack(pady=60)
        fightop2 = add_button_two_param("Rest!", rest, enemy, num)
        fightop2.pack(pady=60)
    else:
        clear_frame(main_frame)
        if your_player.get_progress() == 6:
            tk.messagebox.showinfo("WINNER", "You have won! Your father is saved!")
            root.destroy()
            return None
        your_player.minus_stamina(-random.randint(0, your_player.get_rest_up()))
        play_vend()


# Upgrade your health
def up_health():
    clear_frame(main_frame)
    your_player.plus_max_health(15)
    your_player.set_health(your_player.get_max_health())
    up1 = add_label("Your new max health is " + str(your_player.get_max_health()))
    up1.pack(pady=70)
    up2 = add_label("Health was restored!")
    up2.pack(pady=70)
    your_player.plus_progress()
    upb = add_button_four_param("Continue", play_fight, enemy_messages[your_player.get_progress()], enemy_names[your_player.get_progress()], enemy_healths[your_player.get_progress()], enemy_damages[your_player.get_progress()])
    upb.pack(pady=70)


# Upgrade your stamina
def up_stamina():
    clear_frame(main_frame)
    your_player.plus_max_stamina(15)
    your_player.set_stamina(your_player.get_max_stamina())
    up1 = add_label("Your new max stamina is " + str(your_player.get_max_stamina()))
    up1.pack(pady=70)
    up2 = add_label("Stamina was restored!")
    up2.pack(pady=70)
    your_player.plus_progress()
    upb = add_button_four_param("Continue", play_fight, enemy_messages[your_player.get_progress()], enemy_names[your_player.get_progress()], enemy_healths[your_player.get_progress()], enemy_damages[your_player.get_progress()])
    upb.pack(pady=70)


# Upgrade your resting
def up_rest():
    clear_frame(main_frame)
    your_player.plus_rest_up(8)
    up1 = add_label("Your new max resting is " + str(your_player.get_rest_up()))
    up1.pack(pady=70)
    your_player.plus_progress()
    upb = add_button_four_param("Continue", play_fight, enemy_messages[your_player.get_progress()], enemy_names[your_player.get_progress()], enemy_healths[your_player.get_progress()], enemy_damages[your_player.get_progress()])
    upb.pack(pady=100)


# Vendor choice
def vendor():
    clear_frame(main_frame)
    ven1 = add_label("Choose what to upgrade!")
    ven1.pack(pady=50)
    ven2 = add_button("Health", up_health)
    ven2.pack(padx=20, pady=20)
    ven3 = add_button("Stamina", up_stamina)
    ven3.pack(padx=20, pady=20)
    ven4 = add_button("Resting", up_rest)
    ven4.pack(padx=20, pady=20)


# After naming continue
def play_fight(label_text, enemy_name, enemy_health, enemy_damage):
    clear_frame(main_frame)
    one = add_label(label_text)
    one.pack(pady=200)
    bear = Enemy(enemy_name, enemy_health, enemy_damage)
    one_b = add_button_two_param("Continue", fight, bear, your_player.get_progress())
    one_b.pack(pady=70)


def play_vend():
    clear_frame(main_frame)
    one = add_label("After the fight, you sit down" + "\n" + "a mysterious man appears out of smoke.")
    one.pack(pady=200)
    one_b = add_button("Continue", vendor)
    one_b.pack(pady=70)


# Play button
def play_button():
    ask_name()
    clear_frame(main_frame)
    global can_save
    can_save = True
    intro = add_label("Welcome to the world of Tackzula, " + your_player.get_name() + "!" + "\n" + "You will now begin your quest to find your lost father!")
    intro.pack(pady=200)
    intro_b = add_button_four_param("Continue", play_fight, enemy_messages[your_player.get_progress()], enemy_names[your_player.get_progress()], enemy_healths[your_player.get_progress()], enemy_damages[your_player.get_progress()])
    intro_b.pack(pady=50)


# Load button
def load_button():
    answer1 = 5
    while answer1 is None or answer1 > 3 or answer1 < 1:
        answer1 = tk.simpledialog.askinteger("Choose a save (1-3)",
                                             "Which save to load?\n\n" + "Save 1: " + players_info[
                                                 0].rstrip() + "\n\nSave 2: " + players_info[1].rstrip() + "\n\nSave 3: " + players_info[2].rstrip() + "\n")
    if int(players_info[answer1+2]) == 0:
        tk.messagebox.showinfo("New Game", "No save found, starting a new game")
        your_player.set_health(10)
        your_player.set_stamina(10)
        play_button()
        return None
    global can_save
    can_save = True
    if answer1 == 1:
        your_player.set_name(players_info[0].rstrip())
        your_player.set_progress(int(players_info[3]))
        your_player.set_health(int(players_info[6]))
        your_player.set_stamina(int(players_info[7]))
        your_player.set_max_health(int(players_info[8]))
        your_player.set_max_stamina(int(players_info[9]))
        your_player.set_rest_up(int(players_info[10]))
    elif answer1 == 2:
        your_player.set_name(players_info[1].rstrip())
        your_player.set_progress(int(players_info[4]))
        your_player.set_health(int(players_info[11]))
        your_player.set_stamina(int(players_info[12]))
        your_player.set_max_health(int(players_info[13]))
        your_player.set_max_stamina(int(players_info[14]))
        your_player.set_rest_up(int(players_info[15]))
    elif answer1 == 3:
        your_player.set_name(players_info[2].rstrip())
        your_player.set_progress(int(players_info[5]))
        your_player.set_health(int(players_info[16]))
        your_player.set_stamina(int(players_info[17]))
        your_player.set_max_health(int(players_info[18]))
        your_player.set_max_stamina(int(players_info[19]))
        your_player.set_rest_up(int(players_info[20]))
    play_fight(enemy_messages[int(players_info[answer1+2])], enemy_names[int(players_info[answer1+2])], enemy_healths[int(players_info[answer1+2])], enemy_damages[int(players_info[answer1+2])])


# Start of game

# Create main screen
root.title("Tackzula")
root.geometry("1280x800")
root.resizable(0, 0)
root.iconbitmap("sword.ico")


# Create Initial Screen
def start():
    clear_frame(main_frame)
    main_title = tk.Label(main_frame, bg="black", text="Tackzula", fg="yellow", font=("System", 65))
    main_title.pack(pady=50)

    play = tk.Button(master=main_frame, bg="black", text='Play', fg="blue", font=("System", 65), width=25,
                     command=play_button)
    play.pack(pady=50)

    load = tk.Button(master=main_frame, bg="black", text='Load Game', fg="blue", font=("System", 65), width=25,
                     command=load_button)
    load.pack(pady=50)


start()
# End Initial Screen

# Main loop runner
root.protocol("WM_DELETE_WINDOW", ask_save)
root.mainloop()
