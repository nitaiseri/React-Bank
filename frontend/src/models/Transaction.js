class TransactionModel {
    constructor(transactionObject) {
      this.id = transactionObject["transaction_id"];
      this.amount = transactionObject["amount"];
      this.vendor = transactionObject["vendor"];
      this.category = transactionObject["category"];
    }
  }

  export default TransactionModel;