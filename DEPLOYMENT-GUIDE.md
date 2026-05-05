# Yenjor Website - Cloudflare Pages 部署指南

## 快速部署步骤

### 方法一：使用 GitHub 连接到 Cloudflare Pages（推荐）

#### 步骤 1: 创建 GitHub 仓库并推送代码

```bash
# 进入项目目录
cd yenjor-website

# 添加远程仓库（请先在GitHub网页上创建空仓库 yenjor-website）
git remote add origin https://github.com/yenjorer/yenjor-website.git

# 推送代码到GitHub
git branch -M main
git push -u origin main
```

**在 GitHub 网页上创建仓库的步骤：**
1. 访问 https://github.com/new
2. Repository name: `yenjor-website`
3. Description: `Yenjor Co., Ltd. - Premium Button & Garment Accessories Manufacturer`
4. 选择 Private（私有）或 Public（公开）
5. 点击 "Create repository"
6. 按照页面上的命令推送代码

#### 步骤 2: 连接 Cloudflare Pages

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. 进入 **Workers & Pages** → **Create application**
3. 选择 **Pages** → **Connect to Git**
4. 授权 GitHub 访问
5. 选择仓库 `yenjorer/yenjor-website`
6. 配置构建设置：
   - **Project name**: `yenjor-website`
   - **Production branch**: `main`
   - **Build command**: （留空 - 纯静态站点）
   - **Build output directory**: `/` 或 `/` (根目录)
7. 点击 **Save and Deploy**

#### 步骤 3: 自定义域名（可选）

1. 在 Cloudflare Pages 项目设置中，选择 **Custom domains**
2. 添加你的域名（如 `www.yenjor.com`）
3. 按照指示配置 DNS

---

### 方法二：直接上传到 Cloudflare Pages

1. 访问 [Cloudflare Pages](https://pages.cloudflare.com/)
2. 点击 "Create a project"
3. 选择 "Direct upload"
4. 上传 `yenjor-website` 文件夹中的所有文件
5. 设置项目名称
6. 点击 "Deploy site"

---

## 部署后验证

### 1. 检查网站访问
访问 Cloudflare 提供的临时域名（如 `xxx.pages.dev`）

### 2. 验证图片加载
- 检查 banner 图片
- 检查产品图片（树脂扣、金属扣、牛仔扣等）
- 检查 logo 显示

### 3. 响应式测试
- 桌面端显示
- 平板/手机端导航菜单

---

## 预期访问地址

部署成功后，你的网站将可以通过以下地址访问：

**Cloudflare Pages 临时域名：**
```
https://yenjor-website.pages.dev
```

**自定义域名（如果你配置了）：**
```
https://www.yenjorer.com (或你配置的域名)
```

---

## 文件结构确认

```
yenjor-website/
├── index.html          # 主页面
├── README.md           # 项目说明
├── IMAGE-GUIDE.md      # 图片替换指南
├── logo.png            # Logo
├── images/             # 产品图片目录
│   ├── banner.jpg
│   ├── factory.jpg
│   ├── jeans-button.jpg
│   ├── resin-button.jpg
│   ├── metal-button.jpg
│   ├── horn-button.jpg
│   ├── shell-button.jpg
│   ├── wooden-button.jpg
│   ├── snap-button.jpg
│   ├── rivet.jpg
│   ├── eyelet.jpg
│   ├── metal-buckle.jpg
│   └── logo-new.png
└── public/             # Cloudflare 重定向规则
    └── _redirects
```

---

## 注意事项

1. **首次部署**：Cloudflare Pages 首次部署可能需要 1-2 分钟
2. **自动部署**：连接 GitHub 后，每次推送到 main 分支会自动部署
3. **HTTPS**：Cloudflare Pages 自动提供免费 SSL 证书
4. **CDN**：全球 CDN 加速，访问速度快
