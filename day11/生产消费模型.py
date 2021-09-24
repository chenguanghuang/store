from threading import Thread
import threading
import time
basket = 0
many= 3000
lock = threading.Lock()
# --------------------------厨师------------------------------
class Cooker(Thread):
    bread = 0
    def run(self)->None:
        global basket
        while True:
            self.bread = self.bread + 1
            basket = self.bread
            time.sleep(0.5)
            if 0 <= basket < 500:
                pass
            elif basket == 500:
                # time.sleep(1)
                for i in range(5):
                    print(".", end=' ')
                    time.sleep(0.2)
            elif many == 0:
                break
            # else:
            #     print("面包数:",basket)
            #     break

#--------------------------------顾客-------------------------
class Customer(Thread):
    def run(self)->None:
        global basket,many
        while True:
            if many >0 :
                with lock:
                    basket = basket - 1
                    many = many-2
                print("剩余金额:", many)
                # print("剩余面包数:", basket)
                # break
                if basket ==0:
                    time.sleep(1)
                    print('当前面包数:',basket)
            elif many == 0 or basket < 0:
                break




c1 = Cooker()
c2 = Cooker()
c3 = Cooker()




p1 = Customer()
p2 = Customer()
p3 = Customer()
p4 = Customer()
#
p1.start()
p2.start()
p3.start()
p4.start()

c1.start()
c2.start()
c3.start()
