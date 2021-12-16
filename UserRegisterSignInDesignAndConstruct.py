
import os
import sys
import re
from typing import Pattern

current_path=os.path.abspath('.')
file_name="register_file.txt"
register_file_path=os.path.join(current_path,file_name)
print("注册信息文件：",register_file_path)

'''
@说明        :加载用户注册信息文件
@时间        :2021/12/16 14:13:24
@作者        :ChangYi Li
@版本        :1.0
'''
def load_user_info(user_info_path):
    user_info_lib={}
    try:
        with open(user_info_path,'r',encoding='utf-8') as handle:
            for line in handle:
                pattern1='\n'
                line=re.sub(pattern1,'',line)
                user_name,user_passwd=line.split(',')[0].split(':')[1],line.split(',')[1].split(':')[1]
                user_info_lib[user_name]=user_passwd
    except:
        f=open(user_info_path,'w',encoding='utf-8')
        f.close()
        
    return user_info_lib

'''
@说明        :用户注册
@时间        :2021/12/16 14:13:09
@作者        :ChangYi Li
@版本        :1.0
'''
def user_register(user_info_lib):
    pattern_pwd=r'[a-zA-Z0-9_!@#$%^&*()]'
    user_name=input("请输入用户名：")
    if user_info_lib is None:
        user_info_lib={}

    else:
        if user_name in user_info_lib.keys():
            print("用户名已存在")
            return user_info_lib
    flag=1
    while flag:
        #限定密码格式
        user_password=input("请输入用户密码：")
        user_password1=re.sub(pattern_pwd,'',user_password)
        if user_password1=='':
            user_info_lib[user_name]=user_password
            flag=0
        else:
            print("密码格式限定为 字母数字及！@#$%^&*()_等特殊字符")

    return user_info_lib
    
    pass

'''
@说明        :用户登录
@时间        :2021/12/16 14:12:40
@作者        :ChangYi Li
@版本        :1.0
'''
def user_login(user_info_lib):
    user_name=input("请输入用户名：")
    if user_name in user_info_lib.keys():
        user_password=input("请输入用户密码：")
        if user_info_lib[user_name]==user_password:
            print("欢迎您，{}".format(user_name))
        else:
            print("密码输入错误，请重新输入")
        
    else:
        print("用户不存在")
    return user_info_lib
    pass

'''
@说明        :退出系统
@时间        :2021/12/16 14:12:56
@作者        :ChangYi Li
@版本        :1.0
'''
def exit_user_system(user_info_path,user_info_lib):
    with open(user_info_path,'w',encoding='utf-8') as handle:
        handle.truncate(0)
        for key in user_info_lib.keys():
            line_info='user_name:{},user_password:{}\n'.format(key,user_info_lib[key])
            handle.writelines(line_info)

'''
@说明        :程序入口
@时间        :2021/12/16 12:11:05
@作者        :ChangYi Li
@版本        :1.0
'''
if __name__=="__main__":
    print('''
    ----------用户注册、登录系统设计与实现-----------\n
               \tpowerd by ChangYi Li\n
    ---------------菜单提示---------------\n
    -------------[1].用户登录-------------\n
    -------------[2].注册账号-------------\n
    -------------[其他任意键].退出-----------------\n
    
    ''')
    
    user_input=0
    user_info_lib=load_user_info(user_info_path=register_file_path)
    while 1:
        user_input=int(input('请输入您的指令：\n'))
        try:
            if user_input==1:
                user_info_lib=user_login(user_info_lib)
            elif user_input==2:
                user_info_lib=user_register(user_info_lib)
            else:
                exit_user_system(user_info_path=register_file_path,user_info_lib=user_info_lib)
                print('退出用户登录系统')
                break
            print(user_info_lib)
        except:
            pass
    pass
