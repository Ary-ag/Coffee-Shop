from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary to map coffee choices to their prices
coffee_prices = {
    1: 2.50,  # Espresso
    2: 3.00,  # Latte
    3: 3.50   # Cappuccino
}

@app.route('/order', methods=['POST'])
def order():
    # Get the choice of coffee from the request data
    choice = int(request.json['choice'])
    
    # Check if the choice is valid
    if choice in coffee_prices:
        # Calculate the price of the chosen coffee
        price = coffee_prices[choice]
        
        # Return a JSON response indicating success and the price of the coffee
        return jsonify({'status': 'success', 'message': f'You ordered coffee choice {choice}. The price is ${price}.'})
    else:
        # Return a JSON response indicating failure
        return jsonify({'status': 'error', 'message': 'Invalid coffee choice.'})

if __name__ == '__main__':
    app.run(debug=True)
