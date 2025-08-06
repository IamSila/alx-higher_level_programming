#!usr/bin/node
// Rectangle Class with validation for width and height

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
