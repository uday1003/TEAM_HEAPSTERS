class Graph:
    def __init__ (self):
        self.adj_list = {}
        self.adj_isend=[0]*27
        self.con_wei=[0]*27
        for i in range(0,27):
            self.con_wei[i]= [0]*27
        self.cou=[0]*27

    def insert_string(self,str):
        t = str
        cou=0
        self.add_vertex(0)
       
        self.adj_isend[convert_ascii(str[len(str)-1])] += 1
        for i in t:
            u=convert_ascii(i)
            self.add_vertex(u)
            
            cou += 1
              
        self.adj_list[0].append(str[0])
        for i in range(len(t) - 1):

            u=convert_ascii(t[i])
            self.add_edge(u,t[i+1])
            

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        
        self.adj_list[v1].append(v2)
        self.con_wei[v1][convert_ascii(v2)] +=1
        self.cou[v1] +=1
        self.cou[convert_ascii(v2)]+=1
            

    def print_g(self):
        ch=0
        for vertex in self.adj_list:
            if ch==0:
                if len(self.adj_list[0]) ==0:
                    print(f"{vertex} :","{ }")
                    ch+=1
                else: 
                    print(f"{vertex} : {set(self.adj_list[vertex])}")
                    ch +=1
                    continue
            if self.cou[vertex] == 0:
                
                continue
            if len(self.adj_list[vertex]) == 0:
                print(f"{chr(vertex + 96)} :","{ }")
                ch +=1
            else:
                print(f"{chr(vertex + 96)} : {set(self.adj_list[vertex])}")
                ch +=1
            

    def find_word(self, string):
        if string[0] not in self.adj_list[0]:
            return False
        
        u = convert_ascii(string[0])
        for i in range(1, len(string)):
            if string[i] in self.adj_list[u]:
                u = convert_ascii(string[i])     
            else:
                
                return False
        
        if self.adj_isend[u] >= 1:
           
            return True
        else:
            return False
    def delete_str(self,str):
        if self.find_word(str):
            for i in range(0,len(self.adj_list[0])):
                if self.adj_list[0][i] == str[0]:
                    self.adj_list[0].pop(i)
                    break
            u=str[0]
            for i in range(1,len(str)):
                self.con_wei[convert_ascii(u)][convert_ascii(str[i])] -=1
                u = str[i]
            u=convert_ascii(str[0])
            for i in range(1,len(str)):
                for j in range(0,len(self.adj_list[u])):
                    
                    if self.adj_list[u][j]==str[i] :
                        self.cou[u]-=1
                        self.cou[convert_ascii(str[i])]-=1
                        self.adj_list[u].pop(j)
                        break
                u=convert_ascii(str[i])
            for i in range(0,len(self.adj_list[0])-1):
                if self.adj_list[0][i] == str[0]:
                    self.adj_list[0].pop(i)
            self.adj_isend[convert_ascii(str[len(str)-1])] -=1
            
        else:
            print("the word you tring to delete is not in the graph")

def convert_ascii(cha):
    x = ord(cha)
    if x >=97 and x<=122:
        return x-97+1
    if x>=65 and x<=90:
        return x-65+1

graphs = Graph()
while(True):
    print("type 1 to insert a string\n type 2 to search for a string\n type 3 to delete a string \n 4 to print the adjacent list representation of graph")
    i=int(input())
    if i==1:
        print("enter the string to insert")
        s=input()
        graphs.insert_string(s)
        print("after inserting ",s,"the graph is\n")
        graphs.print_g()
    if i==2:
        print("enter the string to search")
        s=input()
        print(graphs.find_word(s))
    if i==3:
        print("enter the string to delete")
        s=input()
        graphs.delete_str(s)
        print("after deleting ",s,"the graph is\n")
        graphs.print_g()
    if i==4:
        graphs.print_g()
    if i== 5:
        break


