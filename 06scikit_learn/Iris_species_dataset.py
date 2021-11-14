
def dict_traverse():
      # 遍历字典
      dict_temp={
            "key1":1,
            "key2":2,
            "key3":3,
      }

      # 打印字典全部的键对值
      print(dict_temp.items())

      # 打印所有的键值
      print(dict_temp.keys())

      # 打印所有的值
      print (dict_temp.values())



def iris_dataset_show():
      from sklearn.datasets import load_iris,fetch_20newsgroups
      # 获取鸢尾花小数据集（实例化）
      # 数据集是字典
      iris = load_iris()

      # # 获取20种新闻的大数据集
      # 通过生成对象 获取到大数据集，保存到当前的目录下
      # news20=fetch_20newsgroups(data_home="./")

      # 打印数据集是所有键值
      print("鸢尾花数据集的 dict：\n", iris.keys())
      for key in iris.keys():
            print(key)
      # dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
      print("鸢尾花数据集的 data : \n",iris["data"])
      print("鸢尾花数据集的 target : \n",iris["target"])
      print("鸢尾花数据集的 frame : \n",iris["frame"])
      print("鸢尾花数据集的 target_names : \n",iris["target_names"])
      print("鸢尾花数据集的 DESCR : \n",iris["DESCR"])
      print("鸢尾花数据集的 feature_names : \n",iris["feature_names"])
      print("鸢尾花数据集的 filename : \n",iris["filename"])
      print("鸢尾花数据集的 data_module : \n",iris["data_module"])

      #print("鸢尾花数据集的返回值：\n", iris)

      # 返回值是⼀个继承⾃字典的Bench
      # print("鸢尾花的特征值:\n", iris["data"])
      # print("鸢尾花的⽬标值：\n", iris.target)
      # print("鸢尾花特征的名字：\n", iris.feature_names)
      # print("鸢尾花⽬标值的名字：\n", iris.target_names)
      # print("鸢尾花的描述：\n", iris.DESCR)



def iris_dataset_plt():
      # 内嵌绘图
      import seaborn as sns
      import matplotlib.pyplot as plt
      import pandas as pd

      from sklearn.datasets import load_iris,fetch_20newsgroups
      # 获取鸢尾花小数据集（实例化）
      # 数据集是字典
      iris = load_iris()

      # 把数据转换成dataframe的格式
      iris_d = pd.DataFrame(iris['data'], columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
      iris_d['Species'] = iris.target

      def plot_iris(iris, col1, col2):
            sns.lmplot(x = col1, y = col2, data = iris, hue = "Species", fit_reg = False)
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title('Distribution map of iris flower species ')
            plt.show()
      plot_iris(iris_d, 'Petal_Width', 'Sepal_Length')

#数据标准化
def data_stand():
      import pandas as pd
      from sklearn.preprocessing import StandardScaler

if __name__=="__main__":
      iris_dataset_show()
      iris_dataset_plt()
      #dict_traverse()
      print("run end")