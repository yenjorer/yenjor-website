# 图片替换指南

本文档详细说明每个占位图片的位置和应该替换的内容。

## 📍 图片替换清单

### 1. Hero 区域

| 位置 | 当前图片 | 建议替换内容 | 推荐尺寸 |
|------|----------|--------------|----------|
| Hero主图 | `picsum.photos/600/500?random=1` | 工厂生产场景或产品陈列图 | 1200x1000px |

---

### 2. About 区域

| 位置 | 当前图片 | 建议替换内容 | 推荐尺寸 |
|------|----------|--------------|----------|
| About主图 | `picsum.photos/600/500?random=2` | 工厂车间、产品展示室或团队合影 | 1200x1000px |

---

### 3. 产品展示区 (Products)

| 产品名称 | 当前图片 | 建议替换内容 | 推荐尺寸 |
|----------|----------|--------------|----------|
| Wooden Button | `picsum.photos/400/400?random=10` | 木质纽扣特写图 | 800x800px |
| Snap Button | `picsum.photos/400/400?random=11` | 四合扣/ snaps特写图 | 800x800px |
| Shell Button | `picsum.photos/400/400?random=12` | 贝壳纽扣特写图 | 800x800px |
| Resin Button | `picsum.photos/400/400?random=13` | 树脂纽扣特写图 | 800x800px |
| Jeans Button | `picsum.photos/400/400?random=14` | 牛仔裤纽扣/铆钉图 | 800x800px |
| Rivet | `picsum.photos/400/400?random=15` | 金属铆钉特写图 | 800x800px |
| Eyelet | `picsum.photos/400/400?random=16` | 鸡眼扣/气眼特写图 | 800x800px |
| Metal Buckle | `picsum.photos/400/400?random=17` | 金属扣特写图 | 800x800px |

---

### 4. 合作伙伴Logo区

| 位置 | 当前图片 | 建议替换内容 | 推荐尺寸 |
|------|----------|--------------|----------|
| Partner 1 | `picsum.photos/150/60?random=20` | 品牌Logo (如: ZARA, H&M, Nike等) | 200x80px |
| Partner 2 | `picsum.photos/150/60?random=21` | 品牌Logo | 200x80px |
| Partner 3 | `picsum.photos/150/60?random=22` | 品牌Logo | 200x80px |
| Partner 4 | `picsum.photos/150/60?random=23` | 品牌Logo | 200x80px |
| Partner 5 | `picsum.photos/150/60?random=24` | 品牌Logo | 200x80px |
| Partner 6 | `picsum.photos/150/60?random=25` | 品牌Logo | 200x80px |
| Partner 7 | `picsum.photos/150/60?random=26` | 品牌Logo | 200x80px |
| Partner 8 | `picsum.photos/150/60?random=27` | 品牌Logo | 200x80px |

---

### 5. 认证证书区

| 位置 | 当前图片 | 建议替换内容 | 推荐尺寸 |
|------|----------|--------------|----------|
| Certification 1 | `picsum.photos/120/80?random=30` | OEKO-TEX 证书 | 240x160px |
| Certification 2 | `picsum.photos/120/80?random=31` | ISO 9001 证书 | 240x160px |
| Certification 3 | `picsum.photos/120/80?random=32` | ISO 14001 证书 | 240x160px |
| Certification 4 | `picsum.photos/120/80?random=33` | SGS 证书 | 240x160px |
| Certification 5 | `picsum.photos/120/80?random=34` | CE 证书 | 240x160px |
| Certification 6 | `picsum.photos/120/80?random=35` | BSCI 证书 | 240x160px |

---

## 🖼️ 图片命名建议

```
images/
├── hero/
│   └── hero-main.jpg
├── about/
│   └── factory.jpg
├── products/
│   ├── wooden-button-1.jpg
│   ├── wooden-button-2.jpg
│   ├── snap-button-1.jpg
│   ├── snap-button-2.jpg
│   └── ...
├── partners/
│   ├── brand-1.png
│   ├── brand-2.png
│   └── ...
└── certifications/
    ├── oeko-tex.png
    ├── iso-9001.png
    └── ...
```

## 📐 图片格式要求

| 类型 | 格式 | 推荐尺寸 | 最大文件大小 |
|------|------|----------|--------------|
| 产品图 | JPG/PNG/WebP | 800x800px | 200KB |
| Logo | PNG (透明背景) | 200x80px | 50KB |
| 证书 | JPG/PNG | 400x300px | 100KB |
| Hero图 | JPG/WebP | 1920x1080px | 500KB |

## 💡 图片优化建议

1. **产品图**: 使用纯色背景（如白色），突出产品细节
2. **Logo**: 使用透明背景的PNG格式，确保在不同背景下都能正常显示
3. **Hero图**: 使用高质量但文件大小适中的图片，建议使用WebP格式
4. **压缩**: 上传前使用 TinyPNG 或 Squoosh 压缩图片

## 🔄 替换步骤

1. 准备好所有图片
2. 在 `index.html` 中搜索占位符注释（如 `<!-- [替换为：XXX] -->`）
3. 将图片路径替换为实际图片路径
4. 测试不同屏幕尺寸下的显示效果

---

> 💡 **提示**: 如果使用外部图片URL（如CDN），请确保URL可访问且图片已正确加载。
