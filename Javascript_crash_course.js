// This is a comment that the computer will ignore.
/* This comment can span
multiple lines
without needing
to mark up every line */ 
"Gilad".length
"hello". substring(0, 2);   		-up to and excluding
str1.concat(str2)
string1.indexOf('fox')
lastIndexOf
string1.replace("brown", "orange")
string1.split(" ")
string1.substr(4, 11)
string1.substr(4) means 4 onward
toLowerCase
toUpperCase
str.search(pattern)
• returns index of first match or -1 if not found
False=undefined=null=0=Nan=""
"Great to see you," + " " + name
\t
\name\"
\'
\\




confirm("what the fuck is this?")    -  True/False
alert(productName);
prompt("hello, want this?")				- get value from user
console.log() will take whatever is inside the parentheses and log it to the console , like printing to screen

=== Equal to both value and type
== is equal to
&&
||
!== Not equal to


someNum.toFixed(num)	-shortens someNum to have only num decimal places
num.toExponential()
• converts num to expone­ntial notation (i.e. 5.569e+0)
num.toString()
• converts num to a string
num.toPrecision(#)
• converts num to a num with # places starting with whole numbers
String(someValue)
• converts or coerces someValue to a string - someValue can be any type, ie "­Boo­lea­n(1­)" returns true
parseInt(string, radix)
parseFloat(string, radix)



total += 5;
price *= uplift;
var my_number = number * 2;		- limits scope to within function, otherwise uses globalvar that is available
var myAge = 26
isNaN(3)
var myArray = new Array();
var myArray = ['Monday', 'Tuesday', 'Wednesday'];
myArray.length
concatjoin
toString
indexOf
lastIndexOf
slice
sort
splice

parseFloat() function parses a string and returns a floating-point number.
If the first character in the specified string is a number, it parses the string until it
reaches the end of that number, and returns the value as a number, not a strin
parseInt() is similar, but returns either an integer value or NaN.
 isFinite()
if ( ) {
    console.log( );
}
else if{
	
}
while(count > 0) {
sum = sum + count;
count--;
}

for(var x=0; x<10; x++) {
... execute these statements ...
continue
}
for (anItem in anObject) {
 ­ ­ ­ ­  doSome­thing With anItem; 
 ­ ­ ­ ­ ­ ­ ­ ­ // will be the key
 ­ ­ ­ ­  doSome­thi­ngWith Object­[an­Item];
 ­ ­ ­ ­ ­ ­  // will be the value of that key
 ­ ­ }
 
do {
... these statements ...
} while(this condition is true)

switch(color) {
case "red" :
message = "Stop!";
break;
case "yellow" :
message = "Pass with caution";
break;
default :
message = "Traffic light out of service. Pass only with great
care";
}


17 % 5 modulo


var divideByThree = function (number) {
    var val = number / 3;
    console.log(val);
	return val;
};




var mydate = new Date();
			new Date(milliseconds) //milliseconds since January 1st 1970
			new Date(dateString)
			new Date(year, month, day, hours, minutes, seconds, milliseconds)

var year = mydate.getFullYear(); // four-digit year e.g. 2012
var month = mydate.getMonth(); // month number 0 - 11; 0 is Jan, etc.
var date = mydate.getDate(); // day of the month 1 - 31
var day = mydate.getDay(); // day of the week 0 - 6; Sunday = 0, etc.
var hours = mydate.getHours(); // hours part of the time, 0 - 23
var minutes = mydate.getMinutes(); // minutes part of time, 0 - 59
var seconds = mydate.getSeconds(); // seconds part of time, 0 - 59
mydate.setDate(15)
mydate.toTimeString()
getUTCDate(),
setUTCMonth(), and so on). You can retrieve the difference between your
local time and UTC time by using the getTimezoneOffset()




Math.floor(myNum1)); // shows 12
alert(Math.ceil(myNum1)); // shows 13
alert(Math.round(myNum1)); // shows 13
alert(Math.round(myNum2))
Math.min()
Math.max()
Math.random()
Math.E
	.LN10
	.LN2
	LOG10E
	LOG2E
	PI
	SQRT1_2
	SQRT2
	
	
	
	
with (Math) {
var myRand = random();
var biggest = max(3,4,5);
var height = round(76.35);
}