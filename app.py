from flask import Flask, request, jsonify
from scrape_product_info import ScrapeProductInfo

app = Flask(__name__)
scrape_product_info = ScrapeProductInfo()

@app.route('/get_product_info', methods=['POST'])
def get_product_info():
    data = request.get_json()
    try:
        product_url = data['product_url']
    except KeyError:
        return jsonify({'error': 'Invalid input. Missing product_url parameter.'}), 400

    output = scrape_product_info.identify_platform(product_url)
    return jsonify({'product_title': output[0], 'product_mrp': output[1]})
