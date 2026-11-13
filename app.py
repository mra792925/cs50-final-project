from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('store.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # جلب جميع القطع من قاعدة البيانات
    parts = conn.execute('SELECT * FROM parts').fetchall()
    conn.close()
    return render_template('index.html', parts=parts)

@app.route('/buy', methods=['POST'])
def buy():
    part_id = request.form.get('part_id')

    conn = get_db_connection()
    # التحقق من توفر القطعة وخصم 1 من المخزون
    part = conn.execute('SELECT * FROM parts WHERE id = ?', (part_id,)).fetchone()

    if part and part['stock'] > 0:
        # تقليل المخزون بواقع قطعة واحدة
        conn.execute('UPDATE parts SET stock = stock - 1 WHERE id = ?', (part_id,))
        # تسجيل الطلب
        conn.execute('INSERT INTO orders (part_id, buyer_name) VALUES (?, ?)', (part_id, 'زمُّور / زبون متجر'))
        conn.commit()

    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
