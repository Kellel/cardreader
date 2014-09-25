from msr import msr

class BasicOps(object):
    WRITE = 'write'
    WRITETRACKS = 'writetracks'
    READ = 'read'
    READTRACKS = 'readtracks'
    ERASE = 'erase'
    RESET = 'reset'
    TEST = 'test'
    BLANK = '^'

    def __init__(self):
        self._ops = { 
            self.WRITE: self.write,
            self.WRITETRACKS: self.writetracks,
            self.READ: self.read,
            self.READTRACKS: self.readtracks,
            self.ERASE: self.erase,
            self.RESET: self.reset,
            self.TEST: self.test
        }

    def run(self, op, data = None):
        try:
            if data:
                result = self._ops[op](data)
            else:
                result = self._ops[op]()
        except Exception as e:
            status = "OP FAILURE [{}]".format(str(e))
        except ValueError:
            status = "NO OPERATION {}".format(op)
        else:
            status = "{} SUCCESS".format(op.upper())
        finally:
            return status, result

    def read(self):
        return ""

    def readtracks(self):
        return ""

    def write(self, data):
        return ""

    def writetracks(self, data):
        return ""

    def erase(self):
        return ""

    def reset(self):
        return ""

class MSROps(BasicOps):
    def __init__(self, device):
        self.device = msr(device)
        super(Ops, self).__init__()

    def test(self):
        return "UNIMPLEMENTED"

    def read(self):
        _, t2, _= self.device.read_tracks()
        return t2[1:len(t2)-1]

    def readtracks(self):
        t1, t2, t3 = self.device.read_tracks()
        return "[{}][{}][{}]".format(t1, t2, t3)

    def write(self, data):
        self.device.write_tracks(t2 = str(data))
        return None

    def writetracks(self, data):
        tracks = data.split('|')
        t1 = tracks[0] if tracks[0] != self.BLANK else None
        t2 = tracks[1] if tracks[1] != self.BLANK else None
        t3 = tracks[2] if tracks[2] != self.BLANK else None
        self.device.write_tracks(t1 = t1, t2 = t2, t3 = t3)

    def erase(self):
        self.device.erase_tracks(True, True, True)
        return None

    def reset(self):
        self.device.reset()
        return None

class TestOps(BasicOps):
    def __init__(self, device):
        super(TestOps, self).__init__()

    def read(self):
        print("READ")
        return "12345"

    def readtracks(self):
        print("READTRACKS")
        return "[t1][t2][t3]"

    def test(self):
        print("TEST")
        return None

    def write(self, data):
        print("WRITE " + data)
        return None

    def writetracks(self, data):
        tracks = data.split('|')
        t1 = tracks[0] if tracks[0] != self.BLANK else None
        t2 = tracks[1] if tracks[1] != self.BLANK else None
        t3 = tracks[2] if tracks[2] != self.BLANK else None
        print(t1, t2, t3)

    def erase(self):
        print("ERASE")
        return None

    def reset(self):
        print("RESET")
        return None

