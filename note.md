# Ubuntu系统中使用VSCode配置Python和C/C++环境学习笔记

## 语言配置
# Ubuntu安装中英文语言源过程

## 安装中文语言源

### 1. 打开语言支持设置
- 点击系统设置（Settings），然后选择“语言支持”（Language Support）。

### 2. 安装中文语言包
- 在“语言支持”窗口中，点击“安装/删除语言”（Install / Remove Languages）。
- 找到中文（简体），如果尚未安装，点击“安装”（Install）。

### 3. 设置系统语言
- 安装完成后，通过下拉菜单选择中文（简体）作为系统语言。

## 环境准备

### 1. 安装VSCode
- 下载地址：[Visual Studio Code官网](https://code.visualstudio.com/) 
- 安装命令：
  ```bash
  sudo dpkg -i <downloaded-filename>.deb
  sudo apt-get install -f # 安装依赖