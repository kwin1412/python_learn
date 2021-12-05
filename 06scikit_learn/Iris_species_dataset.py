
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
      # Seaborn是基于matplotlib的图形可视化python包
      import seaborn as sns
      import matplotlib.pyplot as plt
      import pandas as pd

      from sklearn.datasets import load_iris
      # 获取鸢尾花小数据集（实例化）
      # 数据集是字典
      iris = load_iris()

      # 把数据转换成dataframe的格式
      # 设置标题
      iris_d = pd.DataFrame(iris['data'], columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
      iris_d['Species'] = iris.target

      print(iris_d)
      def plot_iris(iris, col1, col2):
            sns.lmplot(x = col1, y = col2, data = iris, hue = "Species", fit_reg = False)
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title('Distribution map of iris flower species ')
            plt.show()
      plot_iris(iris_d, 'Petal_Width', 'Sepal_Length')

#数据标准化
def data_stand():
      '''
      标准化：
      X'=(x-mean)/θ
      mean:平均值
      θ:方差
      如果出现异常点，由于具有⼀定数据量，少量的异常点对于平均值的影响并不⼤，从⽽⽅差改变较⼩。
      '''
      import pandas as pd

      # 导入标准差 api
      from sklearn.preprocessing import StandardScaler
      from sklearn.datasets import load_iris

      # 导入数据
      iris_data = load_iris()
      
      iris_d = pd.DataFrame(iris_data['data'], columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
      # 1、实例化⼀个转换器类
      # ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']
      transfer = StandardScaler()
      data = transfer.fit_transform(iris_d['Sepal_Length'])

      print("标准化的结果:\n", data)
      print("每⼀列特征的平均值：\n", transfer.mean_)
      print("每⼀列特征的⽅差：\n", transfer.var_)

def iris_K_nearest_neighbor_train():
      from sklearn.datasets import load_iris
      from sklearn.model_selection import train_test_split
      from sklearn.preprocessing import StandardScaler
      from sklearn.neighbors import KNeighborsClassifier


      # 1.获取数据集
      iris = load_iris()
      # 2.数据基本处理
      # x_train,x_test,y_train,y_test为训练集特征值、测试集特征值、训练集⽬标值、测试集⽬标值
      # iris.data:特征值
      # iris.target：目标值
      # test_size：测试数据集比例，20%
      # random_state：随机划分数据集，如果是None，每次划分就都不一样，如果是固定值，就每次都一样
      x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=11)


      # 3、特征⼯程：标准化
      transfer = StandardScaler()
      # 先拟合数据，然后转化它将其转化为标准形式
      # 这个步骤已经找到数据的转换规则，及均值μ和方差σ^2
      x_train = transfer.fit_transform(x_train)
      # 再标准化测试数据集
      x_test = transfer.transform(x_test)

      # 4、机器学习(模型训练)
      # n_neighbors就是 KNN 的 K 值
      estimator = KNeighborsClassifier(n_neighbors=1)
      estimator.fit(x_train, y_train)
      # 5、模型评估
      # ⽅法1：⽐对真实值和预测值
      y_predict = estimator.predict(x_test)
      print("预测结果为:\n", y_predict)
      print("⽐对真实值和预测值：\n", y_predict == y_test)


      # ⽅法2：直接计算准确率
      score = estimator.score(x_test, y_test)
      print("准确率为：\n", score)


def iris_KNN_K_value_train():
      from sklearn.datasets import load_iris
      from sklearn.model_selection import train_test_split
      from sklearn.preprocessing import StandardScaler
      from sklearn.neighbors import KNeighborsClassifier
      from sklearn.model_selection import GridSearchCV
      # 交叉验证为了让被评估的模型更加准确可信
      # 每组超参数都采⽤交叉验证来进⾏评估。最后选出最优参数组合建⽴模型。
      # 1、获取数据集
      iris = load_iris()
      # 2、数据基本处理 -- 划分数据集
      x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=None)
      # 3、特征⼯程：标准化  
      # 实例化⼀个转换器类
      transfer = StandardScaler()
      # 调⽤fit_transform
      x_train = transfer.fit_transform(x_train)
      x_test = transfer.transform(x_test)
      # 4、KNN预估器流程
      # 4.1 实例化预估器类
      estimator = KNeighborsClassifier()
      # 4.2 模型选择与调优——⽹格搜索和交叉验证
      # 准备要调的超参数
      param_dict = {"n_neighbors": [1, 3, 5]}
      estimator = GridSearchCV(estimator, param_grid=param_dict, cv=3)
      # 4.3 fit数据进⾏训练
      estimator.fit(x_train, y_train)
      # 5、评估模型效果
      # ⽅法a：⽐对预测结果和真实值
      y_predict = estimator.predict(x_test)
      print("⽐对预测结果和真实值：\n", y_predict == y_test)
      # ⽅法b：直接计算准确率
      score = estimator.score(x_test, y_test)
      print("直接计算准确率：\n", score)
      print("在交叉验证中验证的最好结果：\n", estimator.best_score_)
      print("最好的参数模型：\n", estimator.best_estimator_)
      print("每次交叉验证后的准确率结果：\n", estimator.cv_results_)

      return


if __name__=="__main__":
      #iris_dataset_show()
      # iris_dataset_plt()
      #data_stand()
      #dict_traverse()
      #iris_K_nearest_neighbor_train()
      iris_KNN_K_value_train()
      print("run end")