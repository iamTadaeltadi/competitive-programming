class Solution(object):
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        # make a defaultdict to save the transactions first
        mapped_transactions = collections.defaultdict(lambda: collections.defaultdict(set))

        # go through the transactions and save all of them in the structure    
        for transaction in transactions:
            name, time, amount, city = Solution.parse_transaction(transaction)
            mapped_transactions[name][time].add(city)
        
        # go through the transactions again and check for invalid ones
        result = []
        for transaction in transactions:

            # parse the transcation
            name, time, amount, city = Solution.parse_transaction(transaction)
            
            # check for the amount
            if amount > 1000:
                result.append(transaction)
                continue
            
            # check whether we have a transaction with the same name
            if name not in mapped_transactions:
                continue
            
            # check if other transaction exist within the invalid timeframe
            for time_point in range(time-60, time+61):

                # time point does not exist
                if time_point not in mapped_transactions[name]:
                    continue

                # check if there are more cities in within the time frame and the name
                # and if it is only one check that it is not the same city!
                if len(mapped_transactions[name][time_point]) > 1 or (city not in mapped_transactions[name][time_point]):
                    result.append(transaction)
                    break
                                        
        return result
    
    @staticmethod
    def parse_transaction(transaction: str) -> Tuple[str, int, int, str]:
        name, time, amount, city = transaction.split(',')
        time = int(time)
        amount = int(amount)
        return name, time, amount, city