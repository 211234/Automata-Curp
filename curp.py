import tkinter as tk
import re
import matplotlib.pyplot as plt
import networkx as nx

def validar_curp(curp):
    if len(curp) == 1:
        return curp.upper() == 'M'
    elif len(curp) == 2:
        return curp.upper() == 'MA'
    elif len(curp) == 3:
        return curp.upper() == 'MAC'
    elif len(curp) == 4:
        return curp.upper() == 'MACC'
    else:
        return False

def validar_curp_exacta(curp):
    if re.match("^MACC$", curp, re.IGNORECASE):
        return True
    else:
        return False

def validar_curp_inicio_m(curp):
    if re.match("^[mM][^MACL]{3}$", curp):
        return True
    else:
        return False

def generar_automata(rfc):
    G = nx.DiGraph()

    estados = []
    transiciones = []

    for i in range(len(rfc) + 1):
        estado = "q" + str(i)
        estados.append(estado)
        if i < len(rfc):
            transiciones.append({
                'source': "q" + str(i),
                'target': "q" + str(i + 1),
                'label': rfc[i]
            })

    G.add_nodes_from(estados)


    for transicion in transiciones:
        G.add_edge(transicion['source'], transicion['target'], label=transicion['label'])

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def validar_y_mostrar_curp_exacta():
    curp = entry_curp_exacta.get()
    if validar_curp_exacta(curp):
        label_estado_exacta.config(text="Cadena Válida", fg="green")
        generar_automata("MACC")
    else:
        label_estado_exacta.config(text="Cadena no válida", fg="red")

def validar_y_mostrar_curp_inicio_m():
    curp = entry_curp_inicio_m.get()
    if validar_curp_inicio_m(curp):
        label_estado_inicio_m.config(text="Cadena Válida", fg="green")
        generar_automata(curp.upper())
    else:
        label_estado_inicio_m.config(text="Cadena no válida", fg="red")

def validar_y_mostrar_curp():
    curp = entry_curp.get()
    if validar_curp(curp):
        label_estado.config(text="Cadena Válida", fg="green")
        generar_automata(curp.upper())
    else:
        label_estado.config(text="Cadena no válida", fg="red")


ventana = tk.Tk()
ventana.title("Validador de CURP")

frame_primera_expresion = tk.Frame(ventana)
frame_primera_expresion.pack(pady=10)

label_curp = tk.Label(frame_primera_expresion, text="Ingrese su CURP (Exacta o que empiece con 'M' o 'm'):")
label_curp.pack(side="left")
entry_curp = tk.Entry(frame_primera_expresion)
entry_curp.pack(side="left", padx=10)
boton_validar = tk.Button(frame_primera_expresion, text="Validar CURP", command=validar_y_mostrar_curp)
boton_validar.pack(side="left", padx=10)
label_estado = tk.Label(frame_primera_expresion, text="", font=("Arial", 12))
label_estado.pack(side="left")

frame_segunda_expresion = tk.Frame(ventana)
frame_segunda_expresion.pack(pady=10)

label_curp_inicio_m = tk.Label(frame_segunda_expresion, text="Ingrese su CURP (Comienza con 'M' o 'm' y tiene 4 letras):")
label_curp_inicio_m.pack(side="left")
entry_curp_inicio_m = tk.Entry(frame_segunda_expresion)
entry_curp_inicio_m.pack(side="left", padx=10)
boton_validar_inicio_m = tk.Button(frame_segunda_expresion, text="Validar CURP", command=validar_y_mostrar_curp_inicio_m)
boton_validar_inicio_m.pack(side="left", padx=10)
label_estado_inicio_m = tk.Label(frame_segunda_expresion, text="", font=("Arial", 12))
label_estado_inicio_m.pack(side="left")


ventana.mainloop()
