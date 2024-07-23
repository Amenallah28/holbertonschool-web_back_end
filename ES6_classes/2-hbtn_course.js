export default class HolbertonCourse {
    constructor(name, length, students) {
      this._name = name;
      this._length = length;
      this._students = students;
      if (typeof (name) !== 'string') { throw new TypeError('Name must be a string'); }
  
      if (typeof (length) !== 'number') { throw new TypeError('Length must be a Number'); }
  
      if (!Array.isArray(students)) { throw new TypeError('Students must be an Array'); }
    }
  
    get name() {
      return this._name;
    }
  
    set name(namee) {
      if (typeof (namee) !== 'string') { throw new TypeError('Name must be a string'); }
      this._name = namee;
    }
  
    get length() { return this._length; }
  
    set length(lengthh) {
      if (typeof (lengthh) !== 'number') { throw new TypeError('Length must be a Number'); }
      this._length = lengthh;
    }
  
    get students() {
      return this._students;
    }
  
    set students(studentss) {
      if (!Array.isArray(studentss)) { throw new TypeError('Students must be an Array'); }
  
      this._students = studentss;
    }
  }
  