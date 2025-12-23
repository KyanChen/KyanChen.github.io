source "https://rubygems.org"

# 1. 核心依赖：使用 GitHub Pages 官方套件
# 这会自动锁定 Jekyll 版本以及 jekyll-seo-tag, jekyll-sitemap 等常用插件的版本
gem "github-pages", group: :jekyll_plugins

# 2. 兼容性修复：Ruby 3.0+ 必须包含
# 如果你的电脑安装的是较新的 Ruby，没有这个无法运行 jekyll serve
gem "webrick"

# 3. Windows 系统适配 (如果你是用苹果或Linux，这部分会被忽略，不影响)
# 用于在 Windows 上能够正确监控文件变化和处理时区
group :jekyll_plugins do
  gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]
  gem "wdm", "~> 0.1.1", platforms: [:mingw, :mswin, :x64_mingw]
end
