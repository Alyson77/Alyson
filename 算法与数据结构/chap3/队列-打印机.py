from queue import Queue
import random
class Printer: #打印机类
    def __init__ (self,ppm):
        self.pagerate=ppm #打印速度,即每分钟打印多少页
        self.currentTask=None #打印任务
        self.timeRemaining=0 #任务倒计时，即当前作业所剩页数除以速度得到所剩打印任务的时间
    def tick(self): #打印机的打印方法，打印的1秒
        if self.currentTask != None:
            self.timeRemaining=self.timeRemaining-1 #打印机正在打印，所剩的任务倒计时减去一秒
            if self.timeRemaining<=0:
                self.currentTask=None #任务倒计时到0了，当前打印作业已完成，打印机进入空闲状态
    def busy(self): #判断打印机是否正在忙
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self,newtask):#开始打印新的作业
            self.currentTask=newtask
            self.timeRemaining=newtask.getPages()*60/self.pagerate #作业打印需要的时间，页数除以打印速度

class Task: #打印作业类
    def __init__(self,time):
        self.timestamp=time #生成一个打印作业的时间戳
        self.pages=random.randrange(1,21) #一本作业可能有1~20页，生成一个打印作业
    def getStamp(self):
        return self.timestamp #返回生成时间戳
    def getPages(self):
        return self.pages #返回该作业到底有多少页
    def waitTime(self,currenttime): #作业在队列中等待的时间
        return currenttime-self.timestamp #作业从生成到开始被打印之间等待的时间

def newPrintTask(): #新生成打印作业，当前的1秒内是否要新生成一个打印作业
    num=random.randrange(1,181) #设定是1小时有10个学生每人打印2本作业，每秒生成新作业概率1/180
    if num ==180: #等于1~180任意值都行，概率都是1/180
        return True
    else:
        return False

def simulation(numSeconds,pagesPerMinute): #模拟打印总时间与打印机设定的打印速度
    labprinter=Printer(pagesPerMinute) #生成打印机对象
    printQueue=Queue() #准备待打印的队列
    waitingtimes=[] #记录生成的每个作业在待打印队列里的等待时间
    for currentSecond in range(numSeconds): #遍历numSeconds时间内的每一秒
        if newPrintTask(): #numSeconds中每秒都判断1/180的概率是否发生，发生的话就生成新打印作业
            task=Task(currentSecond) #生成新的Task对象，把生成作业的时间传参进去
            printQueue.enqueue(task) #把新生成的作业排到待打印队列中去
        if (not labprinter.busy()) and (not printQueue.isEmpty()): #打印机空闲且有队列就开始打印1秒
            nexttask=printQueue.dequeue() #取出待打印队列的队首，准备开始打印
            waitingtimes.append(nexttask.waitTime(currentSecond)) #nexttask在待打印队列的等待时间
            labprinter.startNext(nexttask) #开始打印nexttask作业
        labprinter.tick() #打印1秒，分为打印机正在打印和打印机空闲两种情况
    averageWait=sum(waitingtimes)/len(waitingtimes) #打印这么多作业的总时间除以打印作业的数量
    print('Average wait %6.2f secs %3d tasks remaining' % (averageWait,printQueue.size()))
    #%6.2f：数字整体长度包括小数点一共6位，保留2位小数；%3d：输出3个字符长度的整数；待打印队列里未打印的作业数量
for i in range(10):
    simulation(3600,5)

