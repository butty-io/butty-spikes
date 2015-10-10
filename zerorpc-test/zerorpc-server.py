import zerorpc

class RequestHandler(object):
        version = '1337'
        myDataStorage = {}

        def getVersion(self):
                return self.version
        def addVals(self, data):
                self.myDataStorage.update(data)
                for item in data:
                        print item
        def getVals(self, keys):
                returnDic = {}
                for key in keys:
                    if key in self.myDataStorage:
                            returnDic.update({key:self.myDataStorage[key]})
                return returnDic
        def add(self, integer):
                return integer + 1
#        def remKeys(self, keys):

s = zerorpc.Server(RequestHandler())
s.bind('ipc:///tmp/requesthandler')
print 'running..'
s.run()
