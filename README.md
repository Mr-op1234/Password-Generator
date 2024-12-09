# Password-Generator
A simple yet effective password generator tool


Passwords are crucial parts of privacy as it grants and revokes the access to different accounts leading to our personal data. This Python project simply takes two inputs
- Your name or a unique number related to you
- A specific pnemonic that only you can remember.

With that information it generates a safe password and secure password following a sinple yet effective algorithm:
- if the input is a number then converts it to its 0. decinal form ( 5147 becomes 0.5147)
- if the input is a string or a name then converts the letters into its respective ACII code and does the above.
- adding the total length of the characters used in the first and the second output and stores it in a specific counter.
- now the new number (5147 now 0.5147) is converted into its hex code.
- since decimal hex codes are infinite the digit extraction will loop till it matches the value of counter.


  I have added the addition module for pyperclip that required installation if you're new to python. its not necessary so you may remove it from the code.

   Enjoy :))
