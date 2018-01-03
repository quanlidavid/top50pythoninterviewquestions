# -*- coding: utf-8 -*-
import threading
import time


def test_xc(txt):
    f = open("test.txt", "a")
    f.write("test_dxc"+txt + '\n')
    time.sleep(1)
    f.close()

def test_xc_withlock(txt):
    f = open("test2.txt", "a")
    f.write("test2_dxc"+txt + '\n')
    time.sleep(1)
    mutex.acquire()
    f.close()
    mutex.release()

if __name__ == '__main__':
    mutex = threading.Lock()
    for i in range(5):
        # t = threading.Thread(target=test_xc,args=(str(i),))
        t = threading.Thread(target=test_xc_withlock,args=(str(i),))
        t.start()