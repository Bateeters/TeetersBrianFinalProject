import tkinter as tk
from PIL import Image

def getSelection(dropdown):
    selection = dropdown.get(dropdown.curselection())

    if selection == 'Aphrodite':
        aphrodite = tk.Toplevel(bg='lightpink')
        aphrodite.geometry("500x600")
        aphrodite.title("Aphrodite")

        aphroditephoto = tk.PhotoImage(file="GreekGodBanners/Aphrodite.png")
        aphroditelabel = tk.Label(aphrodite, image=aphroditephoto)
        aphroditelabel.place(relx=0.5, rely=0.05, relwidth=0.33, relheight=0.33, anchor='n')

        lower_frame = tk.Frame(aphrodite, bg='mistyrose', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame, text="Goddess of Love and Beauty\n\nCan change her appearance to become whatever "
                                            "is thought to be most beautiful\n\nSymbol: the dove\n\nRoman name: Venus",
                          bg='mistyrose')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        #previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        #previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: aphrodite.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        next = tk.Button(lower_frame, text=">", fg='black', font=40)
        next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    elif selection == 'Apollo':
        apollo = tk.Toplevel(bg='beige')
        apollo.geometry("500x600")
        apollo.title("Apollo")

        apolloframe = tk.Frame(apollo, bg='beige')
        apolloframe.place(x=0, y=0, relwidth=1, relheight=1)

        apollobanner = tk.PhotoImage(file="GreekGodBanners/Apollo.png")
        banner = tk.Label(apolloframe, image=apollobanner)
        banner.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(apollo, bg='white', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame, text="God of Poetry and Music\n\nOne of, if not the most, attractive male Olympians,"
                                            "loves to be the center of attention\n\nSymbol: the lyre\n\nRoman name: Apollo",
                          bg='white')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: apollo.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        next = tk.Button(lower_frame, text=">", fg='black', font=40)
        next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    elif selection == 'Ares':
        ares = tk.Toplevel(bg='darkred')
        ares.geometry("500x600")
        ares.title("Ares")

        aresframe = tk.Frame(ares, bg='darkred')
        aresframe.place(x=0, y=0, relwidth=1, relheight=1)

        aresbanner = tk.PhotoImage(file="GreekGodBanners/Ares.png")
        banner = tk.Label(aresframe, image=aresbanner)
        banner.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(ares, bg='grey', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame, text="God of War\n\nSon of Zeus and Hera, said to be involved in every argument"
                                            "from a small disagreement, to wars. Loves to fight.\n\nSymbols: A spear and "
                                            "the wild boar\n\nRoman name: Mars",
                          bg='grey')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: ares.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        next = tk.Button(lower_frame, text=">", fg='black', font=40)
        next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    elif selection == 'Artemis':
        artemis = tk.Toplevel(bg='gainsboro')
        artemis.geometry("500x600")
        artemis.title("Artemis")

        artemisframe = tk.Frame(artemis, bg='gainsboro')
        artemisframe.place(x=0, y=0, relwidth=1, relheight=1)

        artemisbanner = tk.PhotoImage(file="GreekGodBanners/Artemis.png")
        banner = tk.Label(artemisframe, image=artemisbanner)
        banner.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(artemis, bg='azure', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame, text="Goddess of the Moon, Hunt, and Young Maidens\n\nShe is deadly with her bow."
                                            "She does not entertain foolish individuals, especially males. She usually "
                                            "appears as a young girl and dresses all in white and silver to match her "
                                            "eyes and the moon.\n\nSymbols: the moon, the deer\n\nRoman name: Diana",
                          bg='azure')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: artemis.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        next = tk.Button(lower_frame, text=">", fg='black', font=40)
        next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    elif selection == 'Athena':
        athena = tk.Toplevel(bg='slategrey')
        athena.geometry("500x600")
        athena.title("Athena")

        athenaframe = tk.Frame(athena, bg='slategrey')
        athenaframe.place(x=0, y=0, relwidth=1, relheight=1)

        athenabanner = tk.PhotoImage(file="GreekGodBanners/Athena.png")
        banner = tk.Label(athenaframe, image=athenabanner, bg='slategrey')
        banner.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(athena, bg='lightsteelblue', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="Goddess of Wisdom\n\nDaughter of Zeus and Hera. She and Ares argue frequently and have "
                               "been known to start wars. She is the most active goddess in human affairs. She is very"
                               "prideful and has a temper to go with it.\n\nSymbols: the owl\n\nRoman name: Minerva",
                          bg='lightsteelblue')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: athena.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        next = tk.Button(lower_frame, text=">", fg='black', font=40)
        next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    elif selection == 'Demeter':
        demeter = tk.Toplevel(bg='darkkhaki')
        demeter.geometry("500x600")
        demeter.title("Demeter")

        demeterframe = tk.Frame(demeter, bg='darkkhaki')
        demeterframe.place(x=0, y=0, relwidth=1, relheight=1)

        demeterbanner = tk.PhotoImage(file="GreekGodBanners/Demeter.png")
        banner = tk.Label(demeterframe, image=demeterbanner, bg='darkkhaki')
        banner.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(demeter, bg='darkgreen', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="Goddess of Agriculture\n\nQuiet and simple goddess. If she was happy the crops would grow."
                               "Hades kidnapped her daughter, Persephone. Winter is said to be when she leaves to vist "
                               "her in the underworld.\n\nSymbols: Torch, Corn plant\n\nRoman name: Ceres",
                          bg='darkgreen', fg='white')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: demeter.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        next = tk.Button(lower_frame, text=">", fg='black', font=40)
        next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    elif selection == 'Dionysus':
        dionysus = tk.Toplevel(bg='maroon')
        dionysus.geometry("500x600")
        dionysus.title("Dionysus")

        dionysusframe = tk.Frame(dionysus, bg='darkmagenta')
        dionysusframe.place(x=0, y=0, relwidth=1, relheight=1)

        dionysusbanner = tk.PhotoImage(file="GreekGodBanners/Dionysus.png")
        banner = tk.Label(dionysusframe, image=dionysusbanner, bg='darkmagenta')
        banner.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(dionysus, bg='lemonchiffon', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="Goddess of Wine\n\nInvented wine which impressed Zeus, his father, and got him promoted "
                               "to a god. Loves to party and drink. Known to be both a fun and angry drunk.\n\n"
                               "Symbols: the leopard, the grape vine\n\nRoman name: Bacchus",
                          bg='lemonchiffon')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: dionysus.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        next = tk.Button(lower_frame, text=">", fg='black', font=40)
        next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    elif selection == 'Hades':
        hades = tk.Toplevel(bg='indigo')
        hades.geometry("500x600")
        hades.title("Hades")

        hadesframe = tk.Frame(hades, bg='indigo')
        hadesframe.place(x=0, y=0, relwidth=1, relheight=1)

    elif selection == 'Hephaestus':
        hephaestus = tk.Toplevel(bg='dimgray')
        hephaestus.geometry("500x600")
        hephaestus.title("Hephaestus")

        hephaestusframe = tk.Frame(hephaestus, bg='dimgray')
        hephaestusframe.place(x=0, y=0, relwidth=1, relheight=1)

    elif selection == 'Hera':
        hera = tk.Toplevel(bg='silver')
        hera.geometry("500x600")
        hera.title("Hera")

        heraframe = tk.Frame(hera, bg='silver')
        heraframe.place(x=0, y=0, relwidth=1, relheight=1)

    elif selection == 'Hermes':
        hermes = tk.Toplevel(bg='orange')
        hermes.geometry("500x600")
        hermes.title("Hermes")

        hermesframe = tk.Frame(hermes, bg='orange')
        hermesframe.place(x=0, y=0, relwidth=1, relheight=1)

    elif selection == 'Poseidon':
        poseidon = tk.Toplevel(bg='midnightblue')
        poseidon.geometry("500x600")
        poseidon.title("Poseidon")

        poseidonframe = tk.Frame(poseidon, bg='midnightblue')
        poseidonframe.place(x=0, y=0, relwidth=1, relheight=1)

    elif selection == 'Zeus':
        zeus = tk.Toplevel(bg='darkgoldenrod')
        zeus.geometry("500x600")
        zeus.title("Zeus")

        zeusframe = tk.Frame(zeus, bg='darkgoldenrod')
        zeusframe.place(x=0, y=0, relwidth=1, relheight=1)

    else:
        print("please select one")


root = tk.Tk()
root.title("Greek Knowledge Finder")

canvas = tk.Canvas(root, height=250, width=600)
canvas.pack()

large = tk.Frame(root, bg='gray')
large.place(relx=0, rely=0, relwidth=1, relheight=1)

photo = tk.PhotoImage(file="building1.png")
photolabel = tk.Label(large, image=photo)
photolabel.place(relwidth=1, relheight=1)

frame = tk.Frame(large, bg='black', bd=5)
frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.5, anchor='n')

label = tk.Label(frame, text="Learn About the Greek God or Goddess:", bg='black', fg='white', font=100)
label.place(relx=0, rely=0, relwidth=1, relheight=0.5)

gods = tk.StringVar()
gods.set(('Aphrodite', 'Apollo', 'Ares', 'Artemis', 'Athena', 'Demeter', 'Dionysus', 'Hades',
          'Hephaestus', 'Hera', 'Hermes', 'Poseidon', 'Zeus'))
dropdown = tk.Listbox(frame, listvariable=gods, bg='white', fg='black',
                      height=13, highlightcolor='gray', selectmode='single', font=40)
dropdown.place(relx=0, rely=0.5, relwidth=0.65, relheight=0.5)

search = tk.Button(frame, text="Search", fg='blue', font=40, command=lambda: [getSelection(dropdown)])
search.place(relx=0.7, rely=0.5, relwidth=0.3, relheight=0.5)

root.mainloop()
