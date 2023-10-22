import ttkbootstrap as bs

def apply_styles():
    style = bs.Style()
    # style = bs.Style("darkly")
    style.configure('Custom1.TFrame',
                    background='blue',
                    borderwidth=4,
                    relief='groove')

    style.configure('Custom2.TFrame',
                    background='green',
                    borderwidth=5,
                    relief='groove')

    style.configure('Custom1.TButton',
                    foreground='blue',
                    background='white',
                    font=('Arial', 12, 'bold'),
                    padding=10)

    style.map('Custom1.TButton',
              background=[('pressed', 'green'),
                          ('active', 'yellow')],
              foreground=[('pressed', 'white'),
                          ('active', 'red')])

    # success_style = style.lookup("TLabel", "SUCCESS")
    # style.configure("Custom1.TLabel",
    #                 **success_style,
    #                 font=("Arial", 20))



