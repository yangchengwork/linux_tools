// const pixels = require('image-pixels');
// const output = require('image-output');
const getPixels = require("get-pixels");

async function start() {
    // let {data, width, height} = await pixels('1.png');
    // console.log(data, width, height);
    
    // output(await pixels('sulong.png'), 'out.png')
    
    getPixels("1.png", (err, pixels) => {
        if (err) {
            console.log("Bad image path");
            return;
        } else {
            let dx, dy;
            d = pixels.shape.slice();
            dx = d[0]; dy = d[1];
            console.log("got pixels", dx, dy);

            let color = [];
            
            for (let x=0; x<dx; x++) {
                for (let y=0; y<dx; y++) {
                    let r = pixels.get(x, y, 0);
                    let g = pixels.get(x, y, 0);
                    let b = pixels.get(x, y, 0);
                    if ((r === g) && (g === b)) {
                        if (color.indexOf(r) === -1) {
                            color.push(r);
                            console.log("add Gray", r);
                        }
                    } else {
                        console.log("dot", x, ":", y, "not Gary");
                    }
                }
            }
        }
    });
}

start();

//  output([0,1,1,0], [2,2,1], 'a.png');

