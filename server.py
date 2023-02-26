from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'harukiinharu'


def get_db_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_conn()
    post = conn.execute('select * from posts where id = ?',
                        (post_id,)).fetchone()
    return post


@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_not_found.html')


@app.route('/')
def index():
    conn = get_db_conn()
    posts = conn.execute(
        'select * from posts order by created desc').fetchall()
    if len(posts) == 0:
        flash('博主还没更新。。。')
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post:
        return render_template('post.html', post=post)
    else:
        return render_template('page_not_found.html')


@app.route('/posts/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('标题不能为空')
        elif not content:
            flash('内容不能为空')
        else:
            conn = get_db_conn()
            conn.execute(
                'insert into posts (title, content) values (?, ?)', (title, content))
            conn.commit()
            conn.close()
            flash('发布成功')
            return redirect(url_for('index'))
    return render_template('new.html')


@app.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
def edit(post_id):
    return render_template('page_not_found.html')
    post = get_post(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('标题不能为空')
        elif not content:
            flash('内容不能为空')
        else:
            conn = get_db_conn()
            conn.execute(
                'update posts set title = ?, created = (datetime("now", "localtime")), content = ? where id = ?',
                (title, content, post_id))
            conn.commit()
            conn.close()
            flash('发布成功')
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)


@app.route('/posts/<int:post_id>/delete', methods=['GET', 'POST'])
def delete(post_id):
    return render_template('page_not_found.html')
    conn = get_db_conn()
    conn.execute('delete from posts where id = ?', (post_id,))
    conn.commit()
    conn.close()
    flash('删除成功')
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5001, True)
