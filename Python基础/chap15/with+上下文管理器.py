class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用')
    def show(self):
        print('show方法被调用')

with MyContentMgr() as file:
    file.show()