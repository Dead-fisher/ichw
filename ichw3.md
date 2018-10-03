#  高速缓存存储器（Cache）结构及工作原理

##  一、Cache是什么？

Cache，高速缓存存储器，是计算机中介于寄存器与主存储器之间的器件，在工作中频繁的接受CPU的访问并读写Cache上的信息。

## 二、Cache有什么用？

![image](https://raw.githubusercontent.com/Dead-fisher/ichw/master/TIM%E5%9B%BE%E7%89%8720181003172429.png)

众所周知，CPU是电脑中最核心最金贵的部件，许多大难度计算都由CPU完成，因此CPU更新换代的速度极快，计算速度在不断的提高。但是与之相背的是，主存储器的读取数据的
速度却无法与之相适应，这导致出现CPU处理速度过快以至于出现处理后等待读取数据的空缺的现象，因而使CPU的效率大打折扣。为了解决这一问题，Cache横空出世，它被用于
CPU与主存储器之间，提前读取主存储器的数据放入自己的储存空间中，等待CPU的访问；同时，Cache与CPU的读取速率比主存储器快的多，因此大大避免了CPU的等待情况的
出现。

相比于主存储器来说，Cache的存储空间更小，读取速度较高，起到了连接主存储器和CPU的桥梁作用

## 三、Cache的结构是什么样子的？

![image](https://img-blog.csdn.net/20171115142152426?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzE1MDU0ODM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

