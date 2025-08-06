#!usr/bin/node
// Rectangle Class with validation for width and height

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log(('X'.repeat(this.width) + '\n').repeat(this.height).split('')
      .slice(0, -1).join(''));
  }
}
module.exports = Rectangle;
