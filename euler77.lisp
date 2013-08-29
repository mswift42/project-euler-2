;; Prime summations Problem 77 It is possible to write ten as the sum of
;; primes in exactly five different ways:

;; 7 + 3 5 + 5 5 + 3 + 2 3 + 3 + 2 + 2 2 + 2 + 2 + 2 + 2

;; What is the first value which can be written as the sum of primes in
;; over five thousand different ways?

(ql:quickload '(:fiveam))

(defpackage :euler77
  (:use :cl :fiveam))

(in-package :euler77)

;; this sounds suspiciously like the count-change problem,
;; so reusing that.

(defun count-change (amount coins)
    (let ((cache (make-array (list (1+ amount) (length coins))
			   :initial-element nil)))
    (macrolet ((h () `(aref cache n l)))
      (labels
	((recur (n coins &optional (l (1- (length coins))))
		(cond ((< l 0) 0)
		      ((< n 0) 0)
		      ((= n 0) 1)
		      (t (if (h) (h) ; cached
			   (setf (h) ; or not
				 (+ (recur (- n (car coins)) coins l)
				    (recur n (cdr coins) (1- l)))))))))
 
	;; enable next line if recursions too deep
	;(loop for i from 0 below amount do (recur i coins))
	(recur amount coins)))))


(defun sieve-of-eratosthenes (maximum)
  (let ((sieve (make-array (1+ maximum) :element-type 'bit
                                          :initial-element 0)))
    (loop for candidate from 2 to maximum
          when (zerop (bit sieve candidate))
            collect candidate
            and do (loop for composite from (expt candidate 2) 
                                         to maximum by candidate
                          do (setf (bit sieve composite) 1)))))

(defun euler-77 ()
  (loop
       for i from 11
       when (> (count-change i (sieve-of-eratosthenes 100)) 5000)
       return i)) 

(test test-count-change
  (is (= 242 (count-change 100 '(25 10 5 1)))))

(run!)
