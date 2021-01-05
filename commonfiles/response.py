

def Success(messgae,data=[]):
    response={"Message":messgae,'StatusCode' : 200,'ReplyCode' : 'SUCCESS',"data":data}
    return response



def Failure(message):
    response={'StatusCode' : 400,'ReplyCode' : 'BAD_REQUEST',"message":message}
    return response
