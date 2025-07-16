# list_structure
# Use MergeSort, para la organizacion de elementos descendente 
# Ojo (ID ,Nombre, Experticia, Opinion)

class ListStructure:
    def __init__(self, list_data=None):
        self.list = list_data if list_data else []

    def mergeSort(self, lista, compare=None):
        # Caso base
        if len(lista) == 1:
            return lista
        
        # Dividir la lista en dos partes
        middle = len(lista)//2
        left_array = lista[:middle]
        right_array = lista[middle:]
        
        #Llamadas recursivas
        order_left_array = self.mergeSort(left_array, compare)
        order_right_array = self.mergeSort(right_array, compare)
        
        # Combinar las listas ordenadas
        return self.Merge(order_left_array,order_right_array, compare)
                 
   # No crear nuevos arreglos, trabajar sobre el mismo arreglo
   # utilizando indices para definir en cual subarreglo se esta trabajando 
   
    def Merge(self, left_array, right_array, compare=None):
        list_resultado = []
        i=j = 0
            
        while i < len(left_array) and j < len(right_array):
            
            if compare: 
                if compare(left_array[i], right_array[j]): 
                    list_resultado.append(left_array[i])
                    i += 1
                else: 
                    list_resultado.append(right_array[j])
                    j += 1
            
            else:
                if left_array[i] > right_array[j]:
                    list_resultado.append(left_array[i])
                    i += 1
                else:
                    list_resultado.append(right_array[j])
                    j += 1
                        
        while i < len(left_array):
            list_resultado.append(left_array[i])
            i += 1
                
        while j < len(right_array):
            list_resultado.append(right_array[j])
            j += 1
                
        return list_resultado
                    
    # Devuelve la lista                
    def get(self):
        return self.list