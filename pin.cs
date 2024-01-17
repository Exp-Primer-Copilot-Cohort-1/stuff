using System;

namespace EithanPinDemo
{
    /// <summary>
    /// A simple program to demonstrate PIN validation.
    /// </summary>
    class Program
    {
        /// <summary>
        /// The main entry point for the program.
        /// </summary>
        static void Main()
        {
            const string correctPin = "1111";
            Console.WriteLine("Please enter your pin: ");
            int attempts = 4;
            while (attempts > 0)
            {
                string input = Console.ReadLine();
                try
                {
                    bool valid = ValidatePinNumber(input, correctPin);
                    // We wouldn't get here if the pin isn't valid as we'd drop into the catch block, but adding an if anyway in case you added more logic...
                    if (valid)
                    {
                        Console.WriteLine("Security Check Passed");
                        return;
                    }
                }
                catch (InvalidPinException)
                {
                    Console.WriteLine($"Incorrect pin, you have {attempts} attempts left");
                    attempts--;
                }
            }
            Console.WriteLine("Locked Out.");
        }

        /// <summary>
        /// Validates a PIN number.
        /// </summary>
        /// <param name="input">The PIN input provided by the user.</param>
        /// <param name="correctAnswer">The correct PIN number to validate against.</param>
        /// <returns>true if the PIN is valid; otherwise, false.</returns>
        /// <exception cref="InvalidPinException">Thrown when the provided PIN is invalid.</exception>
        private static bool ValidatePinNumber(string input, string correctAnswer)
        {
            if (input == correctAnswer)
            {
                return true;
            }
            throw new InvalidPinException();
        }
    }

    /// <summary>
    /// Exception thrown when the provided PIN is invalid.
    /// </summary>
    public class InvalidPinException : Exception
    {
        public InvalidPinException() : base("Invalid pin number")
        {
        }
    }
}