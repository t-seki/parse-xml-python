from datetime import datetime


class Measurement:
    def __init__(self) -> None:
        self._count = 0
        self._starttime = datetime.now()

    def increment_count(self, *args, **kwargs):
        self._count += 1

    @property
    def count(self):
        return self._count

    @property
    def elapsed_time(self):
        return datetime.now() - self._starttime
