var array = new ArrayBuffer(8);
// var src = new ArrayBuffer([0x93, 0x88, 0xB1, 0x18, 0x01, 0, 0, 0]);
var src = new Uint8Array(array);
src[0] = 0x93;
src[1] = 0x88;
src[2] = 0xB1;
src[3] = 0x18;
src[4] = 0x01;
var view = new Uint32Array(array);
// console.log(src.length, view.length);
// console.log(view[0] & 0x7f);
let year = 2000 + (view[0] & 0x7f);
let month = (view[0] >> 7) & 0xf;
let day = (view[0] >> 11) & 0x1f;
let hour = (view[0] >> 16) & 0x1f;
let minute = (view[0] >> 21) & 0x3f;
let second = ((view[1] & 0x1) << 5) + ((view[0] >> 27) & 0x1f);
console.log(year + '/' + month + '/' + day + ' ' + hour + ':' + minute + ':' + second);
