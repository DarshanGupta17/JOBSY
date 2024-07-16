import time

class Delay_Middleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)

        time.sleep(0.075)

        return response