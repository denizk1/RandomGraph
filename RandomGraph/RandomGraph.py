import numpy as np
import random

class Graph(object):

    def __init__(self, size=13, edge=[0, 1]):

        self.graph_size = size  # grafın dugum sayisi
        self.edge = edge  # iki dugum arasindaki kenar . Eger dugum varsa 1, degilse 0 olacak.
        self.matrix_of_graph = np.zeros(size)  # komsuluk matrisi ilk degerleri 0.
        self.graph_to_dict = {}  # dugum ve bagli oldukleri dugumleri tutan sozluk. komsuluk listesi.

    # ilk olarak ust ucgen olusturur.
    # eger size n ise n-1,n-2,n-3...1 seklinde ust ucgenin kosegenleri 0 olacak seklinde tüm alt listeleri bulunur ve alt liste hep -1 seklinde azalacagi icin her listede sol tarafa eksildigi kazar 0 ekler.
    # orn: n=4  eger tam graph ise [1,1,1],[1,1],[1]= listeler. matris=[0,1,1,1],[0,0,1,1],[0,0,0,1].
    # simetrik oldugu icin transpoze alır ve toplar.
    # graph_matris:[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0].

    def Matrix_Of_Graph(self):

        upper_triangle = []  # oncelikle ust ucgeni belirleyecegiz
        lower_triangle = []
        zero_amount = 1  # ilk listede sol tarafa kendisine bag olmadigi icin ve 1 sıfır eklendigi icin ilk deger 1 dir.
        size = self.graph_size  # size ı sürekli azaltacagimiz icin bir degiskende sezı saklayıp tekrar guncelleyecegiz.

        while self.graph_size != 0:
            RandomUpperList = [0] * zero_amount + [random.randrange(0, 2, 1) for i in range(
                self.graph_size - 1)]  # her alt listeyi rastgele 0 veya 1 secip sol tarafına matrisi olusturacak kadar sifir ekliyoruz.
            upper_triangle.append(RandomUpperList)

            self.graph_size -= 1  # her alt liste bulunacagi icin size ı 1 azaltiyoruz.
            zero_amount += 1  # alt listeye gecerken matris tamamlanacagi icin konulan sifir sayisini arttiriyoruz.

        upper_triangle = np.array(upper_triangle)
        lower_triangle = upper_triangle.T  # simetrik olacagi icin alt ucgen ust ucgenin transpozudur.

        self.graph_size = size
        self.matrix_of_graph = lower_triangle + upper_triangle

        return self.matrix_of_graph

    # matristen gelen dugumleri bir graph komsuluk sozlugunde saklıyor.

    def Graph_To_List(self):

        graph = self.matrix_of_graph
        for i in range(graph.shape[0]):
            nodes = []
            for j in range(graph.shape[1]):  # eger dugum varsa node listesine ekle
                if graph[i][j] == 1:
                    nodes.append(j)
            self.graph_to_dict[i] = nodes

        return self.graph_to_dict

    def BFS_matrix(self, start):  # Matris üzerinden BFS
        Graph.adj = self.matrix_of_graph
        self.v = self.graph_size
        self.e = self.graph_size - 1
        visited = [False] * self.v  # ilk durumda hic bir kose ziyaret edilmedigiicin false.
        q = [start]
        visited[start] = True  # ilk dugum ziyaret edildi.
        while q:
            vis = q[0]
            print(vis, end=' ')
            q.pop(0)  # ziyaret edildikten sonra dugumu cikart
            for i in range(self.v):
                if (Graph.adj[vis][i] == 1 and (not visited[i])):
                    q.append(i)
                    visited[i] = True  # ziyaret edilirse true yap ve ekle.
        print("\n")

    def BFS_list(self, start):  # liste üzerinden BFS

        graph = self.graph_to_dict
        visited = []  # ziyaret edilen dügümler
        q = []
        visited.append(start)
        q.append(start)
        while q:
            s = q.pop(0)  # ziyaret edilen dugumu cikart
            print(s, end=" ")
            for neighbour in graph[s]:
                if neighbour not in visited:  # eger ziyaret edilmediyse ekle
                    visited.append(neighbour)
                    q.append(neighbour)

    # Komsuluk listesinin ekranda gosterimi
    def Print_List_Graph(self):
        print("Dugum sayisi: ", self.graph_size)
        print("Komsuluk Listesi:\n")
        graph = self.graph_to_dict
        for x, y in graph.items():
            print(x, ":", y)

    # komşuluk matrisinin ekranda gosterimi
    def Print_Matrix_Graph(self):
        print("\nKomsuluk matrisi:\n")
        print(self.matrix_of_graph)


if __name__ == "__main__":
    Graph = Graph()
    Graph.Matrix_Of_Graph()
    Graph.Graph_To_List()
    Graph.Print_List_Graph()
    Graph.Print_Matrix_Graph()

    print("BFS: \n")
    Graph.BFS_matrix(0)
    Graph.BFS_list(0)