'''
Author: your name
Date: 2021-05-16 15:18:18
LastEditTime: 2021-05-16 22:48:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \ColorSpace\ColorSpace.py
'''


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
      a=np.zeros((255,255,3),dtype=int)
      for g in range(0,255):
            for r in range(0,255):
                  for b in range(0,255):
                        a[254-r][b][0]=b
                        a[254-r][b][1]=100
                        a[254-r][b][2]=r

      #print(a)
      img=Image.fromarray(np.uint8(a))
      img.show()
      return


def Show3D():
      # 定义figure
      fig = plt.figure()
      # 创建3d图形的两种方式
      # 1、将figure变为3d
      ax = Axes3D(fig)
      # 2、ax = fig.add_subplot(221, projection='3d')

      # 定义x, y
      x = np.arange(-5, 5, 1)
      y = np.arange(-5, 5, 1)

      # 生成网格数据，相当于笛卡尔积
      X, Y = np.meshgrid(x, y)

      # 计算每个点对的长度
      R = np.sqrt(X ** 2 + Y ** 2)
      
      Z = np.sin(R)

      # 绘制3D曲面
      ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = plt.get_cmap('coolwarm'))
      # rstride:行之间的跨度  cstride:列之间的跨度
      # rcount:设置间隔个数，默认50个，ccount:列的间隔个数  不能与上面两个参数同时出现
      # cmap参数可以控制三维曲面的颜色组合, 一般三维曲面就是 rainbow 的，可以使用collwarm
      # 你也可以修改 rainbow 为 coolwarm, 验证我的结论

      # 底部的投影
      #ax.contour(X, Y, Z, zdir = 'z', offset = -1, cmap = plt.get_cmap('rainbow'))
      # zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
      # zdir = 'z', offset = -1 表示投影到z = -1上

      # 设置z轴的维度，x,y类似
      ax.set_zlim(-2, 2)
      plt.show()



if __name__=="__main__":
      Show3D()
      #main()