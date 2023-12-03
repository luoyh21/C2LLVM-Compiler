# Clong
前两个作业的test的代码需要修改，在写完示例后将其替代test.c中的文件.
translator 为第三次作业，项目布局为：antlr文件夹为生成的代码，只需使用，如修改语法树，修改.g4文件后重新生成antlr4 -v 4.7.2 -Dlanguage=Python3 clong.g4 -visitor即可。TargetCode中为示例代码。Analyses中，需要增加对错误的处理的额外py文件，主要为最底下的analyse函数，里面得到的tree是根本。使用了visitor模式，大部分函数都已经在类内写好了，根据示例代码补充内容即可。输入输出语句块起到栈的作用。