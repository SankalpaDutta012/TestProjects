# npm install open
const open = require('open');
const process = require('process');

const URLS = {
    work: [
        "https://www.slack.com",
        "https://www.google.com",
        "https://www.10web.com",
        "https://docs.python.org/3/library/webbrowser.html"
    ],
    personal: [
        "https://www.youtube.com",
        "https://hianime.to",
        "https://www.github.com",
        "https://www.spotify.com"
    ]
};

function openWebpages(urls) {
    urls.forEach(url => open(url));
}

if (process.argv.length !== 3 || !URLS[process.argv[2]]) {
    console.log("Usage: node script.js <set_name>");
    console.log("Available sets:");
    for (const setName in URLS) {
        console.log(`- ${setName}`);
    }
    process.exit(1);
}

const setName = process.argv[2];
const urls = URLS[setName];
openWebpages(urls);
