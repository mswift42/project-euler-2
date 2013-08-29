;; Counting fractions in a range
;; Problem 73 Consider the fraction, n/d, where n and d are positive
;; integers.  If n<d and HCF(n,d)=1, it is called a reduced proper
;; fraction.  If we list the set of reduced proper fractions for d ≤ 8 in
;; ascending order of size, we get:

;; 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
;; 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

;; It can be seen that there are 3 fractions between 1/3 and 1/2.

;; How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
;; proper fractions for d ≤ 12,000?

(ql:quickload "fiveam")

(defpackage :euler73
  (:use :cl :fiveam))

(in-package :euler73)

(defun limit-p (n d)
  "test if fraction is between 1/3 and 1/2 and by
   including gcd-test for 1 exclude duplicates."
  (let ((frac (/ n d)))
    (and (< frac (/ 1 2))
	 (> frac (/ 1 3))
	  (= 1 (gcd n d)))))

 (defun count-fractions ()
   (loop
	for n from 1 to 6000
	collect (loop for d from 1 to 12000
		     counting (limit-p n d))))

(defun euler-73 ()
  (reduce #'+ (count-fractions)))


(test test-limit-p
  (is-true (limit-p 3 8))
  (is-true (limit-p 2 5))
  (is-true (limit-p 3 7))
  (is-true (limit-p 99 200))
  (is-true (limit-p 1001 3000))
  (is-false (limit-p 1 3))
  (is-false (limit-p 6 16)))

(fiveam:run!)
