'''
@说明        :图书馆系统设计与实现
@时间        :2021/12/16 11:07:10
@作者        :ChangYi Li
@版本        :1.0
'''

import os
import sys
import re

#图书信息保存在d:\data.txt
book_lib_path=r'd:\data.txt'


'''
@说明        :添加图书
@时间        :2021/12/15 18:26:08
@作者        :ChangYi Li
@版本        :1.0
'''
def add_book(all_book_lib,book_id):
    if book_id in all_book_lib.keys():
        print("ID已存在")
        return all_book_lib
    else:
        book_name=input("请输入添加图书名：")
        book_loc=input("请输入图书存放位置(形如1-2-1)：")
        # line_info='{'+'"book_id":"'+str(book_id).zfill(3)+'",'+'"book_name":"'+book_name+'",'+'"book_loc":"'+book_loc+'"}'
        # print("写入",line_info)
        all_book_lib[book_id]=[book_name,book_loc]
        return all_book_lib

'''
@说明        :查阅图书
@时间        :2021/12/15 18:26:42
@作者        :ChangYi Li
@版本        :1.0
'''
def search_book(all_book,book_name):
    search_book_count=0
    for key in all_book.keys():
        if book_name in all_book[key]:
            search_book_count+=1
            print("book_name:{},book_id:{},book_loc:{}".format(book_name,str(key).zfill(3),all_book[key][1]))
    if search_book_count>0:
        print("搜索图书成功")
    pass

'''
@说明        :删除图书
@时间        :2021/12/15 18:27:17
@作者        :ChangYi Li
@版本        :1.0
'''
def remove_book(all_book,book_name):
    book_name_count=0
    for key in all_book.keys():
        if book_name in all_book[key]:
            book_name_count+=1
            del all_book[key]
            print("删除图书成功")
    if book_name_count>0:
        pass
    else:
        print("不存在该图书")
    return all_book
    pass

'''
@说明        :修改图书信息
@时间        :2021/12/15 18:27:51
@作者        :ChangYi Li
@版本        :1.0
'''
def update_book(all_book,book_id):
    if book_id in all_book.keys():
        book_name=input("输入修改书名：")
        book_loc=input("输入修改存放位置")
        all_book[book_id]=[book_name,book_loc]
        print("修改图书成功")
    else:
        print("修改失败")
    return all_book
    pass

'''
@说明        :显示所有图书信息
@时间        :2021/12/15 18:28:32
@作者        :ChangYi Li
@版本        :1.0
'''
def list_all_book_info(all_book):
    for key in all_book.keys():
        print("{},\t{},\t{}".format(str(key).zfill(3),all_book[key][0],all_book[key][1]))
    pass

'''
@说明        :退出图书管理系统
@时间        :2021/12/15 18:45:37
@作者        :ChangYi Li
@版本        :1.0
'''
def exit_book_manage_system(book_path,all_book):
    with open(book_path,'w',encoding='utf-8') as handle:
        handle.truncate(0)
        for key in all_book.keys():
            line_info='{'+'"book_id":"'+str(key).zfill(3)+'",'+'"book_name":"'+all_book[key][0]+'",'+'"book_loc":"'+all_book[key][1]+'"}\n'
            handle.writelines(line_info)
    print('退出图书管理系统')
    pass

'''
@说明        :加载图书信息
@时间        :2021/12/15 19:08:08
@作者        :ChangYi Li
@版本        :1.0
'''
def load_book_lib_info(book_lib_path):
    book_lib_info={}
    #with open(book_lib_path,'r+',encoding='utf-8') as handle:
    try:
        with open(book_lib_path,'r+',encoding='utf-8') as handle:
            for line in handle:
                one_book_info=re.sub('[\{\}"]','',line)
                #one_book_info=re.sub('"','',one_book_info)
                one_book_info=one_book_info.split(',')
                book_id=int(one_book_info[0].split(':')[1])
                book_name=str(one_book_info[1].split(':')[1])
                book_loc=str(one_book_info[2].split('\n')[0].split(':')[1])
                book_lib_info[book_id]=[book_name,book_loc]
    except:
        f=open(book_lib_path,'w',encoding='utf-8')
        f.close()
    return book_lib_info

'''
@说明        :关闭文件handle
@时间        :2021/12/15 19:53:51
@作者        :ChangYi Li
@版本        :1.0
'''
def close_book_lib(handle):
    try:
        handle.close()
        print('关闭图书馆')
    except:
        pass


if __name__=="__main__":
    print('''
    ----------图书馆系统设计与实现-----------\n
    欢迎来到图书管理系统  powerd by ChangYi Li\n
    ---------------菜单提示---------------\n
    -------------[1].添加图书-------------\n
    -------------[2].查询图书-------------\n
    -------------[3].删除图书-------------\n
    -------------[4].修改图书信息----------\n
    -------------[5].显示所有图书----------\n
    -------------[6].退出-----------------\n
    
    ''')
    
    user_input=0
    all_book=load_book_lib_info(book_lib_path=book_lib_path)
    
    while 1:
        user_input=int(input('请输入您的指令：\n'))
        try:
            if user_input==6:
                exit_book_manage_system(book_path=book_lib_path,all_book=all_book)
                break
            elif user_input==1:
                book_id=int(input("输入存放ID："))
                all_book=add_book(all_book_lib=all_book,book_id=book_id)

            elif user_input==2:
                book_name=input("输入查询的书名：")
                search_book(all_book=all_book,book_name=book_name)

            elif user_input==3:
                book_name=input("请输入需要删除的图书名：")
                all_book=remove_book(all_book=all_book,book_name=book_name)
                
            elif user_input==4:
                book_id=int(input("请输入需要修改的图书ID号："))
                all_book=update_book(all_book=all_book,book_id=book_id)

            elif user_input==5:
                list_all_book_info(all_book=all_book)

            else:
                print('输入有误，请重新输入：')

        except:
            pass







