class Solution:
    def oraculo(self, lista: list[int]):
        #agrupa em 5
        #acha a mediana de cada grupo
        #acha a mediana das medianas
        
        listinha = []
        listaMediana = []
        
        for i in range(0,len(lista),5):
            for j in range(0,5):
                listinha.append(j)
                
            listinha.sort()
            listaMediana.append(listinha[2])

        if len(listaMediana) > 5:
            self.oraculo(listaMediana)
        else:
            listaMediana.sort()
            meio = int(len(listaMediana)/2)
            return listaMediana[meio]
            
        
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        int_list = [int(i) for i in nums]
        knum = self.oraculo(int_list)
        listaL = []
        listaR = []
        
        #Arrumar os nums ao redor do pivo
        for i in int_list:
            if i < knum:
                listaL.append(i)
            else:
                listaR.append(i)
        
        #Compara
        if len(listaL) == k - 1:
            return str(knum)
        if len(listaL) > k - 1:
            self.oraculo(listaL)
        else:
            self.oraculo(listaR)