from json import JSONEncoder
from twisted.internet.task import cooperate

class AsyncJSON(object):
    def __init__(self,value):
        self._value=value

    def beginProducing(self,consumer):
        self._consumer=consumer
        self._iterable=JSONEncoder().iterencode(self._value)
        self._consumer.registerProducer(self,True)
        self._task=cooperate(self._produce())
        d=self._task.whenDone()
        d.addBoth(self._unregister)
        return d

    def pauseProducing(self):
        self._task.pause()

    def resumeProducing(self):
        self._task.resume()

    def stopProducing(self):
        self._task.stop()

    def _produce(self):
        for ch in self._iterable:
            self._consumer.unregisterProducer()
            return passthrough

