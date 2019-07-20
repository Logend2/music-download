import urllib.request,urllib.parse
import time


def formal_byte(byte):
    if byte > 1024:
        KB = byte / 1024
        if KB > 1024:
            MB = KB / 1024
            if MB > 1024:
                GB = MB / 1024
                return "%.2fGB" % GB
            else:
                return '%.2fMB' % MB
        else:
            return '%.2fKB' % KB



def progress(a,b,c):
    '''
    a : 已下载块数目
    b : 文件块大小
    c : 文件总大小
    '''
    space = ' '*20
    _progress = a*b / c * 100
    size = formal_byte(c)
    down_size = formal_byte(a * b)
    speed = formal_byte((a*b)/(time.time() - start_time))
    progress_bar = r'[*******************]'

    if _progress > 5:
        progress_bar = progress_bar.replace('*','#',int(_progress//5))

    end = '' if _progress < 100 else '\n'
    print('%s/s %s%s%.2f%s %s %s \r' % (speed,down_size,progress_bar,_progress,'%',size,space),end=end)


def download(url,name=''):
    if name == '':
        name = url.split('/')[-1]
    name = urllib.parse.unquote(name)
    print(name)
    start_time =time.time()
    urllib.request.urlretrieve(url,name,progress)


start_time =time.time()
if __name__ == '__main__':
    pass
