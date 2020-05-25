format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
fill        ::=  <any character>
align       ::=  "<" | ">" | "=" | "^"
sign        ::=  "+" | "-" | " "
width       ::=  integer
precision   ::=  integer
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"


Option  Meaning
'<'     Forces the field to be left-aligned within the available space (this is the default for most objects).
'>'     Forces the field to be right-aligned within the available space (this is the default for numbers).
'='     Forces the padding to be placed after the sign (if any) but before the digits.
        This is used for printing fields in the form ‘+000000120’.
        This alignment option is only valid for numeric types.
'^'     Forces the field to be centered within the available space.


Option  Meaning
'+'     indicates that a sign should be used for both positive as well as negative numbers.
'-'     indicates that a sign should be used only for negative numbers (this is the default behavior).
space   indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.


e.g.
'{:@=+30.2d}'.format(64.32)


Integer
'd' Decimal Integer. Outputs the number in base 10.
'n' Number. This is the same as 'd', except that it uses the current locale
    setting to insert the appropriate number separator characters.


float:
'e' Exponent notation. Prints the number in scientific notation using the letter ‘e’ to indicate
    the exponent. The default precision is 6.
'f' Fixed point. Displays the number as a fixed-point number. The default precision is 6.
'%' Percentage. Multiplies the number by 100 and displays in fixed ('f') format, followed by a percent sign.