(defun number-to-list (n)
  (map 'list #'digit-char-p (prin1-to-string n)))

(defun square-sum (n)
  (reduce #'+ (mapcar #'(lambda (x) (* x x)) (number-to-list n))))

(defparameter *ends-in-hash* (make-hash-table))

(defun init-hash ()
  (loop
       for i from 1 to 1000
       do ( setf ( gethash i *ends-in-hash*) (ends-in i))))

(defun ends-in (n)
  (loop
       for x1 = (or (gethash n *ends-in-hash*) (square-sum n))
                then (or (gethash x1 *ends-in-hash*) (square-sum x1))
       when (or (= x1 89) (= x1 1))
       do (return (values x1))))

(defun euler-92 ()
  (init-hash)
  (loop
       for i from 2 to 10000000
       when (= (ends-in i) 89)
       counting i))

