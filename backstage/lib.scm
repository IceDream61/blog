(define (display-ln str)
  (display str) (newline))

(define-syntax swap
  (syntax-rules ()
    ((swap a b)
     (let ((tmp a))
       (set! a b)
       (set! b tmp)))))

(define-syntax string-append!
  (syntax-rules ()
    ((string-append! str str2 ...)
     (set! str (string-append str str2 ...)))))

(define list-have?
  (lambda (a-list a-element)
    (if (not (equal? a-list (list)))
	(if (equal? (car a-list) a-element)
	    #t
	    (list-have? (cdr a-list) a-element))
	#f)))

(define (read-with-display to-display)
  (display to-display)
  (read))

(define (read-all-from-port port)
  (define (read-all-iter port all)
    (define next (read-char port))
    (if (eof-object? next)
	all
	(read-all-iter port (string-append all (string next)))))
  (read-all-iter port ""))

(define (read-all-from-file file-name)
  (define port (open-input-file file-name))
  (define all (read-all-from-port port))
  (close-input-port port)
  all)

(define (display-to-file one file-name)
  (define port
    (begin
      (if (file-exists? file-name) (delete-file file-name))
      (open-output-file file-name)))
  (display one port)
  (close-output-port port))

(define-syntax list-add-if-not-exists!
  (syntax-rules ()
    ((list-add-if-not-exists! a-list a-element)
     (if (not (list-have? a-list a-element))
	 (set! a-list (cons a-element a-list))))))

(define (list-del a-list a-element)
  (define (list-not-empty-del a-list a-element)
    (define head (car a-list))
    (define tail (cdr a-list))
    (if (equal? head a-element)
	tail
	(cons head (list-not-empty-del tail a-element))))
  (if (equal? a-list '())
      '()
      (list-not-empty-del a-list a-element)))

(define-syntax list-del-if-exists!
  (syntax-rules ()
    ([list-del-if-exists! a-list a-element]
     (if (list-have? a-list a-element)
	 (set! a-list (list-del a-list a-element))))))

(define (string-find str sub)
  (let ([L (string-length str)]
	[l (string-length sub)])
    (do ([i 0 (+ i 1)]
	 [sites '()])
	((> (+ i l) L) (reverse sites))
      (if (equal? sub (substring str i (+ i l)))
	  (set! sites (cons i sites))))))
;(string-find "Hello world!" "l")

(define (string-replace str old-sub new-sub)
  (define l (string-length old-sub))
  (define (string-replace-one str sites)
    (if (equal? sites '())
	str
	(let* ([i (car sites)]
	       [others (cdr sites)]
	       [j (+ i l)]
	       [L (string-length str)])
	  ;(display "car sites=") (display i) (newline)
	  (string-append (substring str 0 i)
			 new-sub
			 (string-replace-one (substring str j L)
					     (map - others (make-list (length others) j)))))))
  ;(display "l=") (display l) (newline)
  (string-replace-one str (string-find str old-sub)))
(string-replace "Hello world!" "or" "[DYZ]")

(define (make-md-table table filename)
  (define md-table "")
  (define port
    (begin
      (if (file-exists? filename)
	  (delete-file filename))
      (open-output-file filename)))
  (define algorithm-list (car table))
  (define language-list (cadr table))
  (define code-list (caddr table))
  (define (make-title! title-list)
    (if (not (equal? title-list (list)))
	(begin
	  (string-append! md-table " " (car title-list) " |")
	  (make-title! (cdr title-list)))
	(string-append! md-table "\n")))
  (define (make-fgx!!! title-list)
    (if (not (equal? title-list (list)))
	(begin
	  (string-append! md-table " :---: |")
	  (make-fgx!!! (cdr title-list)))
	(string-append! md-table "\n")))
  (define (make-content! content-list)
    (define (make-code! algorithm title-list)
      (define (get-code-link code-name)
	(if (list-have? code-list code-name)
	    (string-append "[code](code/" code-name ".html)")
	    ""))
      (if (not (equal? title-list (list)))
	  (begin
	    (string-append! md-table " " (get-code-link (string-append algorithm "-" (car title-list))) " |")
	    (make-code! algorithm (cdr title-list)))
	  (begin
	    (string-append! md-table "\n"))))
    (if (not (equal? content-list (list)))
	(begin
	  (string-append! md-table "| " (car content-list) " |")
	  (make-code! (car content-list) language-list)
	  (make-content! (cdr content-list)))))
  (string-append! md-table "| Algorithm \\ Language |")
  (make-title! language-list)
  (string-append! md-table "| :---: |")
  (make-fgx!!! language-list)
  (make-content! algorithm-list)

  (display md-table port) (newline port)
  (close-output-port port)
  )
