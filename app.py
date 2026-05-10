from flask import Flask, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# 1. The Key to the Vault
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="postgres",
        user="postgres",
        password="mysecretpassword"
    )
    return conn

# 2. RUN ONCE: Build the table
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id SERIAL PRIMARY KEY,
            product_name VARCHAR(100),
            quantity INTEGER
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

init_db()

# 3. The Home Page
@app.route('/', methods=['GET', 'POST'])
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # IF THE USER CLICKED 'ADD'
    if request.method == 'POST':
        new_item = request.form['product_name']
        new_qty = request.form['quantity']
        cur.execute('INSERT INTO inventory (product_name, quantity) VALUES (%s, %s)', (new_item, new_qty))
        conn.commit()
        return redirect(url_for('home'))

    # Fetch all items
    cur.execute('SELECT * FROM inventory ORDER BY id DESC;')
    items = cur.fetchall()
    
    cur.close()
    conn.close()
    
    # 4. Build the HTML UI
    html = """
    <div style="font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; border: 1px solid #ccc; border-radius: 10px;">
        <h2>📦 Biznest Inventory System</h2>
        
        <form method="POST" action="/" style="margin-bottom: 20px; padding: 15px; background: #f9f9f9; border-radius: 5px;">
            <input type="text" name="product_name" placeholder="Item Name" required style="padding: 8px; width: 45%;">
            <input type="number" name="quantity" placeholder="Qty" required style="padding: 8px; width: 20%;">
            <button type="submit" style="padding: 8px 15px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">Add to Vault</button>
        </form>
        
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h3>Current Stock:</h3>
            <!-- HERE IS THE NEW DELETE BUTTON -->
            <form method="POST" action="/clear" style="margin: 0;">
                <button type="submit" style="padding: 8px 15px; background: #dc3545; color: white; border: none; border-radius: 4px; cursor: pointer;">🗑️ Clear All Stock</button>
            </form>
        </div>
        
        <ul style="list-style-type: none; padding: 0;">
    """
    
    if not items:
        html += "<p style='color: gray; font-style: italic;'>The vault is completely empty.</p>"
    else:
        for item in items:
            html += f"<li style='padding: 10px; border-bottom: 1px solid #eee;'><strong>{item[1]}</strong>: {item[2]} in stock</li>"
        
    html += "</ul></div>"
    return html

# 5. NEW ACTION: The "Clear Vault" Logic
@app.route('/clear', methods=['POST'])
def clear_database():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # This is the SQL command you learned!
    cur.execute('DELETE FROM inventory;')
    conn.commit()
    
    cur.close()
    conn.close()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)