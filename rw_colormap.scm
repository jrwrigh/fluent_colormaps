(define (write-cmap fn)
  (let ((port (open-output-file (cx-expand-filename fn))) (cmap (cxgetvar 'def-cmap)))
    (write (cons cmap (cx-get-cmap cmap)) port)
    (newline port)
    (close-output-port port)))

(define (read-cmap fn)
  (if (file-exists? fn)
    (let ((cmap (read (open-input-file (cx-expand-filename fn)))))
        (cx-add-cmap (car cmap) (cons (length (cdr cmap)) (cdr cmap)))
        (cxsetvar 'def-cmap (car cmap)))
    (cx-error-dialog
    (format #f "Macro file ~s not found." fn))))

(define (ti-write-cmap)
  (let ((fn (read-filename "colormap filename" "cmap.scm")))
    (if (ok-to-overwrite? fn)
        (write-cmap fn))))

(define (ti-read-cmap)
  (read-cmap (read-filename "colormap filename" "cmap.scm")))

(ti-menu-insert-item!
  file-menu
  (make-menu-item "read-colormap" #t ti-read-cmap
  "Read a colormap from a file."))

(ti-menu-insert-item!
  file-menu
  (make-menu-item "write-colormap" #t ti-write-cmap
  "Write a colormap to a file."))