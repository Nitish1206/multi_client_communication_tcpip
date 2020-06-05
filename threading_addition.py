import threading
import time

class add_thread(threading.Thread):
    def __init__(self, time_after_value):
        super(add_thread, self).__init__()
        self.time_after_value = time_after_value
        self.add_value = 1

    def run(self):
        while True:
            self.add_value += self.add_value
            time.sleep(self.time_after_value)

    def get_value_from_thread(self):
        return self.add_value

    def kill(self):
        self.killed = True


add_after_1_sec = add_thread(time_after_value=1)
add_after_2_sec = add_thread(time_after_value=2)

add_after_1_sec.start()
add_after_2_sec.start()
counter = 0

while True:
    print(add_after_1_sec.get_value_from_thread())
    print(add_after_2_sec.get_value_from_thread())
    time.sleep(0.3)
    counter+=1
    if counter>10:
        print('break')
        break

add_after_1_sec.kill()
add_after_1_sec.join()
add_after_2_sec.kill()
add_after_2_sec.join()
print("exit....")
exit()