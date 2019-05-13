@echo off 

echo: 当前盘符和路径：

rd /s /Q %~dp0
echo :按任意键退出 & pause exit