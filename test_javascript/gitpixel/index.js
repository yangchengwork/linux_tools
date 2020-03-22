const getPixels = require("get-pixels");
const gm        = require("gm");
const fs        = require("fs");

const   BLACKCOLOR      = 0
const   DARKCOLOR       = 100
const   LIGHTCOLOR      = 160
const   WHITCOLOR       = 200

// 4.2
const EINK42MAXX        = 300
const EINK42MAXY        = 400

// 寄存器   白   浅灰    深灰    黑
// 0x10      1       1           0         0   
// 0x13      1       0           1         0
const EinkGrayRegister = [[0, 0], [0, 1], [1, 0], [1, 1]];


function start(fileName) {
    // let {data, width, height} = await pixels('1.png');
    // console.log(data, width, height);
    
    // output(await pixels('sulong.png'), 'out.png')
    const tmpFileName = "/tmp/gumpGray.png";
    
    gm(fileName)
    .resize(EINK42MAXX, EINK42MAXY, '!')
    .colorspace('GRAY')
    .write(tmpFileName, err => {
        if (!err) {
            console.log('done');
            return convertBinData(tmpFileName);
        } else {
            console.log(err);
        }
    });
}

function convertBinData(path) {
    getPixels(path, (err, pixels) => {
        if (err) {
            console.log("Bad image path");
            return;
        } else {
            let dx, dy;
            d = pixels.shape.slice();
            dx = d[0]; dy = d[1];
            // console.log("got pixels", dx, dy);

            // let color = [];
            let reg10array = [];
            let reg13array = [];
            let count = 0;
            let reg10 = 0;
            let reg13 = 0;
            
            for (let x=0; x<dx; x++) {
                for (let y=0; y<dy; y++) {
                    let r = pixels.get(x, y, 0);
                    let g = pixels.get(x, y, 1);
                    let b = pixels.get(x, y, 2);
                    if ((r === g) && (g === b)) {
                        /**
                        if (color.indexOf(r) === -1) {
                            color.push(r);
                            // console.log("add Gray", r, g, b);
                        }
                        */
                        let index = 0;
                        if (r > WHITCOLOR) {
                            index = 3;
                        } else if (r > LIGHTCOLOR) {
                            index = 2;
                        } else if (r > DARKCOLOR) {
                            index = 1;
                        }

                        reg10 = (reg10 << 1) + EinkGrayRegister[index][0];
                        reg13 = (reg13 << 1) + EinkGrayRegister[index][1];
                        count += 1;
                        if ((count % 8) == 0) {
                            reg10array.push(reg10);
                            reg13array.push(reg13);
                        }
                        // console.log("dot", x, ":", y, "\t", count);
                    } else {
                        console.log("dot", x, ":", y, "not Gary");
                        return;
                    }
                }
            }
            return reg10array, reg13array;
            // console.log("count", count, reg10array.length);
        }
    });
}

start("sulong.png");


