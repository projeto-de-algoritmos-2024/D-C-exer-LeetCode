class Solution:
    def oraculo(self, lista: list[int]):
        #agrupa em 5
        #acha a mediana de cada grupo
        #acha a mediana das medianas
        
        if len(lista) <= 5:
            lista.sort()
            return lista[len(lista) // 2]
        
        listinha = []
        listaMediana = []
        
        for i in range(0,len(lista),5):
            listinha = lista[i:i + 5] 
            listinha.sort()
            listaMediana.append(listinha[2])

        return self.oraculo(listaMediana)
    
    def quickSelect(self, lista, left, right, k):
        if left == right:
            return lista[left]
        
        pivo = self.oraculo(lista)
        pivoIndice = self.partir(lista, left, right, pivo)
        
        if k == pivoIndice:
            return lista[k]
        elif k < pivoIndice:
            return self.quickSelect(lista, left, pivoIndice-1 , k)
        else:
            return self.quickSelect(lista, pivoIndice+1, right, k)
    
    def partir(self, lista, left, right, pivo):
        indicePivo = lista.index(pivo)
        lista[indicePivo], lista[right] = lista[right], lista[indicePivo]
        indice = left
        
        for i in range(left, right):
            if lista[i] < pivo:
                lista[i], lista[indice] = lista[indice], lista[i]
                indice += 1
        
        lista[indice], lista[right] = lista[right], lista[indice]
        
        return indice
           
                
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        int_list = [int(i) for i in nums]
        
        return str(self.quickSelect(int_list, 0, (len(int_list) - 1), (len(int_list) - k)))