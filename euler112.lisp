
(ql:quickload "lisp-unit") 
(defpackage :euler-112
  (:use :cl :lisp-unit))

(in-package :euler-112)


(lisp-unit:define-test test-nr-to-list
  (lisp-unit:assert-equal '(1 2 3) (number-to-list 123))
  (lisp-unit:assert-equal '(4 2 1) (number-to-list 421)))

(lisp-unit:define-test test-increasing-p
  (lisp-unit:assert-true (increasing-p '(2 4 5)))
  (lisp-unit:assert-true (increasing-p '(2 8 9)))
  (lisp-unit:assert-false (increasing-p '(3 4 5 2))))

(lisp-unit:define-test test-decreasing-p
  (lisp-unit:assert-true (decreasing-p '(5 3 2)))
  (lisp-unit:assert-true (decreasing-p '(9 8 1)))
  (lisp-unit:assert-false (decreasing-p '(9 7 2 4))))

(lisp-unit:define-test test-bouncy-p
  (lisp-unit:assert-true (bouncy-p '( 2 4 3)))
  (lisp-unit:assert-true (bouncy-p '( 4 3 5)))
  (lisp-unit:assert-false (bouncy-p '( 2 3 4))))


(defun number-to-list (num)
  (map 'list #'digit-char-p (prin1-to-string num)))

(defun increasing-p (lst)
  (cond
    ((null lst) t)
    ((null (rest lst)) t)
    (t (and (<= (first lst) (second lst))
	    (increasing-p (rest lst))))))

(defun decreasing-p (lst)
  (cond
    ((null lst) t)
    ((null (rest lst)) t)
    (t (and (>= (first lst) (second lst))
	    (decreasing-p (rest lst))))))

;; checking numbers recursively with incr and decr instead of
;; checking against the sorted lists nearly halves the running time.

(defun bouncy-p (lst)
  "Return if list is neither increasing nor decreasing."
  (and (not ( increasing-p lst))
       (not ( decreasing-p lst))))

(defun euler-112 ()
  "return ratio of bouncy to non bouncy numbers."
  (loop
     for i from 1
     counting (bouncy-p (number-to-list i)) into sumbouncy
     when (= 99 (* 100 (/ sumbouncy i)))
     return  i))


