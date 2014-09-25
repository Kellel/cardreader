import multiprocessing as mp
from Queue import Empty

def _worker(workq, statusq):
    from ops import MSROps as Ops

    try:
        o = Ops("/dev/ttyUSB0")
    except:
        statusq.put(("DEVICE SETUP FAILED", None))


    while True:
        command, data = workq.get()
        result = None

        try:
            status, result = o.run(command, data)
        except:
            status = "COMMAND EXECUTION FAILED"
        finally:
            statusq.put((status, result))

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Worker:
#    __metaclass__ = Singleton

    def __init__(self, device):
        from ops import BasicOps as ops

        self.ops = ops
        self.workq = mp.Queue()
        self.statusq = mp.Queue()
        self.p = mp.Process(target=_worker, args=(self.workq, self.statusq,))

        self.p.start()

    def read(self):
        self.workq.put((self.ops.READ, None))

    def read_tracks(self):
        self.workq.put((self.ops.READTRACKS, None))

    def write(self, data):
        self.workq.put((self.ops.WRITE, data))

    def writetracks(self, track1 = None, track2 = None, track3 = None):
        t1 = track1 or self.ops.BLANK
        t2 = track2 or self.ops.BLANK
        t3 = track3 or self.ops.BLANK

        data = "|".join([t1, t2, t3])

        self.workq.put((self.ops.WRITETRACKS, data))

    def reset(self):
        self.workq.put((self.ops.RESET, None))

    def erase(self):
        self.workq.put((self.ops.ERASE, None))

    def test(self):
        self.workq.put((self.ops.TEST, None))

    def get_status(self):
        try:
            status, result = self.statusq.get_nowait()
        except Empty:
            return None, None
        else:
            return status, result

    def terminate(self):
        self.p.terminate()

if __name__ == "__main__":
    w = Worker("/dev/ttyUSB0")
    w.read()
    w.write("1234")
    w.reset()

    import time

    time.sleep(5)
    
    print(w.statusq.get())
    print(w.statusq.get())
    print(w.statusq.get())

    w.terminate()
