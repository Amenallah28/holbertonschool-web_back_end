export default function appendToEachArrayValue(array, appendString) {
    const text = [];
    for (const idx of array) {
      text.push(appendString + idx);
    }
  
    return text;
  }