class Transaction {
    constructor(transactionObject) {
      this.id = transactionObject["id"];
      this.amount = transactionObject["amount"];
      this.vendor = transactionObject["vendor"];
      this.category = transactionObject["category"];
    }
  }

  export default Transaction;