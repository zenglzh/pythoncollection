pythoncollection
================

some python script

scripy
gensim
windows64 位 安装python 扩展包。
1、下载编译器 Microsoft Visual C++ Compiler for Python 2.7（包含32位和64位） 下载地址: http://aka.ms/vcpython27
2、安装完路径为：C:\Users\Administrator\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0
3、修改python安装目录下Lib\distutils\msvc9compiler.py文件
def get_build_version():
    """Return the version of MSVC that was used to build Python.
 
    For Python 2.3 and up, the version number is included in
    sys.version.  For earlier versions, assume the compiler is MSVC 6.
    """
    return 9.0
    prefix = "MSC v."
    ...
    
4、然后再找到find_vcvarsall方法直接返回vcvarsall.bat的路径
def find_vcvarsall(version):
    """Find the vcvarsall.bat file
 
    At first it tries to find the productdir of VS 2008 in the registry. If
    that fails it falls back to the VS90COMNTOOLS env var.
    """
    return r'C:\Users\Administrator\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0\vcvarsall.bat'
    vsbase = VS_BASE % version
    ...
5、运行 python setup.py install 安装相应的扩展包
6、也可以 建立一个windows的二进制包 ：python setup.py bdist_wininst
 