const { app, BrowserWindow } = require('electron');

function createWindow() {
  // Create the browser window
  let win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  });

  // Load your JavaScript file
  win.loadFile('index.html');

  // Open the DevTools (optional)
  // win.webContents.openDevTools()
}

// When Electron has finished initializing, create a new window
app.whenReady().then(createWindow);