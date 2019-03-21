from multiprocessing import Process, Queue
running = True
def fill(q):
        while(running):
            if not q.full():
                q.put('*')
def pull(q):
        while(running):
            if not q.empty():
                print q.get()



if __name__ == '__main__':
    q = Queue()
    filler = Process(target=fill, args=(q,))
    puller = Process(target=pull, args=(q,))
    filler.start()
    puller.start()