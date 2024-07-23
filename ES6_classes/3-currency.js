export default class Currency {
    constructor(code, name) {
      this._name = name;
      this._code = code;
    }
  
    get name() { return this._name; }
  
    set name(namee) {
      this._name = namee;
    }
  
    get code() { return this._code; }
  
    set code(codee) {
      this._code = codee;
    }
  
    displayFullCurrency() {
      return `${this._name} (${this._code})`;
    }
  }