<p align="center">
<img src=https://img.shields.io/github/stars/SyntX34/PH-DL?style=for-the-badge&logo=appveyor&color=blue />
<img src=https://img.shields.io/github/forks/SyntX34/PH-DL?style=for-the-badge&logo=appveyor&color=blue />
<img src=https://img.shields.io/github/issues/SyntX34/PH-DL?style=for-the-badge&logo=appveyor&color=informational />
<img src=https://img.shields.io/github/issues-pr/SyntX34/PH-DL?style=for-the-badge&logo=appveyor&color=informational />
</p>
<br />
<p align="center">
  <a href="https://github.com/SyntX34/PH-DL">
    <img src="assets/logo.png" alt="Logo" width="150" height="150">
  </a>

  <h3 align="center">PH-DL</h3>

  <p align="center">
    A powerful script to download and manage videos and pictures with ease.
    <br />
    <a href="https://github.com/SyntX34/PH-DL/releases">Download Latest Release</a>
    <br />
    <br />
    <a href="https://github.com/SyntX34/PH-DL/issues">Report Bug</a>
    ·
    <a href="https://github.com/SyntX34/PH-DL/issues">Request Feature</a>
  </p>
</p><details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
    </li>
    <li>
      <a href="#known-issues">Known Issues</a>
    </li>
    <li>
      <a href="#roadmap">Roadmap</a>
    </li>
    <li>
      <a href="#contributing">Contributing</a>
    </li>
    <li>
      <a href="#licence">License</a>
    </li>
    <li>
      <a href="#contact">Contact</a>
    </li>
  </ol>
</details>

## About The Project

<img src="assets/screenshot1.png" alt="Screenshot of PH-DL">

PH-DL is a command-line tool that allows you to download videos and images from supported websites. It provides an organized system for managing your downloads with categories.

### Features

- **Video Downloads**: Download videos with automatic format selection
- **Image/Album Downloads**: Download individual images or entire albums
- **Category Management**: Organize downloads into custom categories
- **Notifications**: Get desktop notifications when downloads complete
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Auto-Update**: Automatically updates yt-dlp for the latest site support

### Built With

*On initial launch, the script will automatically prompt you to install required packages*
* [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Video extraction and downloading
* [Requests](https://github.com/psf/requests) - HTTP library
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - HTML parsing
* [pynotifier](https://github.com/YuriyLisovskiy/pynotifier) - Desktop notifications

## Getting Started

### Option 1: Download Pre-built Binaries (Recommended)

Download the latest release for your operating system from the [Releases page](https://github.com/SyntX34/PH-DL/releases).

- **Windows**: Download `PH_Downloader.exe` and run it directly
- **Linux**: Download `PH_Downloader`, make it executable (`chmod +x PH_Downloader`), and run it
- **macOS**: Download `PH_Downloader`, make it executable (`chmod +x PH_Downloader`), and run it

### Option 2: Run from Source

#### Prerequisites
- Python 3.8 or higher ([Download Python](https://www.python.org/downloads/))

#### Installation
1. Clone the repository
   ```sh
   git clone https://github.com/SyntX34/PH-DL.git
   cd PH-DL
   ```

2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application
   ```sh
   python main.py
   ```

The script will automatically install any missing dependencies on first run.

## Usage

1. Run the application using one of the methods above
2. Select an option from the main menu:
   - `[1] Download Video` - Enter a video URL to download
   - `[2] Download album or picture` - Enter an image/album URL
   - `[3] Shuffle / Unshuffle videos` - Manage video playback order
   - `[4] Manage categories` - Create and organize download categories
   - `[5] Exit`
3. After downloading, you'll be prompted to organize the file into a category

### Video URL Format
```
https://www.pornhub.com/view_video.php?viewkey=xxxxxxxxxx
```

### Image/Album URLs
- Album: `https://www.pornhub.com/album/12345678`
- Picture: `https://www.pornhub.com/photo/123456789`

## Known Issues

### HTTP 410 Error
If you encounter an `HTTP Error 410: Gone` error, this indicates the video may have been removed or the site's structure has changed. The application will automatically attempt to update yt-dlp to the latest version which often resolves these issues. If the problem persists:

1. The video may have been deleted from the source
2. Try updating yt-dlp manually: `pip install --upgrade yt-dlp`
3. Check the [yt-dlp issues page](https://github.com/yt-dlp/yt-dlp/issues) for known problems

## Roadmap

See the [open issues](https://github.com/SyntX34/PH-DL/issues) for a list of proposed features and known issues.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Licence

Copyright © 2021 Drillenissen#4268 - logicguy.mailandcontact@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contact

Project Link: [https://github.com/SyntX34/PH-DL](https://github.com/SyntX34/PH-DL)

Original Author: Drillenissen#4268 - logicguy.mailandcontact@gmail.com
