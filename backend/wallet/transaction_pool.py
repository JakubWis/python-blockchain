class TransactionPool:
    def __init__(self):
        self.transaction_map = {}

    def set_transaction(self, transaction):
        """"
        Set a transaction in the transaction pool.
        """
        self.transaction_map[transaction.id] = transaction

    def existing_transaction(self, address):
        """
        Find a transaction from the transaction pool with matching address.
        """
        for transaction in self.transaction_map.values():
            if transaction.input['address'] == address:
                return transaction

    def update_or_add_transaction(self, transaction):
        """
        Update a transaction in the transaction pool.
        """
        self.transaction_map[transaction.id] = transaction

    def transaction_data(self):
        """
        Return the transactions of the transaction pool represented in the json serialize from.
        """
        return list(
            map(
                lambda transaction: transaction.to_json(),
                self.transaction_map.values()
            )
        )

    def clear_blockchain_transactions(self, blockchain):
        """
        Delete blockchain transactions from the transaction pool.
        """
        for block in blockchain.chain:
            for transaction in block.data:
                try:
                    del self.transaction_map[transaction['id']]
                except KeyError:
                    pass
