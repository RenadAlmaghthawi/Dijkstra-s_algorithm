import networkx as nx
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import Forwarding_Table

#create graph
G = nx.Graph()

G.add_nodes_from("uvwzyx")
G.add_edges_from([
    ("u", "v", {"weight": 2}),
    ("u", "w", {"weight": 5}),
    ("v", "w", {"weight": 3}),
    ("z", "w", {"weight": 5}),
    ("z", "y", {"weight": 2}),
    ("y", "w", {"weight": 1}),
    ("x", "w", {"weight": 3}),
    ("v", "x", {"weight": 2}),
    ("x", "u", {"weight": 1}),
    ("y", "x", {"weight": 1})
])
#position of nodes (x,y)
pos = {
    "u": (1, 5),
    "v": (3.5, 6.6),
    "x": (3.6, 3),
    "z": (10.3, 5),
    "y": (8, 3),
    "w": (8, 6.6), }
edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
# Draw the Graph
nx.draw(G, pos=pos, with_labels=True,
        node_color="blue", node_size=3000,
        font_color="white", font_size=20, font_family="Times New Roman", font_weight="bold",
        edge_color="lightgray",
        width=5)
#---------------------------------------------------------------------------------
def to_dstination():
   layout = [[sg.Text("Enter the first and last node to can you\nfind the shortest path between them:",
                   font='Any 15', background_color="#7aa4cc")],
          [sg.Image('Dijkstra_algorithm_app/gg.png')],
          [sg.Text('Enter the source node :', font='Any 15',
                   background_color="#7aa4cc"), sg.InputText()],
          [sg.Text('Enter the destination node :', font='Any 15',
                   background_color="#7aa4cc"), sg.InputText()],
          [sg.Button("  FIND  ",key='-find-', pad=((180, 170), 4), font='Any 15', button_color="#014e9a")],
          [sg.Text('Total Delay of path = ', font='Any 15', background_color="#7aa4cc"),sg.Text(key='-OUT-',font='Any 15', background_color="#7aa4cc") ]
          
          ]

   window = sg.Window("Dijkstra's algorithm", layout, size=(
    500, 450), background_color="#7aa4cc")

   while True:
    event, values = window.read()

    path = nx.dijkstra_path(G, source=values[1], target=values[2])
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                           edge_color='r', width=10)

    nx.draw_networkx_edge_labels(
        G, pos=pos, edge_labels=edge_labels, label_pos=0.5)
    plt.margins(0.2)
    plt.axis('equal')

    result = nx.dijkstra_path_length(G,source=values[1], target=values[2])
    window['-OUT-'].update(result)
    if event == '-find-':
        plt.show()
    if event == sg.WIN_CLOSED:
        break
    window.close()
#-------------------------------------------------------------------------------- 
def to_allNode():
    layout = [[sg.Text("Enter the source node to can you\nfind the shortest path of all nodes:",
                    font='Any 15', background_color="#7aa4cc")],
            [sg.Image('Dijkstra_algorithm_app/gg.png')],
            [sg.Text('Enter the source node :', font='Any 15',
                    background_color="#7aa4cc"), sg.InputText()],
            [sg.Button("  FIND  ",expand_x=10 ,font='Any 15', button_color="#014e9a"),
            sg.Button("forwarding table",expand_x=50, font='Any 15', button_color="#014e9a")]]

    window = sg.Window("Dijkstra's algorithm", layout, size=(
        500, 450), background_color="#7aa4cc")

    while True:
        event, values = window.read()
        for n in G.nodes:
            path = nx.dijkstra_path(G, source= values[1] , target=n)
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='r')
            nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                                edge_color='r', width=10)

            nx.draw_networkx_edge_labels(
                G, pos=pos, edge_labels=edge_labels, label_pos=0.5)
            plt.margins(0.2)
            plt.axis('equal') 
        for n in G.nodes:
            path = nx.dijkstra_path(G, source= values[1] , target=n)
            path = dict(nx.all_pairs_dijkstra_path(G))
            if (n != values[1]):
             print("from "+values[1]+" to " + n +" :" , path[values[1]][n] ) 

        if event in (None, 'Exit'):
            break
        if event == "  FIND  ":
            plt.show()   
        if event == "forwarding table":
           Forwarding_Table.forwarding_table(values[1])     
    window.close()
#---------------------------------------------------------------------------------
# Create the UI for (to chosse to dstination or all node)
layout = [[sg.Text("Choose what you want? ",font='Any 15', background_color="#7aa4cc")],
          [sg.Image('Dijkstra_algorithm_app/gg.png')],
          [sg.Text("find the shortest path from source to ",font='Any 15', background_color="#7aa4cc")],
          [sg.Button("  all nodes  ", expand_x=50, font='Any 15', button_color="#014e9a")
          ,sg.Button(" destination node ", expand_x=50, font='Any 15', button_color="#014e9a")
          ]]
          

window = sg.Window("Dijkstra's algorithm", layout, size=(500, 450), background_color="#7aa4cc")

while True:
    event, values = window.read()
 
    if event == sg.WIN_CLOSED:
        break
#to all node
    if event == "  all nodes  ":
       to_allNode()
#to destination node
    if event == " destination node ":
      to_dstination()
      
window.close()
#--------------------------------------------------------------------------------

