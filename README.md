# Yenjor Co., Ltd. - Static Website

一个专业的B2B外贸展示网站，基于纽扣和服装配件制造商的需求设计。

## 📁 项目结构

```
yenjor-website/
├── index.html          # 主页面（包含所有HTML, CSS, JS）
├── README.md           # 说明文档
└── IMAGE-GUIDE.md      # 图片替换指南
```

## 🚀 快速预览

### 本地预览
1. 直接在浏览器中打开 `index.html` 文件
2. 或使用 VS Code 的 Live Server 扩展

### 在线预览
使用以下任一平台：
- **GitHub Pages**: 上传整个 `yenjor-website` 文件夹到 GitHub 仓库，启用 Pages
- **Cloudflare Pages**: 连接 GitHub 仓库或直接上传
- **Netlify**: 拖拽 `yenjor-website` 文件夹到 Netlify Drop

## 📝 需要替换的内容

### 1. 联系信息
在 `index.html` 中搜索并替换以下内容：
- 公司名称: `Yenjor Co., Ltd.`
- 地址: `Jiashan, Zhejiang, China`
- 邮箱: `sales@yenjor.com`, `info@yenjor.com`
- 电话: `+86 573-XXXX-XXXX`

### 2. 产品图片
参见 `IMAGE-GUIDE.md` 获取详细的图片替换指南

### 3. 合作伙伴Logo
在 `index.html` 中搜索 `[替换为：品牌Logo图片]`，替换为实际的品牌Logo

### 4. 认证证书图片
在 `index.html` 中搜索 `[替换为：认证证书图片]`，替换为实际的认证证书图片

## 🎨 技术栈

- **HTML5**: 语义化结构
- **Tailwind CSS v3**: 通过 CDN 引入
- **Font Awesome 6**: 图标库
- **Vanilla JavaScript**: 交互功能
- **Google Fonts**: Inter 字体

## ✨ 功能特性

- ✅ 完全响应式设计（手机、平板、桌面）
- ✅ 现代化B2B外贸风格
- ✅ 平滑滚动动画
- ✅ 滚动显示动画
- ✅ 移动端汉堡菜单
- ✅ 联系表单（含提交动画）
- ✅ 返回顶部按钮
- ✅ 固定导航栏（滚动时变色）

## 📱 响应式断点

- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

## 🔧 自定义修改

### 修改配色
在 `<style>` 标签中找到 `tailwind.config`，修改 `colors` 部分：
```javascript
colors: {
    primary: '#1a1a1a',    // 主色（深灰/黑色）
    secondary: '#4a4a4a',  // 次要色
    accent: '#c9a227',     // 强调色（金色）
}
```

### 修改字体
更改 `<link>` 标签中的 Google Fonts URL

### 添加更多产品
在 Products 区域复制产品卡片结构，修改图片和文本

## 📄 许可证

MIT License - 可自由使用和修改

## 📞 技术支持

如有问题，请检查：
1. 图片路径是否正确
2. CDN 链接是否可访问
3. 浏览器是否支持 JavaScript
