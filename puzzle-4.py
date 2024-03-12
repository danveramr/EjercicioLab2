# Puzle Lineal con búsqueda en profundidad
from arbol import Nodo

def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    n_v = []
    n_f = []
    nodoInicial = Nodo(estado_inicial)
    n_f.append(nodoInicial)
    
    while (not solucionado) and len(n_f) != 0:        
        nodo = n_f.pop()        
        # extraer nodo y añadirlo a visitados
        n_v.append(nodo)

        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo
            d_n = nodo.get_datos()            
            # operador izquierdo
            hijo = [d_n[1], d_n[0], d_n[2], d_n[3]]
            h_i = Nodo(hijo)
            if not h_i.en_lista(n_v) \
                    and not h_i.en_lista(n_f):                
                n_f.append(h_i)
            # operador central
            hijo = [d_n[0], d_n[2], d_n[1], d_n[3]]
            h_c = Nodo(hijo)
            if not h_c.en_lista(n_v) \
                    and not h_c.en_lista(n_f):                
                n_f.append(h_c)
            # operador derecho
            hijo = [d_n[0], d_n[1], d_n[3], d_n[2]]
            h_d = Nodo(hijo)
            if not h_d.en_lista(n_v) \
                    and not h_d.en_lista(n_f):                
                n_f.append(h_d)

            
            nodo.set_hijos([h_i, h_c, h_d])           



if __name__ == "__main__":
    estado_inicial=[1,4,3,2]
    solucion=[1,2,3,4]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)