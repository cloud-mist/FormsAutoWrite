# 1 功能
- 青年大学习 收集表单的自动填写(仅限 云大 计科专硕使用）
- 若其他专业需要用，需要找到你们专业学院的xpath进行替换。
- 若其他学校有类似收集， 也可自行修改适配你的情况。
# 2 前置条件
## 本机环境
- windows 11
- python 3.9.7 
- google-chrome 最新版(96.xxxx)
- go 1.17
## 首先你需要
- python & chrome最新版
- 安装一个库,在命令行执行`pip install selenium`
# 3 操作
0. 在`writeForm.py`中填写你的个人信息。将`二维码图片`放入yl文件夹，命名为`xuexi.jpeg`
1. 在`writeForm.py`取消注释掉带`提交按钮`的那一行代码, 这时运行即会提交.
2. 执行`QRcode2url.exe` 
3. 执行`writeForm.py`.执行完,会生成2个结果图片,看是否正常执行(假如你开启了无头模式)。



