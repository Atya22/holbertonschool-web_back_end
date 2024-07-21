/* eslint-disable */
export default (array, appendString) => {
  for (const value of array) {
    const index = array.indexOf(value);
    array[index] = appendString + value;
  }

  return array;
};
