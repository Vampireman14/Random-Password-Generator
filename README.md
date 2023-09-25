# Random-Password-Generator
Creates unique passwords featuring a combination of special characters, numbers, and both lowercase and uppercase letters.

Step-By-Step Explanation

Step 1: Import Necessary Libraries
*Import two libraries: random for generating random elements and string for accessing character sets (e.g., letters, digits, punctuation).

Step 2: Define a Function to Generate a Strong Password
*Define a function called generate_strong_password that takes a single argument, length, which represents the desired length of the password.
*Create a string called characters by concatenating sets of uppercase letters, lowercase letters, digits, and punctuation from the string module. This will be the pool of     characters from which the password will be generated.
*Start a while loop that continues until we generate a password that meets our criteria for strength.
*Inside the loop, we generate a password by selecting length random characters from the characters string and joining them together to form the password.
*We check if the generated password meets the criteria for a strong password. Specifically, we check if it contains at least one lowercase letter, one uppercase letter, one   digit, and one special character.
*If the password meets all the criteria, we exit the loop and return the generated strong password.

Step 3: Get User Input for Password Length
*We prompt the user to enter the desired length of the strong password and convert their input to an integer.

Step 4: Generate and Display the Strong Password
*We call the generate_strong_password function with the user-defined length to generate a strong password.
*Finally, we display the generated strong password to the user.
