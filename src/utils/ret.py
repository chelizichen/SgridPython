class R:
    @staticmethod
    def success(data):
        return {
            "code": 0,
            "msg": "ok",
            "data": data
        }
