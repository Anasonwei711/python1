# -*- coding: utf-8 -*-
import os#加入os库
def rename_files():
    #(1) get file names from a floder
    file_list = os.listdir(r"C:\Users\Administrator\Desktop\50\prank")#r表示rawpack
    #print(file_list)
    saved_path = os.getcwd()#因为出错开始参考内部变量
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\Administrator\Desktop\50\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()