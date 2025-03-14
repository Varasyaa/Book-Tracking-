{% extends 'layout.html' %}

{% block content %}
  <h1 class="mt-5">{{ title }}</h1>
  <form method="post">
    <div class="form-group">
      <label for="title">Title</label>
      <input type="text" class="form-control" id="title" name="title" value="{{ book.title if book else '' }}" required>
    </div>
    <div class="form-group">
      <label for="author">Author</label>
      <input type="text" class="form-control" id="author" name="author" value="{{ book.author if book else '' }}" required>
    </div>
    <div class="form-group">
      <label for="status">Status</label>
      <select class="form-control" id="status" name="status" required>
        <option value="Want to Read" {{ 'selected' if book and book.status == 'Want to Read' else '' }}>Want to Read</option>
        <option value="Currently Reading" {{ 'selected' if book and book.status == 'Currently Reading' else '' }}>Currently Reading</option>
        <option value="Read" {{ 'selected' if book and book.status == 'Read' else '' }}>Read</option>
      </select>
    </div>
    <button type="submit" class="btn btn-primary">{{ button_text }}</button>
    <a href="{{ url_for('index') }}" class="btn btn-secondary">Cancel</a>
  </form>
{% endblock %}
