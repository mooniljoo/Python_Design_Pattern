import sys
import threading
import queue


class Consumer(threading.Thread):

    def __init__(self, v_queue):

        # for thread
        threading.Thread.__init__(self)
        self.setDaemon(True)

        # for queue
        self.g_queue = v_queue

    # End of __init__

    def run(self):

        while True:
            try:
                v_value = self.g_queue.get()   # if queue is empty, queue is blocked
                print(f"{threading.currentThread().getName()} => {v_value}")
                self.g_queue.task_done()
            except Exception:
                pass

            if self.g_queue.empty():
                break
        # while

    # End of run

# End of Consumer


def MyThread():

    v_queue = queue.Queue()

    for i in range(5):
        v_consumer = Consumer(v_queue)
        v_consumer.start()

    for i in range(1000):
        v_queue.put(i)

    v_queue.join()


# End of MyThread
MyThread()
