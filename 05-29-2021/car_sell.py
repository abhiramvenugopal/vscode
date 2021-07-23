# Your class should be named `CarSell`.
# Your method should be named `getPromisingCustomers`
# Your method should return the indices of customers who are willing to pay greater than or equal to 90% of the car value
class CarSell:
    def __init__(self,customer_proposals):
        self.customer_proposals=customer_proposals
    def getPromisingCustomers(self):
        ret_list=[]
        for i in range(len(self.customer_proposals)):
            if self.customer_proposals[i]>=900000:
                ret_list.append(i)
        if len(ret_list)==0:
            ret_list.append(-1)
        return ret_list
if __name__ == "__main__":
    num_customers = int(input())
    customer_proposals = []
    for i in range(num_customers):
        customer_proposals.append(int(input()))

    car_sell = CarSell(customer_proposals)
    for j in car_sell.getPromisingCustomers():
        print(j)