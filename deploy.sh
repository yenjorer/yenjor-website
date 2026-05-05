#!/bin/bash
# Yenjor Website - GitHub + Cloudflare Pages 自动化部署脚本

echo "=========================================="
echo "Yenjor Website 部署脚本"
echo "=========================================="

# 检查git远程是否已配置
if ! git remote get-url origin 2>/dev/null; then
    echo ""
    echo "⚠️  尚未配置GitHub远程仓库"
    echo ""
    echo "请先在GitHub上创建仓库，然后运行以下命令："
    echo ""
    echo "  git remote add origin https://github.com/yenjorer/yenjor-website.git"
    echo "  git branch -M main"
    echo "  git push -u origin main"
    echo ""
    exit 1
fi

# 推送到GitHub
echo ""
echo "📤 正在推送到GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 代码已成功推送到GitHub！"
    echo ""
    echo "=========================================="
    echo "下一步：在Cloudflare Pages配置部署"
    echo "=========================================="
    echo ""
    echo "1. 访问 https://dash.cloudflare.com/"
    echo "2. 进入 Workers & Pages → Create application"
    echo "3. 选择 Pages → Connect to Git"
    echo "4. 授权GitHub，选择仓库 yenjor-website"
    echo "5. 配置："
    echo "   - Project name: yenjor-website"
    echo "   - Production branch: main"
    echo "   - Build command: (留空)"
    echo "   - Build output directory: /"
    echo "6. 点击 Save and Deploy"
    echo ""
    echo "部署完成后，你的网站将可访问："
    echo "https://yenjor-website.pages.dev"
    echo ""
else
    echo ""
    echo "❌ 推送失败，请检查GitHub认证"
    exit 1
fi
