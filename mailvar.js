const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter the EMAIL: ', (email) => {
    let k = 0, j = 0, d = 0;

    if (email.length >= 6) {
        if (isAlpha(email[0])) {
            if (email.includes('@') && email.split('@').length - 1 === 1) {
                if (email.endsWith('.') && email.length - email.indexOf('.') <= 4) {
                    for (let i = 0; i < email.length; i++) {
                        if (email[i] === ' ') {
                            k = 1;
                        } else if (isAlpha(email[i])) {
                            if (isUpper(email[i])) {
                                j = 1;
                            }
                        } else if (isDigit(email[i])) {
                            continue;
                        } else if (email[i] === '_' || email[i] === '.' || email[i] === '@') {
                            continue;
                        } else {
                            d = 1;
                        }
                    }

                    if (k === 1 || j === 1 || d === 1) {
                        console.log('WWWWRRRROOOONNGGGG EEEMMMAAAIIILLL');
                    } else {
                        console.log('RIGHT EMAIL!!!');
                    }
                } else {
                    console.log('WRONGGGGG!!!');
                }
            } else {
                console.log('Wrong Email 2');
            }
        } else {
            console.log('Wrong Email!!');
        }
    } else {
        console.log('Input valid email!!');
    }

    rl.close();
});

function isAlpha(char) {
    return /^[a-zA-Z]$/.test(char);
}

function isUpper(char) {
    return /^[A-Z]$/.test(char);
}

function isDigit(char) {
    return /^[0-9]$/.test(char);
}
