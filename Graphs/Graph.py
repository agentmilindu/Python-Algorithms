class _Vertex:
    
    FLAG_WHITE = 0
    FLAG_GRAY = 1
    FLAG_BLACK = 2
    
    def __init__(self, value):
        self.flag=_Vertex.FLAG_WHITE
        self.value=value
        self.parent=None
        self.distance=None
        self.neighbors=[]

    def get_Neighbors(self):
        return self.neighbors
    def add_neighbor(self, value):
        if value not in self.neighbors:
            self.neighbors.append(value)
    def __hash__(self):
        return self.value.__hash__()
    
    def __str__(self):
        return self.value
    
    def __eq__(self, other):
        return True if self.value is other.value else False
    def __lt__(self, other):
        return True if self.value < other.value else False
    

    
class Graph:
    def __init__(self):
        self.vertices=[]
        
    def add_vertice(self, value):
        if _Vertex(value) not in self.vertices:
            self.vertices.append(self.build_vertex(value))
            
    def get_vertice(self, value):
        if _Vertex(value) not in self.vertices:
            self.add_vertice(value)
        return self.vertices[self.vertices.index(_Vertex(value))]
            
    def get_vertices(self):
        return self.vertices
    
    def get_vertices_count(self):
        return len(self.vertices)
    
    def build_vertex(self,value):
        return _Vertex(value)
         
    def is_vertice(self, value):
        if _Vertex(value) in self.vertices:
            return True
        else:
            return False
        
    def add_edge(self, v1, v2):
        self.get_vertice(v1).add_neighbor(self.get_vertice(v2))





        
