import os
import time
import logging
import sys
import datetime
import json


def LoggerInit(
                  log_name,
                  log_path=".\\logs\\",
                  file_level="INFO",
                  console_level="INFO"
                  ):
      """
      @ brief:          log对象初始化
      这个初始化不要嵌套其他类内函数，类内函数都有引用logger
                        | level    |
                        | -------- |
                        | CRITICAL |
                        | ERROR    |
                        | WARNING  |
                        | INFO     |
                        | DEBUG    |
                        | NOTSET   | 
                        
      @ log_path_file:  log保存的地址,log名自动生成
      @ file_level:     log file 保存的等级
      @ console_level:  log console 输出等级
      @ return:         log对象
      """
      # 检查文件夹
      #self.CheckFolder(log_path_file)
      if not (os.path.exists(log_path)):
            os.makedirs(log_path)

      # log文件
      log_name=log_name+"_"+datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".log"
      
      #输出到文件
      file_handler =logging.FileHandler(log_path+log_name)
      #输出到控制台 
      console_handler = logging.StreamHandler()

      #设置等级输出到文件
      file_handler.setLevel(file_level)
      #设置等级输出到控制台
      console_handler.setLevel(console_level)

      fmt = "[%(asctime)s]-[ %(funcName)s : %(lineno)s ] - <%(levelname)s> : %(message)s"
      formatter = logging.Formatter(fmt) 

      #设置输出内容的格式
      file_handler.setFormatter(formatter) 
      console_handler.setFormatter(formatter)

      logger = logging.getLogger(__name__)

      #设置基础的等级,默认最低DEBUG
      logger.setLevel('DEBUG')     

      # 绑定文件输出流和控制台输出流
      logger.addHandler(file_handler)   
      logger.addHandler(console_handler)
      

      logger.info("{}() Finished".format(sys._getframe().f_code.co_name))
      return logger


 # 检查文件夹，是否创建不存在文件夹
def CheckFolder(folder_path,if_create=False):
      """
      @brief:           检查文件夹，是否创建不存在文件夹

      @folder_path:     需要检查的文件夹
      @if_create：      如果不存在是否需要创建
      @return:          存在/创建成功True,否则False
      """
      #self.logger.info(dir_lists)

      if(os.path.exists(folder_path)):
            return True
      
      # 需要创建文件夹的话，就遍历创建
      if(if_create==True):
            os.makedirs(folder_path)
            if(os.path.exists(folder_path)):
                  return True
      return False

# 检查文件，是否创建不存在文件
def CheckFile(path_filename,if_create=False):
      """
      @brief:           检查文件，是否创建不存在文件

      @folder_path:     需要检查的文件
      @if_create：      如果不存在是否需要创建
      @return:          存在/创建成功True,否则False
      """
      path,filename=os.path.split(path_filename)

      if (os.path.exists(path_filename)):
            return True

      # 文件夹都不存在，就是文件不存在
      if(CheckFolder(path,if_create)!=True):
            return False

      # 如果不存在,就创建
      if not (os.path.exists(path_filename)):
            if(if_create==True):
                  with open(path_filename,"w") as fp:
                        fp.close()
                        return True
      return False


# 获取时间
def GetTimeFormat(fmt="%Y-%m-%d %H:%M:%S"):
      """
      @ brief:    按照格式输出当前时间

      @ fmt:      时间格式
      @ return:   当前时间
      """
      now=datetime.datetime.now()
      result=now.strftime(fmt)
      return result

# 加载json文件
def LoadJson(
            json_path_filename=".\\config.json",
            check_lists=[]
                  ):
      """
      @ brief:          加载json文件

      @ json_path_file: 目标文件
      @ check_lists     
      @ return:         返回加载的json内容
      """

      # 判断是否文件存在
      if(CheckFile(json_path_filename)==False):
            ErrorHandle("{} not Exists".format(json_path_filename)) 


      # 读取文件
      with open(json_path_filename,"r") as fp:
            try:
                  result = json.load(fp)
            except Exception as e:
                  ErrorHandle(e) 

      #json文件内容检查
      if(check_lists!=[]):
            for check_index in check_lists:
                  try:
                        a=result[check_index]
                  except Exception as e:
                        ErrorHandle(e) 

      # 检查文件内容
      return result

def ErrorHandle(error_info):
      """
      @brief:           严重的错误处理，退出程序

      @error_info:      错误信息
      @return
      """
      print(error_info)
      print("The program has encountered a serious error and is about to exit!!")
      os.system("pause")
      sys.exit(0)
      

def CheckDictIntegrity(_dict,_check_list):
      """
      @brief:           检查字典的完整性

      @_dict:           需要检查的字典
      @_check_list：    字典所有的键值list
      @return
      """

      # 字典为空就是错误
      if not _dict:
            return False
      
      # 字典有键值不存在就是不完整
      for key in _check_list:
            try:
                  _dict[key]
            except:
                  return False

      return True

def CheckValueLegality(_value,_value_list):
      """
      @brief:           检查值的合法性

      @_value:          需要检查的值
      @_value_list:     值的合法性list
      @return
      """ 
      # _value_list 为空，就是正确的
      if not _value_list:
            return True
      # 检查每一个值
      for value in _value_list:
            if (value != _value):
                  return False
      return True


def CheckDictCorrect(_dict,_check_list):
      """
      @brief:           检查字典的正确性

      @_dict:           需要检查的字典
      @_check_list：    字典所有的键值正确值list
      @return
      """ 

      if(len(_dict)!=len(_check_list)):
            return False

      i=0
      for key in _dict.keys():
            if(CheckValueLegality(_dict[key],_check_list[i])==False):
                  return False
            i=i+1
      return True


def print_dict(_dict):
      for key in _dict.keys():
            print(" {} : {} ".format(key,_dict[key]))