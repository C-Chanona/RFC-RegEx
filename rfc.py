import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox
import re

#Solicitar RFC
modal = tk.Tk().withdraw()
not_break_loop = True

def case_1():
    while True:
        rfc = simpledialog.askstring("Input", 'Inserte su RFC')
        if(not len(rfc) > 4 ):
            isvalid = re.fullmatch(pattern="^[cC][aA][aA][cC]", string=rfc)
            if(isvalid):
                #Crear un grafo
                graph = nx.Graph()

                # Crear nodos
                nodos = [0, 1, 2, 3, 4]
                labels = {0: 'q0', 1: 'q1', 2: 'q2', 3: 'q3', 4: "q4"}
                symbols = {(0, 1): rfc[0], (1, 2): rfc[1], (2, 3): rfc[2], (3, 4): rfc[3]}

                # Definir el nodo inicial y el nodo final
                initial_state = 0
                final_state = 4

                # Añadir nodos y aristas al grafo
                graph.add_nodes_from(nodos)
                graph.add_edges_from(symbols.keys())

                # Asignar etiquetas y símbolos
                nx.set_node_attributes(graph, labels, 'label')
                nx.set_edge_attributes(graph, symbols, 'symbol')

                # Posiciones fijas para cada nodo, con un mayor margen izquierdo
                pos = {0: (1, 0), 1: (2, 0), 2: (3, 0), 3: (4, 0), 4: (5, 0)}

                # Personalizar las propiedas del grafo y sus nodos
                nx.draw(graph, pos, node_color='lightgreen', node_size=800)
                nx.draw_networkx_labels(graph, pos, labels=labels, font_color='blue')
                nx.draw_networkx_edge_labels(graph, pos, edge_labels=symbols, font_color='red')
                nx.draw_networkx_nodes(graph, pos, nodelist=[final_state], edgecolors='black', node_color='lightgreen')

                # Ajustar la flecha de inicio
                offset_x = 0.59  # Distancia en el eje X desde el nodo inicial
                offset_y = 0.1  # Altura de la flecha
                arrow_length = 0.3  # Longitud de la flecha

                plt.arrow(pos[initial_state][0] - offset_x, pos[initial_state][1], arrow_length, 0, head_width=offset_y, head_length=0.1, fc='k', ec='k')
                plt.axis('equal')  # Asegura que las proporciones sean iguales en ambos ejes
                plt.xlim(0, 6)  # Ajusta los límites del eje X para evitar que el gráfico esté demasiado pegado al borde
                plt.show()
                break
            else:
                messagebox.showerror("CADENA INVALIDA", "Los caracteres no son los esperados")
        else:
            messagebox.showerror("CADENA INVALIDA", "La cadena contiene demasiados caracteres")
    global not_break_loop
    not_break_loop = False

def case_2():
    while True:
        rfc = simpledialog.askstring("Input", 'Inserte su RFC')
        if(not len(rfc) > 4 ):
            isvalid = re.fullmatch(pattern="^[cC][aAcC][aAcC][cCaA]", string=rfc)
            if(isvalid):
                #Crear un grafo
                graph = nx.Graph()

                # Crear nodos
                nodos = [0, 1, 2, 3, 4]
                labels = {0: 'q0', 1: 'q1', 2: 'q2', 3: 'q3', 4: "q4"}
                symbols = {(0, 1): rfc[0], (1, 2): rfc[1], (2, 3): rfc[2], (3, 4): rfc[3]}

                # Definir el nodo inicial y el nodo final
                initial_state = 0
                final_state = 4

                # Añadir nodos y aristas al grafo
                graph.add_nodes_from(nodos)
                graph.add_edges_from(symbols.keys())

                # Asignar etiquetas y símbolos
                nx.set_node_attributes(graph, labels, 'label')
                nx.set_edge_attributes(graph, symbols, 'symbol')

                # Posiciones fijas para cada nodo, con un mayor margen izquierdo
                pos = {0: (1, 0), 1: (2, 0), 2: (3, 0), 3: (4, 0), 4: (5, 0)}

                # Personalizar las propiedas del grafo y sus nodos
                nx.draw(graph, pos, node_color='lightgreen', node_size=800)
                nx.draw_networkx_labels(graph, pos, labels=labels, font_color='blue')
                nx.draw_networkx_edge_labels(graph, pos, edge_labels=symbols, font_color='red')
                nx.draw_networkx_nodes(graph, pos, nodelist=[final_state], edgecolors='black', node_color='lightgreen')

                # Ajustar la flecha de inicio
                offset_x = 0.59  # Distancia en el eje X desde el nodo inicial
                offset_y = 0.1  # Altura de la flecha
                arrow_length = 0.3  # Longitud de la flecha

                plt.arrow(pos[initial_state][0] - offset_x, pos[initial_state][1], arrow_length, 0, head_width=offset_y, head_length=0.1, fc='k', ec='k')
                plt.axis('equal')  # Asegura que las proporciones sean iguales en ambos ejes
                plt.xlim(0, 6)  # Ajusta los límites del eje X para evitar que el gráfico esté demasiado pegado al borde
                plt.show()
                break
            else:
                messagebox.showerror("CADENA INVALIDA", "Los caracteres no son los esperados")
        else:
            messagebox.showerror("CADENA INVALIDA", "La cadena contiene demasiados caracteres")
    
    global not_break_loop
    not_break_loop = False
    
def default_case():
    messagebox.showwarning('OPCION INVALIDA', 'Ingrese una opcion correcta')

switch_dict = {
    '1': case_1,
    '2': case_2
}

while not_break_loop:
    option = simpledialog.askstring("Input", 'Elija una opcion \n1) RFC en orden\n2) RFC sin orden')
    if option is None:  # El usuario cerró el diálogo
        break
    else:
        # Obtener la función a ejecutar del diccionario y llamarla
        switch_dict.get(option, default_case)()