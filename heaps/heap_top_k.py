import heapq
import time
import random


class Bank:

    def __init__(self):
        self.accounts = {}
        self.size = 0

    def create_account(self, timestamp: int, account_id: str):
        # try:
        #     if self.accounts[account_id]:
        #         return False
        # except KeyError:
        #     #Left value is balance and the other is spending history
        #     self.accounts[account_id] = [0,0]
        #     return True

        if self.check_account(account_id):
            return False
        else:
            self.accounts[account_id] = [0,0]
            return True

    def deposit(self, timestamp: int, account_id:str, amount: int) -> int:
        if self.check_account(account_id):
            total = self.accounts[account_id][0] + amount
            self.accounts[account_id][0] = total
            return total


        return None
    
    def withdraw(self, timestamp: int, account_id:str, amount: int) -> int:
        if self.check_account(account_id):  
            money = self.accounts[account_id][0]
            if money - amount > 0:
                self.accounts[account_id][0] -= amount
                self.accounts[account_id][1] += amount 
                return self.accounts[account_id][0]

        return None 
    
    def transfer(self, timestamp:int, source_account_id:str, target_account_id:str, amount:int) -> bool:
        if source_account_id != target_account_id and self.check_account(source_account_id) and self.check_account(target_account_id):
            if self.withdraw(time.time(), source_account_id, amount) and self.deposit(time.time(), target_account_id, amount):
                return self.accounts[source_account_id][0]
        
        return None 
    
    def top_spenders(self, timestamp:int, numSpenders: int):
        if numSpenders >= len(self.accounts):
            return None 

        spenderHeap = []
        count = 0
        for acct in self.accounts:
            spend = self.accounts[acct][1]
            #To fill up the priority queue we will simply push to it 
            if count < numSpenders:
                heapq.heappush(spenderHeap, (spend,acct))
            else: 
                heapq.heappushpop(spenderHeap, (spend, acct))
            count += 1
        spenderRanking = []
        for i in range(numSpenders):
            value = heapq.heappop(spenderHeap)
            spenderString  = f'{value[1]}({value[0]})'
            spenderRanking = [spenderString] + spenderRanking 

        
        return spenderRanking 
    
    def check_account(self, account_id:str):
        #BADA BING
        if self.accounts.get(account_id):
            return True 
        else:
            return False

    def printBank(self):
        for acct in self.accounts:
            print("Acct:", acct, "Balance:", self.accounts[acct][0], "Spend:", self.accounts[acct][1])

        
# def get_max_elems(arr, k:int):
#     priority_queue = []
#     for i in range(len(arr)):
#         heapq.heappush(priority_queue, (-arr[i], "&"))
    

    
#     priority, addon = heapq.heappop(priority_queue)
#     priority, addon = heapq.heappop(priority_queue)
#     priority, addon = heapq.heappop(priority_queue)
#     #priority, addon = heapq.heappop(priority_queue)

#     print("PRI", priority, "ADDON",addon)
#     print(priority_queue)
    
#     # for j in range(k, len(arr)):
#     #     heapq.nlargest
#     #     heapq.heappushpop(newHeap, arr[j])

   


def main():
    newBank = Bank()
    print(newBank.create_account(time.time(), 'acc1'))
    print(newBank.create_account(time.time(), 'acc1'))
    for i in range(2, 10):
        newBank.create_account(time.time(), f'acc{i}')
        newBank.deposit(time.time(), f'acc{i}', random.randint(1, 800))
    
    for i in range(5):
        randacct1 = random.randint(1, 9)
        randacct2 = random.randint(1, 9)
        newBank.transfer(time.time(), f'acc{randacct1}', f'acc{randacct2}', random.randint(1, 800))

    for i in range(5):
        randacct1 = random.randint(1, 9)
        randacct2 = random.randint(1, 9)
        newBank.transfer(time.time(), f'acc{randacct1}', f'acc{randacct2}', random.randint(1, 800))


    
    print(newBank.top_spenders(time.time(), 5))
    newBank.printBank()




if __name__ == "__main__":
    main()