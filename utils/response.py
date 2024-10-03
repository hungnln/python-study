from typing import TypeVar, Generic, List, Dict, Any
T = TypeVar('T')

class Response(Generic[T]):
    @staticmethod
    def make(status: bool = True, msg: str ='',data: T = None):
        return {'status':status,'msg':msg,'data':data}