# KyanChen.github.io

[![Update Profile](https://github.com/KyanChen/KyanChen.github.io/actions/workflows/update_profile.yml/badge.svg)](https://github.com/KyanChen/KyanChen.github.io/actions/workflows/update_profile.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the source code for [Keyan Chen's personal website](https://kyanchen.github.io), built with [Jekyll](https://jekyllrb.com/).

## Features

- **Academic Profile**: Tailored for researchers and academics to showcase publications, news, and biography.
- **Automated Updates**: Includes GitHub Actions workflows to automatically update the profile and fetch data.
- **Responsive Design**: Optimized for viewing on various devices.
- **Integrated Data**: Easy management of publications, news, and profile info via YAML data files.

## Usage


### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KyanChen/KyanChen.github.io.git
   cd KyanChen.github.io
   ```

2. Setup data:
   ```bash
   cp -r _data_samples _data
   ```
   > [!IMPORTANT]
   > You must rename `_data_samples` to `_data` and modify the data in `_data` to your own information.


3. Generate Favicon:
   Use [RealFaviconGenerator](https://realfavicongenerator.net/) to generate your favicon.
   - Upload your image (at least 260x260 px).
   - Configure the settings and generate.
   - Download the package, unzip it, and place the files in the directory of `assets/favicon`.


4. Install dependencies:
   ```bash
   conda create -n jekyll python=3.13 -y
   conda activate jekyll
   conda install ruby -y
   
   # check gem version
   gem -v
   # if there is no gem, install it first, from https://rubygems.org/pages/download, then run
   conda install compilers make
   bundle install
   ```

### Local Development

To serve the website locally:

```bash
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`.

## Customization

### Configuration

Edit `_config.yml` to update site-wide settings such as title, description, email, and social links.

### Content

- **Profile**: Update `_data/profile.yml` with your biography and personal details.
- **News**: Add new items to `_data/news.yml`.
- **Publications**: Manage your publication list in `_data/publications.yml`.
- **Pages**: Modify markdown files in `_pages/` to change page content.







## FAQ

**Q: What if the page styles are not loading correctly?**

If the page loading is incorrect, try turning off CDN acceleration and cache, and open the page in a new incognito window or use "Ctrl + F5" for Windows or "Cmd + Shift + R" for Mac.

**Q: What if error occurs when running `bundle install`?**

If error `bigdecimal` occurs when running `bundle install`, try running `conda install compilers make` first.



## License

This project is open source and available under the [MIT License](LICENSE).

---

&copy; 2025 Keyan Chen.
