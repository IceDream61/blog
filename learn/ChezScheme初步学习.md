# Chez Scheme初步学习

　　最近在学习用scheme做各种事情，选用的实现是chez scheme。

　　学习过程中，发现chez scheme的英文资料几乎没有，中文资料更是一篇都搜不到。

　　因此，记录一些经验分享给大家。

　　值得一提的是，本文的Scheme部分，是适用于任何一个Scheme实现的，而非单单为Chez Scheme而写。

## 前言

　　Scheme的语言标准简称R5RS，全称是“Revised5 Report on the Algorithmic Language Scheme”。

　　这个标准很短，只有不到五十页，中文翻译质量也挺高的，这是中文版PDF的百度文库链接。如果哪天失效了，可以发邮件找我要。

　　这里要普及一下，编程语言的“标准”只是规定了语言最基本的要求。而语言的“实现”才是编译器、解释器、各种库等等。你平时手里用的，比如gcc，就是语言的实现。实现一定要符合标准才能算这个语言，但可以在标准之外自己扩充很多东西。

　　据王垠所说，Chez Scheme是迄今为止速度最快的Scheme实现，这就是我选用它的原因，因为我个人喜欢速度快的。

　　然而，这是个收费的实现，其免费版称为Petite Chez Scheme，虽然功能都有，但调试功能大幅缩水，最明显的地方就是报错信息极其简约，真的是极其极其简约。有的时候，他只给你错误信息，连第几行出错了都不告诉你……所以，调试的工作，就要更多靠手动了。好在我平时也不写很大规模的工程，不怎么需要调试功能。等需要的时候，再考虑是买正常版还是换实现吧。

## 安装

　　这是Chez Scheme的官网。

　　最新版的Chez Scheme、Petite Chez Scheme、SWL（Scheme Widget Library）都在这里下载，自己选择对应的版本。然而，由于SWL暂时只支持32位、单线程的版本，所以我的做法是不管计算机的型号，直接安装32位、单线程的Petite Chez Scheme，然后再安装SWL即可。

　　当安装完成后，直接在命令行中输入petite、swl即可分别打开Petite Chez Scheme和SWL。

　　注1：官方说明我并没有读的太仔细，因此我并不能确定高级的版本（例如64位、多线程）能否在源码安装且配合一些安装参数（例如--64、--threads）的情况下，兼容SWL，有兴趣的读者自行尝试，也可以和我交流～

　　注2：我的机器是Mac，因此后面的所有实测内容都以Mac为准。不过，看起来Chez Scheme对于不同平台的支持还是挺到位的，应该基本一致。

## 简要目录

　　我的“Chez Scheme初步学习”主要内容有以下几部分：

　　　　1. Scheme部分

　　　　2. Chez Scheme部分

　　　　3. SWL部分

　　之所以如此分，是因为在我看来，掌握一门语言就是要掌握语言本身、语言实现以及相应的实用工具（库）。对应来说：

　　　　1. 掌握了Scheme部分，便可以比较顺畅地使用Scheme语言了

　　　　2. 掌握了Chez Scheme部分，就能顺畅地使用Chez Scheme这个实现了

　　　　3. 掌握了SWL部分，则可以使用Chez Scheme做平常想做的很多事情了

　　那么，话不多说，进入正文。

## Scheme部分

### Scheme部分——前言

　　首先，我先介绍Scheme部分。应当注意的是，虽然我是使用的Chez Scheme这个实现，但在这里介绍的内容不会超出R5RS标准的范围。

　　因此，这部分的内容，适用于任何一个Scheme实现，因为所有的Scheme实现都应该遵循R5RS标准。

### Scheme部分——语言特点

　　Scheme语言中，所有的代码都是S表达式。这种表达式，就是用一对小括号括起来的一个个元素，而每个元素又是一个S表达式。

　　可见，Scheme中所有的语句形式都是一样的。一般来说，S表达式的第一个元素是操作，而其余元素则是这个操作的参数。简单来说，就是前缀形势，例如：(+ 1 2 3) => 6。

　　按照惯例，本文也使用上面这个符号 “=>” 来表示一段代码及其计算结果。

### Scheme部分——变量、常见运算

　　大家来看这段代码：

``` scheme
                        ; 大家可以自己打开petite，依次输入看结果
(define x 123)
(define y (- 200 x))
x                       ; => 123
y                       ; => 77
(+ x y)                 ; => 200
(- 200 x y 10)          ; => -10

(set! x 10)
(set! y 20)
(> x y)                 ; => #f
(< x y 30 40 100)       ; => #t
```

　　上面的代码中，有变量的定义、使用、赋值、比较。

　　含义很显然，define是定义、set!是赋值，其余运算符就是各自的含义。顺带提一句，由于采用了前缀表达式，每个运算的操作数个数便不受限制了；由于一个小括号都不省略，因此也不需要考虑算符优先级问题了。

　　在Scheme中，会修改参数值的操作，结尾都有一个叹号（就像上面那样）。在Scheme中，这样的命名惯例还有一些，后面会依次见到。

### Scheme部分——顺序结构、分支结构（if语句）

　　大家来看这段代码：

``` scheme
                        ; 可以保存为control.scm，然后petite control.scm运行
(define x 2)
(display "猜数，范围[1,3]") (newline)
(if (= (read) x)
    (begin
      (display "猜对啦 ^.^") (newline))
    (begin
      (display "猜错了 -.-") (newline)))
(exit)
```

　　其中，display是打印、newline是换行、read是从标准输入端口读一个值。而最后的exit语句，则是表示运行结束。

　　以上这便是if语句和begin语句的例子了，其标准语句形式如下：

``` scheme
(if <判断条件> <then分支>)
(if <判断条件> <then分支> <else分支>)
(begin <语句1> ...)
```

　　大家看上面我给出的begin语句形式，里面的 “...” 表示后面还可以有随便几个和前一个参数相同形式的参数，也可以没有。也就是说，这样的一个形式代表以下这些形式：

``` scheme
(begin <语句1>)
(begin <语句1> <语句2>)
(begin <语句1> <语句2> <语句3>)
(begin <语句1> <语句2> <语句3> <语句4>)
                        ; 以此类推
```

　　这种三个点的表示方法，是Scheme的语言标准中写明的，在后面我们接触到Scheme的宏时还会遇到，这是可以写入Scheme代码的标准写法。

### Scheme部分——函数、分支结构（cond语句、case语句）

``` scheme
                        ; 可以保存为cc.scm，然后petite cc.scm运行
(define (display-ln str)
  (display str) (newline))

(define (run x)
  (cond
   ((> x 0) (display-ln "正整数"))
   ((= x 0) (display-ln "零"))
   (else (display-ln "负整数"))))

(display "写一个整数：")
(define x (read))
(if (integer? x)
    (run x)
    (display-ln "你写的不是整数"))

(display "写整数，范围[1,3]")
(case (read)
  (1 (display-ln "你写的是1"))
  (2 (display-ln "你写的是2"))
  (3 (display-ln "你写的是3"))
  (else (display-ln "你写的不是这个范围里的整数"))
(exit)
```

　　我在这里定义、使用了函数，使用了cond语句、case语句。它们的主要形式如下：

``` scheme
(define (<函数名> <参数1> ...)
  <语句1>
  ...)
                        ; 函数定义中，参数可以一个都没有
(cond
  (<条件1> <语句1>)
  ...
  (else <语句>))

(case
  (<值1> <语句1>)
  ...
  (else <语句>))
                        ; cond语句和case语句中
                        ; 1. else分支可以没有
                        ; 2. 内部的每一条“<语句>”，都只是一个语句
                        ;    如果想要在一个分支中执行多条语句
                        ;    你需要用begin语句来达到目的。
                        
```
