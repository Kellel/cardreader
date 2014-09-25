from msr import msr

class BasicOps(object):
    WRITE = 'write'
    READ = 'read'
    ERASE = 'erase'
    RESET = 'reset'
    TEST = 'test'

    def __init__(self):
        self._ops = { 
            self.WRITE: self.write,
            self.READ: self.read,
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

    def write(self, data):
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
        t2= self.device.read()
        return t2[1:len(t2)-1]

    def write(self, data):
        self.device.write_tracks(t2 = str(data))
        return None

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

    def test(self):
        print("TEST")
        return None

    def write(self, data):
        print("WRITE " + data)
        return None

    def erase(self):
        print("ERASE")
        return None

    def reset(self):
        print("RESET")
        return None

