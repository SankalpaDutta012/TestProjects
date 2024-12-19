# npm install pdf-lib
const fs = require('fs');
const path = require('path');
const { PDFDocument } = require('pdf-lib');

async function mergePDFs(outputPath) {
    const pdfDoc = await PDFDocument.create();
    const files = fs.readdirSync(__dirname).filter(file => file.endsWith('.pdf'));

    for (const file of files) {
        const pdfBytes = fs.readFileSync(path.join(__dirname, file));
        const donorPdfDoc = await PDFDocument.load(pdfBytes);
        const copiedPages = await pdfDoc.copyPages(donorPdfDoc, donorPdfDoc.getPageIndices());
        copiedPages.forEach(page => pdfDoc.addPage(page));
    }

    const mergedPdfBytes = await pdfDoc.save();
    fs.writeFileSync(outputPath, mergedPdfBytes);

    console.log(`Merged PDF saved to ${outputPath}`);
}

mergePDFs('combinedUNIDocs.pdf');
