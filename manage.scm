(define (ui-hello)
  (display "算法大全的后台代码") (newline)
  )

(define (print-line port)
  (display (read port)) (newline))

(define (test-one-line port)
  (define x (read port))
  (write x) (display " -> ") (write (eof-object? x)) (newline))

(define (test-one-char port)
  (define x (read-char port))
  (write x) (display " -> ") (write (eof-object? x)) (newline))

(define (peek-one-char port)
  (define x (peek-char port))
  (write x) (display " -> ") (write (eof-object? x)) (newline))

(define (read-table filename)
  (define port (open-input-file filename))
  (peek-one-char port)
  (peek-one-char port)
  (peek-one-char port)
  (peek-one-char port)
  (peek-one-char port)
  (peek-one-char port)
  ; read table from port
  (close-input-port port)
  ; return table
  )

(define (ui-work table)
  (newline)
  ; look and change this table
  ; at last, exit and return new table
  )

(define (write-table filename table)
  (define port (open-output-file filename))
  ; write table into port
  (close-output-port port)
  )

(define (ui-bye)
  (display "保存完毕，拜拜～") (newline)
  )

(begin
  (transcript-on "transcript.txt")
  (ui-hello)
  (define table (read-table "data.txt"))
;  (define new-table (ui-work table))
;  (write-table "data.txt" new-table)
  (ui-bye)
  (transcript-off)
  )

(exit)