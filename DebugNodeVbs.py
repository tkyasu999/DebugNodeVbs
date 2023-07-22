#
# \par Copyright (C), 2023, tkyasu999
# @file    DebugNodeVbs.py
# @author  tkyasu999
# @version V1.0.0
# @date    2023/05/28
# @brief   Description: Arbitrary nodes implemented in VBScript (e.g., customized WinActor nodes) can be easily tested in Python.
#
import sys
import subprocess

#
# 引数の辞書化
#
def getArgsDict(args):
    dict = {}
    for i in range(2, len(args)):
        dict[args[i].split('=')[0]] = args[i].split('=')[1]
    return dict

#
# 引数の辞書化
#
def getConcatDict():
    dict = {}
    with open('concat.data', 'r') as f:
        read_list = f.read().split("\n")
        for index, item in enumerate(read_list):
            dict[item.split(',')[0]] = item.split(',')[1]
    return dict

#
# 除外データを読み込み
#
def readExclusive():
    with open('exclusive.data', 'r') as f:
        ex_list = f.read().split("\n")
    return ex_list

#
# 辞書化の該当キーの値を変更
#
def replaceDic(item, dict, concatdict):
    for k, v in dict.items():
        if k in item:
            im = item.split(" =")[0]
            item = item.replace("!" + k + "!", "\"" + v + "\"")
            if im in concatdict:
                item += "\n"
                item += concatdict[im] + " = " + im
    return item

#
# 除外データを含むか確認
#
def checkExclusive(item, ex_list):
    for ix, im in enumerate(ex_list):
        if im in item:
            return False
    return True

#
# シフトJISエンコードのテキストファイルの読み込み
#
def readFile(filename):
    with open(filename, encoding='shift_jis') as f:
        read_list = f.read().split("\n")
        return read_list

#
# 実行ファイルの再構成
#
def saveFile(read_list, dict, concatdict):
    fw = open('execution.vbs', 'w')
    for index, item in enumerate(read_list):
        item = replaceDic(item, dict, concatdict)
        if checkExclusive(item, ex_list):
                fw.write(item+"\n")
    fw.close()

#
# 実行ファイルの実行
#
def executeFile():
    result = subprocess.check_output(['cscript', '.\\execution.vbs'])
    print(result.decode())

#
# Main
#
if __name__ == '__main__':
    args = sys.argv
    
    # 引数の辞書化
    dict = getArgsDict(args)
    print(dict)

    # 結合条件の辞書化
    concatdict = getConcatDict()
    print(concatdict)

    # 除外データを読み込み
    ex_list = readExclusive()
    print(ex_list) 

    # シフトJISエンコードのテキストファイルの読み込み
    read_list = readFile(args[1])

    # 実行ファイルの再構成
    saveFile(read_list, dict, concatdict)

    # 実行ファイルの実行
    executeFile()