# npm install -g yt-dlp
const { exec } = require('child_process');

// Get the YouTube link from the command-line arguments
const link = process.argv[2];

if (!link) {
  console.error('Please provide a YouTube link.');
  process.exit(1);
}

// Function to execute the yt-dlp command and handle the output
const runYtDlp = (command, callback) => {
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Stderr: ${stderr}`);
      return;
    }
    callback(stdout);
  });
};

// Extract video information
runYtDlp(`yt-dlp --dump-json ${link}`, (output) => {
  const info = JSON.parse(output);
  const videoTitle = info.title;
  const videoViews = info.view_count;

  console.log("Title:", videoTitle);
  console.log("Views:", videoViews);

  // Download the video in the best format
  runYtDlp(`yt-dlp -f best ${link}`, (output) => {
    console.log("Download complete!");
  });
});
