
# O problema é que para a solucao eu só posso retornar uma unica lista e para resolver 
# recursivamente nessa unica funcao eu preciso trabalhar com 2 listas, a normal recebida
# e a lista com as inversoes que é a resposta. Solucao foi criar outra funcao que eu posso mexer hehehe
                            
                    
class Solution:
    
    def recursiveCount(self, nums: list[int], indices: list[int], invCount: list[int]):
        # Se a lista L tem 1 elemento retorna L e array dessa lista vai ser 0 (pq tem 0 inversoes)
        
        if len(nums) == 1:
            return nums, indices
        
        #Divide a lista em 2 A e B
        meio = len(nums) // 2
        listaA = nums[:meio]
        listaB = nums[meio:]
        indicesA = indices[:meio]
        indicesB = indices[meio:]
        
        #recursivo para A, pega o array com as inversoes e os indices originais
        #recursivo para B, pega o array com as inversoes e os indices originais
        sortedA, sortedIndicesA = self.recursiveCount(listaA, indicesA, invCount)
        sortedB, sortedIndicesB = self.recursiveCount(listaB, indicesB, invCount)
        #faz o merge
        mergedList, mergedIndices = self.mergeCount(sortedA, sortedB, sortedIndicesA, sortedIndicesB, invCount)
        
        return mergedList, mergedIndices
    
    def mergeCount(self, listaA: list[int], listaB: list[int], indicesA: list[int], indicesB: list[int], invCount: list[int]):
        mergedList = []
        mergedIndices = []
        i, j = 0, 0
        #teve inversao
        while i < len(listaA) and j < len(listaB):
            if listaA[i] <= listaB[j]:
                mergedList.append(listaA[i])
                mergedIndices.append(indicesA[i])
                invCount[indicesA[i]] += j
                i += 1
            else:
                mergedList.append(listaB[j])
                mergedIndices.append(indicesB[j])
                j += 1
        
        while i < len(listaA):
            mergedList.append(listaA[i])
            mergedIndices.append(indicesA[i])
            invCount[indicesA[i]] += j
            i += 1
        
        while j < len(listaB):
            mergedList.append(listaB[j])
            mergedIndices.append(indicesB[j])
            j += 1
        
        return mergedList, mergedIndices
    
    def countSmaller(self, nums: list[int]):
        indices = list(range(len(nums)))
        invCount = [0] * len(nums)  # Inicializa o array das inversoes com zeros
        _, _ = self.recursiveCount(nums, indices, invCount) #passa o proprio array de inversoes
        return invCount