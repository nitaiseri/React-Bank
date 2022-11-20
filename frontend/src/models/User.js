class User {
    constructor(userObject) {
      this.id = userObject["id"];
      this.balance = userObject["balance"];
      this.name = userObject["name"];
    }
  }

  export default User;