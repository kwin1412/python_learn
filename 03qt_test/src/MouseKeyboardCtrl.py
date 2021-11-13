from MyBaseClass import MyBaseClass
import pyautogui
import sys
from pynput import mouse
from pynput import keyboard

import time
import datetime
from threading import Thread

class MouseKeyboardCtrl(MyBaseClass):

      least_time=0
      thread_close=0
      action_list=[]

      key_board_value={
            "alt":      keyboard.Key.alt,
            "alt_l":    keyboard.Key.alt_l,
            "alt_r":    keyboard.Key.alt_r,
            "alt_gr":   keyboard.Key.alt_gr,
            "backspace":keyboard.Key.backspace,
            "caps_lock":keyboard.Key.caps_lock,
            "cmd":      keyboard.Key.cmd,
            "cmd_l":    keyboard.Key.cmd_l,
            "cmd_r":    keyboard.Key.cmd_r,
            "ctrl":     keyboard.Key.ctrl,
            "ctrl_l":   keyboard.Key.ctrl_l,
            "ctrl_r":   keyboard.Key.ctrl_r,
            "delete":   keyboard.Key.delete,
            "down":     keyboard.Key.down,
            "end":      keyboard.Key.end,
            "enter":    keyboard.Key.enter,
            "esc":      keyboard.Key.esc,
            "f1":       keyboard.Key.f1,
            "f2":       keyboard.Key.f2,
            "f3":       keyboard.Key.f3,
            "f4":       keyboard.Key.f4,
            "f5":       keyboard.Key.f5,
            "f6":       keyboard.Key.f6,
            "f7":       keyboard.Key.f7,
            "f8":       keyboard.Key.f8,
            "f9":       keyboard.Key.f9,
            "f10":      keyboard.Key.f10,
            "f11":      keyboard.Key.f11,
            "f12":      keyboard.Key.f12,
            "f13":      keyboard.Key.f13,
            "f14":      keyboard.Key.f14,
            "f15":      keyboard.Key.f15,
            "f16":      keyboard.Key.f16,
            "f17":      keyboard.Key.f17,
            "f18":      keyboard.Key.f18,
            "f19":      keyboard.Key.f19,
            "f20":      keyboard.Key.f20,
            "f21":      keyboard.Key.f21,
            "f22":      keyboard.Key.f22,
            "f23":      keyboard.Key.f23,
            "f24":      keyboard.Key.f24,
            "home":     keyboard.Key.home,
            "left":     keyboard.Key.left,
            "page_down":keyboard.Key.page_down,
            "page_up":  keyboard.Key.page_up,
            "right":    keyboard.Key.right,
            "shift":    keyboard.Key.shift,
            "shift_l":  keyboard.Key.shift_l,
            "shift_r":  keyboard.Key.shift_r,
            "space":    keyboard.Key.space,
            "tab":      keyboard.Key.tab,
            "up":       keyboard.Key.up,
            "media_play_pause":     keyboard.Key.media_play_pause,
            "media_volume_mute":    keyboard.Key.media_volume_mute,
            "media_volume_down":    keyboard.Key.media_volume_down,
            "media_volume_up":keyboard.Key.media_volume_up,
            "media_previous": keyboard.Key.media_previous,
            "media_next":     keyboard.Key.media_next,
            "insert":   keyboard.Key.insert,
            "menu":     keyboard.Key.menu,
            "num_lock": keyboard.Key.num_lock,
            "pause":    keyboard.Key.pause,
            "print_screen":   keyboard.Key.print_screen,
            "scroll_lock":    keyboard.Key.scroll_lock
      }
      def __init__(self):
            #super().__init__()

            self.logger=self.LoggerInit(console_level="ERROR")
            self.least_time=datetime.datetime.now()

      def LoadConfig(self):
            config=self.LoadJson()
            self.logger.info("config is {}".format(config))
            self.logger.info("{}() Finished".format(sys._getframe().f_code.co_name))
            return config



      def MouseMoveTo(self):
            print(pyautogui.size())
            
            print(pyautogui.position())
            x,y=pyautogui.size()
            print(x,y)

      def GetDiffTime(self):
            now=datetime.datetime.now()
            diff=now-self.least_time
            self.least_time=now
            self.logger.info("Time is {} ".format(diff))
            self.logger.info("{}() Finished".format(sys._getframe().f_code.co_name))
            return diff.microseconds/1000000

      # 解码mouse event
      # [model,mouse_type,[pos.x,pos.y],click_button,pressed]
      # model:"m"鼠标，"k"键盘
      # mouse_type:"m" move,"c" click
      # click_button:"left" left,"middle" middle, "right" right
      # press: "1" true, "0" false
      def DecodeMouseEvent(self,get_event):
            if  get_event is None:
                  return None

            #print(get_event.__dict__)
            try:
                  if(get_event.button==mouse.Button.left):
                        click_button="left"
                  if(get_event.button==mouse.Button.middle):
                        click_button="middle"
                  if(get_event.button==mouse.Button.right):
                        click_button="right"
                  
                  

                  result=[self.GetDiffTime(),"m","c",[get_event.x,get_event.y],click_button,get_event.pressed]
            except:

                  return None
                  #result=[self.GetDiffTime(),"m","m",[get_event.x,get_event.y]]
            return result
            #print(help(event))
            
      def MouseDo(self,action):
            
            if(action[2]=="c"):
                  pyautogui.moveTo(action[3])
                  if(action[5]==1):
                        pyautogui.mouseDown(button=action[4])
                  elif(action[5]==0):
                        pyautogui.mouseUp(button=action[4])
                  else:
                        self.logger.error("error pressed {}".format(action[5]))
            elif(action[2]=="m"):
                  pyautogui.moveTo(action[3][0]/self.screen_zoom_ratio*100,action[3][1]/self.screen_zoom_ratio*100)
            else:
                  self.logger.error("error mouse_type {}".format(action[3]))

      def ListenMouse(self):
            # The event listener will be running in this block
            with mouse.Events() as events:
            # Block at most one second
                  get_event = events.get(1)
                  return self.DecodeMouseEvent(get_event)

      def TaskListenMouse(self):
            while(True):
                  if(self.thread_close==1):
                        break
                  event=self.ListenMouse()
                  if(event!=None):
                        print(event)
                        self.action_list.append(event)
                        #print(self.action_list)
                        
                        self.logger.info('TaskListenMouse event {}'.format(event))
      
      def DecodeKeyboardEvent(self,get_event):
            if  get_event is None:
                  return None

            #print(get_event.__dict__)
            try:
                  if(get_event.button==mouse.Button.left):
                        click_button="left"
                  if(get_event.button==mouse.Button.middle):
                        click_button="middle"
                  if(get_event.button==mouse.Button.right):
                        click_button="right"
                  
                  

                  result=[self.GetDiffTime(),"m","c",[get_event.x,get_event.y],click_button,get_event.pressed]
            except:

                  return None
                  #result=[self.GetDiffTime(),"m","m",[get_event.x,get_event.y]]
            return result
            #print(help(event))


      def ListenKeyboard(self):
            # The event listener will be running in this block
            with keyboard.Events() as events:
            # Block at most one second
                  event = events.get(1)
                  if not event is None:
                        return event
                  return None

      def TaskListenKeyboard(self):
            while(True):
                  event=self.ListenKeyboard()
                  if(event!=None):
                        print(event)
                        if(event.key==keyboard.Key.esc):
                              
                              self.thread_close=1
                              break
                        self.logger.info('TaskListenKeyboard event {}'.format(event))
                  
      def StartListenMouseKeyboard(self):
            self.listen_mouse_thread=Thread(target=self.TaskListenMouse)
            self.listen_keyboard_thread=Thread(target=self.TaskListenKeyboard)

            self.listen_mouse_thread.start()
            self.listen_keyboard_thread.start()
            self.logger.info('StartListenMouseKeyboard')
            while(True):
                  if(self.thread_close==1):
                        self.listen_mouse_thread.join()
                        self.listen_mouse_thread.join()
                        self.SaveJson("./test.json",self.action_list,True)
                        break
                  time.sleep(1)

      def LoadAction(self,path_filename):
            if(self.CheckFile(path_filename,if_create=False)==False):
                  self.ErrorHandle("can not load action file {}".format(path_filename))
                  

            self.action_list=self.LoadJson(path_filename)
            print(self.action_list)
            
      def delayMicrosecond(self,t):    # 微秒级延时函数
            start,end=0,0           # 声明变量
            start=time.time()       # 记录开始时间
            t=(t-3)/1000000     # 将输入t的单位转换为秒，-3是时间补偿
            while end-start<t:  # 循环至时间差值大于或等于设定值时
                  end=time.time()     # 记录结束时间


if __name__=="__main__":

      #mkc=MouseKeyboardCtrl()

      #print(keyboard.Key.__dict__)
      print(keyboard.Key.esc)
      print(str(keyboard.Key.esc)[4:len(str(keyboard.Key.esc))])
      while(True):
            with keyboard.Events() as events:
            # Block at most one second
                  event = events.get(1)
                  if not event is None:
                        print(event.key)
                        print(type(event.key))
      # mkc.StartListenMouseKeyboard()
      # mkc.LoadAction("./test.json")
      # for action in mkc.action_list:
      #       if(action[1]=="m"):
      #             time.sleep(action[0])
      #             mkc.MouseDo(action)





            