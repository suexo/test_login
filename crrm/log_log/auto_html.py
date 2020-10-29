import logging
import time


class Autolog:
    def __init__(self):
        self.logger=logging.getLogger('log')

    def set_message(self,mess,level):
        try:
            self.logger = logging.getLogger('log')
            data_time = time.strftime('%Y-%m-%d', time.localtime())
            # 创建文件
            fh = logging.FileHandler('../../log/mylog' + data_time + '.log')
            # 创建控制台
            ch = logging.StreamHandler()
            # 格式化
            fm = logging.Formatter('%(levelname)s %(asctime)s %(message)s')
            # 对文件格式
            fh.setFormatter(fm)
            # 对控制台格式
            ch.setFormatter(fm)
            # 文件加到logger对象
            self.logger.addHandler(fh)
            # 控制台句柄加入logger
            self.logger.addHandler(ch)
            # 设置打印级别
            self.logger.setLevel(logging.DEBUG)
            # 输出info
            if level=='debug':
                self.logger.debug(mess)
            elif level=='info':
                self.logger.info(mess)
            else:
                pass
            # 移除文件句柄
            self.logger.removeHandler(fh)
            # 移除控制台
            self.logger.removeHandler(ch)
            # 关闭文件
        except:
            print('file except')
        finally:
            fh.close()

# if __name__=='__main__':
#     logg=Autolog()
#     url='http://www.baidu.com/'
#     logg.set_message('打开浏览器'+url,'info')