from fastapi import FastAPI, Query
from middleware import setup_cors
from fastapi.responses import HTMLResponse
import math
import random
import requests



app = FastAPI()
setup_cors(app)


#Function to check if a value is even or odd
def even_or_odd(n: int) -> str:
    even_odd =  "even" if n % 2 == 0 else "odd"

    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    armstrong_sum = sum(digit ** power for digit in digits)

    if armstrong_sum == n:
        return f"armstrong, {even_odd}"
    else:
        return even_odd


# Checking if it is a prime number
def is_prime(n: int) -> bool:
    n = int(n)  # Ensure n is an integer
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Properly convert sqrt(n) to int
        if n % i == 0:
            return False
    return True



# Checking if the number is a perfect square
def is_perfect(n: int) -> bool:
    if math.sqrt(n).is_integer():
        return True
    else:
        return False


# def is_fibonacci(n: int) -> bool:
#     if n < 0:  # Fibonacci numbers cannot be negative
#         return False
#     return is_perfect(5 * n**2 + 4) or is_perfect(5 * n**2 - 4)





# Function to create the html page accept values


# Sum of the individual numbers input
def digit_sum(n: int) -> int:
    num_sum = 0
    for i in str(n):
        num_sum += int(i)
    return num_sum


def fun_fact_function(n: int) -> str:
    url = f"http://numbersapi.com/{n}"
    try:
        result = requests.get(url)

        if result.status_code == 200:
            fun_fact = result.text
            return fun_fact
        else:
            return None
    except requests.exceptions.RequestException:
        return None


@app.get("/", response_class=HTMLResponse)
def input_page():
    return """
    <form id="numForm" action="/api/classify-number" onsubmit="handleSubmit(event)">
        <label for="num">Enter a numerical value: </label>
        <input type="number" name="num" required>
        <button type="submit">Check</button>
    </form>
<script>
    async function handleSubmit(event) {
        event.preventDefault(); // Prevent automatic form submission
        
        const form = document.getElementById("numForm"); // Get the form element
        const numInput = document.querySelector("input[name='num']").value; // Get the input value

        if (!numInput) {
            alert("Please enter a valid number.");
            return;
        }
        
        try {
            const response = await fetch(`/api/classify-number?num=${numInput}`, {
                method: "GET",
            });
            
            if (!response.ok) {
                throw new Error("Network response was poor");
            }
            
            const data = await response.json();
            
            if (!data.fun_fact) {
                alert('There was an interference, please try again later');
                return; // Prevent form submission if fun_fact is null
            }
            
            // Only submit the form if fun_fact is not null
            form.submit(); 
            
        } catch (error) {
            alert("Check Your Network Connection");
        }    
    }
</script>

    """

# Displays the value given and the result from all functions
@app.get("/api/classify-number")
def number_facts(num: int = Query(..., description="The number to classify")):
    return{
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": [even_or_odd(num)],
        "digit_sum": digit_sum(num),
        "fun_fact": fun_fact_function(num)
    }
