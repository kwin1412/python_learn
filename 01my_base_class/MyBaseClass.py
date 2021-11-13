import os
import time
import logging
import sys
import json
import re
import datetime

__author__="kwin"

class MyBaseClass():
      def __init__(self):
            self.logger = self.LoggerInit()
            self.logger.info("{}() Finished".format(sys._getframe().f_code.co_name))
            return
      
      def LoggerInit(
                        self,
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
            log_name=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".log"
            

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
      def CheckFolder(self,folder_path="./",if_create=False):
            """
            @brief:           检查文件夹，是否创建不存在文件夹

            @folder_path:     需要检查的文件夹
            @if_create：      如果不存在是否需要创建
            @return:          存在/创建成功True,否则False
            """
            #self.logger.info(dir_lists)

            if(os.path.exists(folder_path)):
                  self.logger.info("{} exists".format(folder_path))
                  self.logger.info("{}() Finished".format(sys._getframe().f_code.co_name))
                  return True
            
            # 需要创建文件夹的话，就遍历创建
            if(if_create==True):
                  self.logger.info("{} is creating".format(folder_path))
                  os.makedirs(folder_path)
                  if(os.path.exists(folder_path)):
                        self.logger.info("{} is created".format(folder_path))
                        self.logger.info("{}() Finished".format(sys._getframe().f_code.co_name))
                        return True

            self.logger.info("{} is not exists".format(folder_path))
            self.logger.info("{}() Finished".format(sys._getframe().f_code.co_name))
            return False


      # 检查文件，是否创建不存在文件
      def CheckFile(self,path_filename,if_create=False):
            """
            @brief:           检查文件，是否创建不存在文件

            @folder_path:     需要检查的文件
            @if_create：      如果不存在是否需要创建
            @return:          存在/创建成功True,否则False
            """
            path,filename=os.path.split(path_filename)
            self.logger.info("{} ,{}".format(path,filename))

            if (os.path.exists(path_filename)):
                  return True

            # 文件夹都不存在，就是文件不存在
            if(self.CheckFolder(path,if_create)!=True):
                  self.logger.info("{} not exists".format(path_filename))
                  return False

            # 如果不存在,就创建
            if not (os.path.exists(path_filename)):
                  if(if_create==True):
                        with open(path_filename,"w") as fp:
                              self.logger.info("{} is Created".format(path_filename))
                              fp.close()
                              self.logger.info("{}() Finished".format(sys._getframe().f_code.co_name))
                              return True

            self.logger.info("{} not exists".format(path_filename))            
            self.logger.info("{}() Finished".format(sys._getframe().f_code.co_name))
            return False
            
            
            
      
      def ListFolders(self):
            return 
      
      def ListFiles(self):
            return

      # 获取时间
      def GetTimeFormat(self,fmt="%Y-%m-%d %H:%M:%S"):
            """
            @ brief:    按照格式输出当前时间

            @ fmt：     时间格式
            @ return:   当前时间
            """
            now=datetime.datetime.now()
            result=now.strftime(fmt)
            self.logger.info("Time is {} ".format(result))
            self.logger.info("{}() Finished".format(sys._getframe().f_code.co_name))
            return result


      # 加载json文件
      def LoadJson(
                  self,
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
            if(self.CheckFile(json_path_filename)==False):
                  self.ErrorHandle("{} not Exists".format(json_path_filename)) 


            # 读取文件
            with open(json_path_filename,"r") as fp:
                  try:
                        result = json.load(fp)
                  except Exception as e:
                        self.ErrorHandle(e) 

            #json文件内容检查
            if(check_lists!=[]):
                  for check_index in check_lists:
                        try:
                              a=result[check_index]
                        except Exception as e:
                              self.ErrorHandle(e) 

            # 检查文件内容
            return result

      def SaveJson(self,path_filename,content,if_create=False):
            """
            @ brief:          保存json文件

            @ path_filename:  目标文件
            @ content         dict()内容  
            @ if_create       是否创建文件
            @ return:         保存成功True
            """
            

            if(self.CheckFile(path_filename,if_create)==True):
                  with open(path_filename,"w") as fp:
                        json.dump(content,fp,indent = 4)
                        fp.close()
                        return True
            else:
                  self.ErrorHandle("json create failed!")


      def ErrorHandle(self,error_info):
            """
            @brief:           严重的错误处理，退出程序

            @error_info:      错误信息
            @return
            """
            
            self.logger.error(error_info)
            self.logger.error("The program has encountered a serious error and is about to exit!!")
            os.system("pause")
            sys.exit(0)
            




if __name__=="__main__":
      mbc=MyBaseClass()
      #print(mbc.GetTime())
      #mbc.CheckFile(r"D:\code_wokspace\vscode_python\my_python_test\note\dd.tt",True)
      #mbc.ErrorHandle("111")
      
      #mbc.LoadJson("./config.json")
      
      dict_txt=[
            [1,2],
            2,
            3,
      ]
      mbc.SaveJson("./config.json",dict_txt)
      print(mbc.LoadJson("./config.json"))

