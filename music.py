import urllib.request
import urllib.parse
import json,traceback
import os
import download

def getid(url):
    '''try:
        id = int(url)
        return id
    except ValueError:
        id = url.split('id=')[-1]
        try:
            id = int(id)
            return id
        except Exception:
            print('嘿，瞧瞧你输入了什么玩意？')
            a = 123 / 0'''

    if url.isdigit():
        return url
    else:
        id = url.split('id=')[-1]
        if id.isdigit():
            return id
        else:
            print('嘿，瞧瞧你输入的什么玩意!')
            raise ValueError('输入的不是歌单id或地址！')

def get(id):
    list = {}   #歌曲名-歌手，id组成的字典
    url = ''.join(["http://music.163.com/api/playlist/detail?id=",str(id)])#歌单地址
    print('正在获取歌单数据...')
    print(url)
    input
    req = urllib.request.urlopen(url)
    html = req.read().decode('utf-8')
    list1 = json.loads(html)    #返回歌单的数据解析
    x = list1['result']['tracks']
    for i in x:
        name = str(i['name'])   #歌名
        song = str(i['artists'][0]['name']) #歌手
        id = str(i['id'])   #歌id，下载用
        x = ''.join([name,r"-",song])#把歌名和歌手拼接成‘歌名-歌手’的格式
        list[x] = id   #歌名歌手和id组成字典
    print("共有",len(list),'首歌')
    return list

def downalfile(list):
    len = 0
    ls = input('输入保存文件夹名(music):\n')
    
    print(ls)
    if ls == '':
        ls = 'music'
        print(ls)
    if os.path.exists(ls):
        print('文件夹已存在')
    else :
        print('正在创建...')
        os.mkdir(ls)
    for i in list:
        name = ''.join([ls,'/',i,'.mp3'])
        song = urllib.parse.quote(list[i])    #歌名-歌手 中文字符转ul，否则下载会出问题
        address = ''.join(['http://music.163.com/song/media/outer/url?id=',song,'.mp3'])  #歌曲下载地址
       # downal.downal(address) #下载进度条失败的尝试
        print('(oﾟvﾟ)ノ开始下载',i,'...')
        
        data = download.download(address,name)
        #data = urllib.request.urlopen(address) #开始下载
        '''try:
            with open(name,"wb+") as f:
                f.write(data) #写入磁盘
                print(i,'下载已完成(￣▽￣)"')
                len += 1
        except FileNotFoundError:
            print ("文件夹不存在,正在创建..")
            os.mkdir(ls)'''
    print(len,'首下载成功..')

if __name__ == '__main__':
    try:
        id = getid(input('输入歌单地址或id:\n'))
        list = get(id)
        downalfile(list)
        input("按任意键退出")

    except Exception:
        print('ERROR!QUITING!\n')
        traceback.print_exc()
        input('\n按任意键退出')
        #traceback.print_exc()
        
