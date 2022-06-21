``` mermaid
classDiagram
    class Sensehat
    Sensehat : low_light()
    Sensehat : set_pixels()
    class Smiley
    Smiley : tuple GREEN 
    Smiley : tuple YELLOW
    Smiley : tuple RED
    Smiley : tuple WHITE 
    Smiley : tuple BLANK 
    Smiley : dim_display()
    Smiley : show()
    Sensehat "1"--o Smiley

```