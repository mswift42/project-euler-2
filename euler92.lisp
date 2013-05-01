(defun number-to-list (n)
  (map 'list #'digit-char-p (prin1-to-string n)))

(defun square-sum (n)
  (reduce #'+ (mapcar #'(lambda (x) (* x x)) (number-to-list n))))

(defun ends-in (n)
  (loop
       for x1 = (square-sum n) then (square-sum x1)
       when (or (= x1 89) (= x1 1))
       do (return (values x1))))

(defun result ()
  (loop
       for i from 2 to 10000000
       when (= (ends-in i) 89)
       counting i))
