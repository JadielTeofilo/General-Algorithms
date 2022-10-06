import threading



class Singleton:
    _instance: 'Singleton' = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls, *args, **kwargs) -> None:
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

class Normal:
    pass

import pdb;pdb.set_trace()
