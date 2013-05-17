(load "~/quicklisp/setup.lisp")
(ql:quickload "lisp-unit")


(defun readfile ()
  "open base-expt.text file and collect the lines of strings."
  (with-open-file (f "~/project-euler/base_exp.txt")
    (loop
	 for l = (read-line f nil 'eof)
	 until (eq l 'eof)
	 collect l)))

(defun string-list (string)
  "Build list with (base expt) for base_exp.txt
   Splits line by comma, converts to int."
  (loop
       for i = 0 then (1+ j)
       as j = (position #\, string :start i)
       collect (parse-integer (subseq string i j))
       while j))

(defun base-expt-list ()
  "map string-list function over string collection"
  (mapcar #'string-list (readfile)))

(defun linenumber (line)
  "Calculte exp * log base (log(a ^ x) == x * (log a))"
  (* (second line) (log (first line))))


(defun res ()
  (loop
       with max-i = 0 and max-x = 0
       for i in (base-expt-list)
       for j from 1 to 1000
       for m = (linenumber i)
       when (> m max-x)
       do (setf max-i j max-x m)
       finally (return (values max-i max-x))))


(lisp-unit:define-test test-length
  (lisp-unit:assert-equal 1000 (length (base-expt-list))))


