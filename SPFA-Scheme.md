# Algorithm：SPFA
# Language：Scheme

``` scheme
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;;  题目：单源最短路，输入数据给定
;;
;;  作者：卢奇
;;  学号：5130309680
;;  邮箱：icedream@sjtu.edu.cn
;;
;;  算法：SPFA（简化版）
;;
;;  代码结构：共三大部分——
;;    开始是一些语法糖，
;;    然后是SPFA算法的实现，
;;    最后是主体部分，调用了SPFA算法并输出结果。
;;
;;  备注：代码备注共有两种——
;;    1. 代码的三大部分，各自开头有一段备注
;;    2. 代码的两个主体部分，内部穿插了一些备注
;;      其中，两个主体部分是指：代码主体部分 以及 SPFA算法的主体部分（即SPFA函数）
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(begin

  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ;;
  ;;  这里是为后面代码定义的一些语法糖。
  ;;
  ;;  为了可读性，我做了一个“下标变换”：
  ;;    题目图中6个点，存储为0~5，但供操作的API对外设计成1~6的假象，简化思路
  ;;
  ;;  有一维数组、二维数组、队列和逻辑运算几方面，具体如下所示：
  ;;    1. 根据下标该值，构造新数组：change, change2
  ;;    2. 根据下标赋值（＋下标变换）：set, set2
  ;;    3. 根据下标取值（＋下标变换）：get, get2
  ;;    4. 入队、出队：push, pop
  ;;    5. 逻辑运算（二元与、二元或）：and, or
  ;;
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

  (define (change a i x)
    (if (eqv? i 0)
	(cons x (cdr a))
	(cons (car a) (change (cdr a) (- i 1) x))))
  (define (change2 a i j x)
    (if (eqv? i 0)
	(cons (change (car a) j x) (cdr a))
	(cons (car a) (change2 (cdr a) (- i 1) j x))))
  (define-syntax set
    (syntax-rules ()
      ([set a i x] (set! a (change a (- i 1) x)))))
  (define-syntax set2
    (syntax-rules ()
      ([set2 a i j x]
       (begin
	 (set! a (change2 a (- i 1) (- j 1) x))
	 (set! a (change2 a (- j 1) (- i 1) x))))))
  (define-syntax get
    (syntax-rules ()
      ([get a i] (list-ref a (- i 1)))))
  (define-syntax get2
    (syntax-rules ()
      ([get2 a i j] (list-ref (list-ref a (- i 1)) (- j 1)))))
  
  (define-syntax push
    (syntax-rules ()
      ([push Q x] (set! Q (append Q (list x))))))
  (define-syntax pop
    (syntax-rules ()
      ([pop Q]
       (let ([x (car Q)])
	 (set! Q (cdr Q))
	 x))))

  (define-syntax and
    (syntax-rules ()
      ([and Ea Eb]
       (if (eqv? Ea #t)
	   (if (eqv? Eb #t) #t #f)
	   #f))))
  (define-syntax or
    (syntax-rules ()
      ([or Ea Eb]
       (if (eqv? Ea #t)
	   #t
	   (if (eqv? Eb #t) #t #f)))))
  
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ;;
  ;;  此为SPFA算法部分（简化版）
  ;;
  ;;  其中SPFA函数是主体，其调用了update-all函数，后者又调用了update函数。
  ;;
  ;;  注：之所以称之为简化版，是因为本来SPFA的入队应该去重的，但被我给省了。
  ;;     不过本题中并不要求速度、也不影响正确性，写不写也就无所谓了。
  ;;
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  
  (define (update map d Q u allv)
    (cond
     [(not (eqv? allv null))
      (let ([v (car allv)] [lastv (cdr allv)])
;	(newline)
;	(display "an update --") (newline)
;	(display "d: ") (display d) (newline)
;	(display "Q: ") (display Q) (newline)
;	(display "u: ") (display u) (newline)
;	(display "v: ") (display v) (newline)
;	(display "allv: ") (display allv) (newline)
	(cond
	 [(and (not (eqv? (get2 map u v) #f)) (or (eqv? (get d v) #f) (< (+ (get d u) (get2 map u v)) (get d v))))
	  (begin
	    (set d v (+ (get d u) (get2 map u v)))
	    (push Q v))])
	(update map d Q u lastv))]
     [else (list d Q)]))
  
  (define (update-all map d Q)
    (if (eqv? Q null)
	d
	(let ([u (pop Q)])
	  (define tmp  (update map d Q u (list 1 2 3 4 5 6)))
	  (set! d (car tmp))
	  (set! Q (cadr tmp))
	  (update-all map d Q))))

  (define (SPFA map s)
					; 初始化SPFA中的数组
    (define d (make-list 6 #f))
    (set d s 0)
    (define Q null)
    (push Q s)
					; 输出初始化的数组，仅供调试
    (display "d: ") (display d) (newline)
    (display "Q: ") (display Q) (newline)
					; 计算由s出发的单源最短路，并返回计算出的结果
    (update-all map d Q))

  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ;;
  ;;  题目主函数在此
  ;;
  ;;  本题所有的IO都在这里给出了，一目了然。
  ;;
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

					; 建图 称为map
  (define map (make-list 6 (make-list 6 #f)))
  (set2 map 1 2 7)
  (set2 map 1 3 9)
  (set2 map 1 6 14)
  (set2 map 2 4 15)
  (set2 map 2 3 10)
  (set2 map 3 4 11)
  (set2 map 3 6 2)
  (set2 map 4 5 6)
  (set2 map 5 6 9)
					; 通过简化的SPFA算法计算最短路
  (define d (SPFA map 1))
					; 输出答案
  (display "last-d: ") (display d) (newline)
  (display "result: ") (display (get d 5)) (newline))

```