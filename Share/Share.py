class Share:

    def __init__(self,share_code, share_quantity, avg=0):
        self.share_code = share_code
        self.share_quantity = float(share_quantity)
        self.average = float(avg)