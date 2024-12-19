# npm install qrcode
const QRCode = require('qrcode');
const fs = require('fs');

const url = 'https://www.youtube.com/watch?v=56_rgF058QI';
const outputPath = 'FG_2_YT.png';

QRCode.toFile(outputPath, url, function (err) {
  if (err) throw err;
  console.log('QR code saved to ' + outputPath);
});



const QRCode = require('qrcode');
const Jimp = require('jimp');

const url = 'https://www.youtube.com/watch?v=56_rgF058QI';

const options = {
  errorCorrectionLevel: 'H',
  margin: 3,
  color: {
    dark: '#FF0000', // Red color
    light: '#FFFF00' // Yellow color
  }
};



# npm install qrcode jimp

// Generate QR code
QRCode.toBuffer(url, options, (err, buffer) => {
  if (err) throw err;

  // Save the image
  Jimp.read(buffer, (err, image) => {
    if (err) throw err;
    image.write('FG_2_YT_2.png', (err) => {
      if (err) throw err;
      console.log('QR code saved to FG_2_YT_2.png');
    });
  });
});
