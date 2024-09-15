from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

faqs = [
    {
        'id': 1,
        'title': 'How is Tangerine healthy?',
        'description': 'Tangerines are a great health booster due to their high vitamin C content, which supports the immune system and skin health.',
        'image': 'https://www.halegroves.com/blog/wp-content/uploads/2016/12/order-floridda-tangerines-online-081816.jpg',
    },
    {
        'id': 2,
        'title': 'How is Apple healthy?',
        'description': 'Apples are rich in fiber and antioxidants, which help improve heart health and reduce the risk of cancer and diabetes.',
        'image': 'https://tse3.mm.bing.net/th?id=OIP.-4RJk-TNzc0Ulbu6-Ogx_AHaFR&pid=Api&P=0&h=180'
    }
]

@app.route('/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs)

@app.route('/faqs/<int:faq_id>', methods=['GET'])
def get_faq(faq_id):
    faq = next((faq for faq in faqs if faq['id'] == faq_id), None)
    if faq is None:
        return jsonify({'error': 'FAQ not found'}), 404
    return jsonify(faq)

@app.route('/faqs', methods=['POST'])
def create_faq():
    new_faq = request.get_json()
    new_faq['id'] = len(faqs) + 1  
    faqs.append(new_faq)
    return jsonify(new_faq), 201

@app.route('/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    faq = next((faq for faq in faqs if faq['id'] == faq_id), None)
    if faq is None:
        return jsonify({'error': 'FAQ not found'}), 404

    updated_data = request.get_json()
    faq.update(updated_data)  
    return jsonify(faq)


@app.route('/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    global faqs
    faqs = [faq for faq in faqs if faq['id'] != faq_id]
    return jsonify({'message': 'FAQ deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000,debug=True)


