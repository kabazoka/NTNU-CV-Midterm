

# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:30:45 2021

@author: zxw
"""
# 设置文件路径
import os
import networkx as nx
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

arr = np.array([[43, 73, 93, 71, 35, 36, 53, 27, 45, 17, 76, 13],
                [80, 75, 13, 88, 69, 37, 75, 50, 26, 91, 54, 50],
                [26, 71, 90, 35, 65, 55, 21, 93, 59, 60, 54, 78],
                [92, 13, 67, 92, 61, 43, 31, 89, 94, 41, 25, 33],
                [95, 77, 26, 11, 61, 61, 69, 25, 40, 64, 30, 70],
                [76, 57, 38, 38, 27, 98, 78, 18, 81, 66, 13, 26],
                [69, 62, 26, 68, 97, 91, 33, 95, 53, 55, 36, 21]])

class SeamCarver:
    def __init__(self,picture):
        self.im = Image.open(picture) #读取图片
        self.W = self.im.size[0] #宽度
        self.H = self.im.size[1] #高度
        self.matrix = np.array(Image.open(picture)) #用一个三维矩阵存储像素信息
        self.matrix = self.matrix.astype(int)
        self.energy_matrix = np.arange(self.H*self.W).reshape(self.H,self.W)
        self.energy_matrix = self.energy_matrix.astype(float)
        for i in range(self.H):
            for j in range(self.W):
                Left = (j == 0)
                Right = (j == self.W - 1)
                Top = (i == 0)
                Bottom = (i == self.H-1)
                if (Left)|(Right)|(Top)|(Bottom):
                    self.energy_matrix[i][j] = 1000
                else:
                    dx = self.matrix[i+1][j] - self.matrix[i-1][j]
                    dy = self.matrix[i][j+1] - self.matrix[i][j-1]
                    dx_square = sum(np.square(dx))
                    dy_square = sum(np.square(dy))
                    self.energy_matrix[i][j] =  np.sqrt(dx_square+dy_square)
    #展示图片
    def picture(self):
        plt.imshow(self.matrix)
    #定义能量
    def energy(self,x,y):
        return self.energy_matrix[y][x]
    #定义横向接缝
    #利用矩阵的转置
    def findHorizontalSeam(self):
        t = self.W
        self.W = self.H
        self.H = t
        self.energy_matrix = self.energy_matrix.T
        H_Seam = self.findVerticalSeam()
        self.energy_matrix = self.energy_matrix.T
        t = self.W
        self.W = self.H
        self.H = t
        return H_Seam 
    #定义纵向接缝
    def findVerticalSeam(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([i for i in range(self.W*self.H+2)])
        a = self.W
        b = self.H
        for i in range(a):
            graph.add_edge(0, i+1, weight = 1000)
            graph.add_edge(a*b - i, a*b+1, weight = 0)
        for k in range(a*(b-1)):
            i = k % a
            j = int((k/a))
            if i == 0:
                graph.add_edge(k+1,k+1+a, weight = self.energy(i, j+1))
                graph.add_edge(k+1,k+2+a, weight = self.energy(i+1, j+1))
            elif i == a-1:
                graph.add_edge(k+1,k+a, weight = self.energy(i-1, j+1))
                graph.add_edge(k+1,k+1+a, weight = self.energy(i, j+1))
            else:
                graph.add_edge(k+1,k+a, weight = self.energy(i-1, j+1))
                graph.add_edge(k+1,k+1+a, weight = self.energy(i, j+1))
                graph.add_edge(k+1,k+2+a, weight = self.energy(i+1, j+1))
        Nodes = nx.shortest_path(G=graph,source=0,target=b*a+1,weight='weight')[1:-1]
        V_Seam = []
        for i in range(len(Nodes)):
            V_Seam.append((Nodes[i] % a)-1)
        return V_Seam
    def removeHorizontalSeam(self,seam):
        New_matrix = np.zeros((self.H-1,self.W,3))
        for i in range(self.W):
            k = 0
            for j in range(self.H):
                if j != seam[i]:
                    New_matrix[k][i] = self.matrix[j][i]
                    k = k+1
        New_matrix = New_matrix.astype(int)
        self.matrix = New_matrix
        New_energy_matrix = np.arange(self.H*(self.W-1)).reshape(self.H,self.W-1)
        New_energy_matrix = New_energy_matrix.astype(float)
        for i in range(self.W):
            k = 0
            for j in range(self.H):
                if j != seam[i]:
                    New_energy_matrix[k][i] = self.energy_matrix[j][i]
                    k = k+1
        self.energy_matrix = New_energy_matrix
        self.H = self.H-1        
    def removeVerticalSeam(self,seam):
        New_matrix = np.zeros((self.H,self.W-1,3))
        for i in range(self.H):
            k = 0
            for j in range(self.W):
                if j != seam[i]:
                    New_matrix[i][k] = self.matrix[i][j]
                    k = k+1
        New_matrix = New_matrix.astype(int)
        self.matrix = New_matrix
        New_energy_matrix = np.arange(self.H*(self.W-1)).reshape(self.H,self.W-1)
        New_energy_matrix = New_energy_matrix.astype(float)
        for i in range(self.H):
            k = 0
            for j in range(self.W):
                if j != seam[i]:
                    New_energy_matrix[i][k] = self.energy_matrix[i][j]
                    k = k+1
        self.energy_matrix = New_energy_matrix
        self.W = self.W-1
# 测试
test= SeamCarver("test.png")
test.picture()
print(test.findVerticalSeam())


# # 定点展示有向图（需构建图）
# import networkx as nx
# import matplotlib.pyplot as plt
# from PIL import Image

# im = Image.open("test.png")
# graph = nx.DiGraph()
# graph.add_nodes_from([i for i in range(32)])
# graph.add_edges_from([(i, i+1) for i in range(0, 31, 6)])
# graph.add_edges_from([(i, i+6) for i in range(6)])
# graph.add_edges_from([(i, i+7) for i in range(0, 25, 6)])
# graph.add_edges_from([(i, i+5) for i in range(1, 31, 6)])
# pos = {}
# for node in graph.nodes():
#     if node == 0:
#         pos[node] = (3,-3)
#     elif node == 31:
#         pos[node] = (3,6)
#     else:
#         pos[node] = ((node-1) % 6,int((node-1)/6))
# nx.draw(graph,pos,with_labels = True)
# plt.show()
