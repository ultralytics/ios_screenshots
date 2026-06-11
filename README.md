<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 📘 Introduction

Welcome to the `ios_screenshots` software repository developed by Ultralytics! This tool is open-source and 🔄 freely redistributable under the [AGPL-3.0 license](https://opensource.org/license/agpl-v3). We encourage the use and adaptation of our tools and welcome contributions to our projects. For more details on the exciting work we do at Ultralytics, including advancements in [computer vision](https://www.ultralytics.com/glossary/computer-vision-cv) and AI, please visit us at [https://www.ultralytics.com](https://www.ultralytics.com/).

[![Ultralytics Actions](https://github.com/ultralytics/ios_screenshots/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/ios_screenshots/actions/workflows/format.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

# 📝 Description

The [Ultralytics ios_screenshots repository](https://github.com/ultralytics/ios_screenshots) is an automated tool designed to simplify the workflow for [iOS](https://docs.ultralytics.com/hub/app/ios/) developers. By resizing screenshot images to selected [Apple App Store screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/), this tool saves time and helps maintain visual consistency across your app listings. The defaults in `screenshots.py` generate `5_5`, `5_8`, `6_5`, and `12_9` output sizes; update the `formats`, `size_x`, and `size_y` lists if your App Store Connect submission requires newer device classes. For a practical demonstration, take a look at the iSky app created by Ultralytics, as seen below.

<p align="center">
  <a href="https://itunes.apple.com/app/id1445737240">
    <img src="https://user-images.githubusercontent.com/26833433/50044365-9b22ac00-0082-11e9-862f-e77aee7aa7b0.png" width="180" alt="iSky App Icon">
  </a>
</p>

Below is an example of a beautifully resized image that's ready for the App Store:
<img src="https://user-images.githubusercontent.com/26833433/50044338-5eef4b80-0082-11e9-9b2f-e989d7fa5c1c.jpg" width="100%" alt="Resized App Store Screenshot Example">

# 🛠️ Requirements

To use the `ios_screenshots` tool, you'll need [Python](https://www.python.org/) version 3.7 or later installed on your system. Additionally, the following package is required, which can be easily installed using [pip](https://pip.pypa.io/en/stable/) and the provided `requirements.txt` file:

```bash
# Install dependencies
pip3 install -U -r requirements.txt

# Included packages:
# opencv-python: Crucial for image manipulation tasks.
# pillow: Used by screenshots.py to save resized JPEG outputs.
```

You can find more information about [opencv-python](https://pypi.org/project/opencv-python/) and [Pillow](https://pypi.org/project/pillow/) on PyPI. For a general guide on setting up Python environments, check out the Ultralytics [Conda Quickstart Guide](https://docs.ultralytics.com/guides/conda-quickstart/).

# 🤝 Contribute

We actively welcome contributions from the community! Whether you're fixing bugs, adding new features, or improving documentation, your input is invaluable. Please take a look at our [Contributing Guide](https://docs.ultralytics.com/help/contributing/) to get started. We'd also love to hear about your experience using Ultralytics software; please consider filling out our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A huge 🙏 **thank you** to all our contributors!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ios_screenshots/graphs/contributors)

# ©️ License

Ultralytics offers two licensing options to accommodate different use cases:

- **AGPL-3.0 License**: This [OSI-approved](https://opensource.org/license/agpl-v3) open-source license is ideal for students and enthusiasts, promoting open collaboration and knowledge sharing. See the [LICENSE](https://github.com/ultralytics/ios_screenshots/blob/main/LICENSE) file for full details.
- **Enterprise License**: Designed for commercial applications, this license permits the integration of Ultralytics software and AI models into commercial products and services without the open-source requirements of AGPL-3.0. If your project requires an Enterprise License, please contact us via [Ultralytics Licensing](https://www.ultralytics.com/license).

# 📬 Contact Us

If you encounter any bugs or have feature requests, please report them on [GitHub Issues](https://github.com/ultralytics/ios_screenshots/issues). For broader questions and discussions about this project or other Ultralytics initiatives, join our vibrant community on [Discord](https://discord.com/invite/ultralytics)!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
