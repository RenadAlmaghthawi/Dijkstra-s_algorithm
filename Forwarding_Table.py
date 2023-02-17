import PySimpleGUI as sg

def forwarding_table_u():
    toprow = ['destination', 'outgoing link']
    rowOF = [['v', '(u,v)'],
                ['w', '(u,x)'],
                ['z', '(u,x)'],
                ['y', '(u,x)'],
                ['x', '(u,x)']
                ]
    tbl1 = sg.Table(values=rowOF, headings=toprow,
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)

    layout = [[tbl1]]
    window = sg.Window("Forwarding Table", layout, size=(400, 150), resizable=True)
    while True:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WIN_CLOSED:
            break
        if '+CLICKED+' in event:
            sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
        window.close() 

def forwarding_table_z():
    toprow = ['destination', 'outgoing link']
    rowOF = [['v', '(z,y)'],
            ['w', '(z,y)'],
            ['u', '(z,y)'],
            ['y', '(z,y)'],
            ['x', '(z,y)']
                    ]
    tbl1 = sg.Table(values=rowOF, headings=toprow,
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)

    layout = [[tbl1]]
    window = sg.Window("Forwarding Table", layout, size=(400, 150), resizable=True)
    while True:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WIN_CLOSED:
            break
        if '+CLICKED+' in event:
            sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
        window.close() 

def forwarding_table_v():
    toprow = ['destination', 'outgoing link']
    rowOF = [ ['z', '(v,x)'],
                ['w', '(v,w)'],
                ['u', '(v,u)'],
                ['y', '(v,x)'],
                ['x', '(v,x)']
                    ]
    tbl1 = sg.Table(values=rowOF, headings=toprow,
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)

    layout = [[tbl1]]
    window = sg.Window("Forwarding Table", layout, size=(400, 150), resizable=True)
    while True:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WIN_CLOSED:
            break
        if '+CLICKED+' in event:
            sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
        window.close()

def forwarding_table_w():
    toprow = ['destination', 'outgoing link']
    rowOF = [   ['z', '(w,y)'],
                ['v', '(w,v)'],
                ['u', '(w,y)'],
                ['y', '(w,y)'],
                ['x', '(w,y)']
                    ]
    tbl1 = sg.Table(values=rowOF, headings=toprow,
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)

    layout = [[tbl1]]
    window = sg.Window("Forwarding Table", layout, size=(400, 150), resizable=True)
    while True:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WIN_CLOSED:
            break
        if '+CLICKED+' in event:
            sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
        window.close()
        
def forwarding_table_y():
    toprow = ['destination', 'outgoing link']
    rowOF = [   ['z', '(y,z)'],
                ['v', '(y,x)'],
                ['u', '(y,x)'],
                ['w', '(y,w)'],
                ['x', '(y,x)']
                    ]
    tbl1 = sg.Table(values=rowOF, headings=toprow,
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)

    layout = [[tbl1]]
    window = sg.Window("Forwarding Table", layout, size=(400, 150), resizable=True)
    while True:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WIN_CLOSED:
            break
        if '+CLICKED+' in event:
            sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
        window.close()
def forwarding_table_x():
    toprow = ['destination', 'outgoing link']
    rowOF = [   ['z', '(x,y)'],
                ['v', '(x,v)'],
                ['u', '(x,u)'],
                ['w', '(x,y)'],
                ['y', '(x,y)']
                    ]
    tbl1 = sg.Table(values=rowOF, headings=toprow,
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)

    layout = [[tbl1]]
    window = sg.Window("Forwarding Table", layout, size=(400, 150), resizable=True)
    while True:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WIN_CLOSED:
            break
        if '+CLICKED+' in event:
            sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
        window.close()

##############################"uvwzyx"#######################################################
def  forwarding_table(source):
    if source == 'u' :
        forwarding_table_u()
    if source == "v":
        forwarding_table_v()
    if source == "w":
        forwarding_table_w()
    if source == "z":
        forwarding_table_z()
    if source == "y":
        forwarding_table_y()
    if source == "x":
        forwarding_table_x()
    
        