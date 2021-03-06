# 正则表达式-文稿

大家好，本视频将介绍正则表达式的基本使用，正则表达式是对搜索和替换功能的扩展，允许使用者使用预先设定的搜索语法匹配给定文本中的字符串。目前如 C、C++、Java、Python、JavaScript 等主流语言均支持正则表达式。

因此，本视频将正则表达式作为一种独立的技术进行介绍，对于具体的语言，尽管其实现略有不同，但其核心思想都是相似的。

我将在该正则表达式在线解析网站进行正则表达式的测试，在此输入正则表达式，在此输入待匹配的文本，匹配信息就会在这里显示。下面我们进入正题。

之前已经提到，正则表达式是对普通搜索或替换功能的扩展，使用普通搜索功能时，我们必须完整的写出想要匹配的字符串，如假设搜索 abc，必须输入 abc，在编写代码时我们经常使用这种方式寻找方法名所在位置，但如果想要获取文本中出现的所有以 a 开头的字符串，普通搜索方式就显得力不从心了，而正则表达式可以解决这个问题，它在普通搜索功能的基础上，提供了基于模式的匹配。

下面我们打开 script.md 文件，在该文件中我总结了正则表达式的常用语法。

## 元字符

首先是元字符，其可以用来匹配单个字符。

首先是.(dot)字符，可以匹配任意字符，可以看到文本中的所有字符均被匹配。

\s 用于匹配空格。

\S 用于匹配非空格

\d 用于匹配阿拉伯数字

\D 用于匹配非阿拉伯数字

\w 用于匹配字母、数字或下划线

\W 用于匹配非字母、数字或下划线

\v 用于匹配纵向空白字符

\ 用于转义

## 字符组合

有了元字符，我们就可以组合元字符生成规则，如：

中括号表示匹配括号内的所有字符。

[abc]：匹配 a 或 b 或 c

[a-z]：匹配 a-z

上标表示逻辑非

[^abc]：匹配非 a 或 b 或 c

竖线表示逻辑或

a|b：匹配 a 或 b

## 数量词修饰

以上均为对单个字符的匹配，实际使用时，我们需要指定某个字符出现的次数，此时需要数量词修饰符

- \*：星号表示 0 个或多个
- ?：问号表示 0 个或 1 个
- \+：加号表示 1 个或多个
- {n}：若需要指定具体数量，可以使用大括号，{n}表示出现 n 次
- {a,b}：大括号内可以指定两个参数，表示起始数量和结束数量，若不指定第二个参数，则表示大于 a

## 其它

有时我们先准确匹配某个字符串的开始和结尾

- ^ 或 \A 用于匹配字符串的开始
- $ 或 \Z 用于匹配字符串的结尾

## 分组

小括号用于分组，分组的目的是便于获取每个组内的数据。

## 匹配模式

下面介绍匹配模式：

- g: 表示全局模式，会获取到文本内所有匹配的字符串
- m：表示多行模式，此时^和$会表示每行的开头和结尾
- i：表示不区分大小写
- s：表示单行模式，此时输入的文本会被当成一行处理
- u：表示支持 unicode 字符
- a：表示仅支持 ascii 字符

## 例子

### A. 电话

1. 134[0-9]{8} \g
2. ^134[0-9]{8}$ \gm

### B. 邮箱

^[a-zA-Z\.]+@[a-zA-Z0-9]+\.(com|net|edu.cn)$

### C. 经纬度

(\d{1,3}\.\d+),\v?\s\*(\d{1,3}\.\d+)
