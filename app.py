from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory storage for notes
notes = {}
next_id = 1

@app.route('/notes', methods=['GET'])
def get_notes():
    """Return a list of all notes."""
    return jsonify(list(notes.values()))

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    """Return a specific note by ID."""
    note = notes.get(note_id)
    if note is None:
        abort(404)
    return jsonify(note)

@app.route('/notes', methods=['POST'])
def create_note():
    """Create a new note with a title and content."""
    global next_id
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        abort(400, description="Se requiere 'title' y 'content'")

    note = {
        'id': next_id,
        'title': data['title'],
        'content': data['content']
    }
    notes[next_id] = note
    next_id += 1
    return jsonify(note), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    """Update an existing note by ID."""
    note = notes.get(note_id)
    if note is None:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400)

    # Update the fields if provided, otherwise keep existing values
    note['title'] = data.get('title', note['title'])
    note['content'] = data.get('content', note['content'])
    return jsonify(note)

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Delete a note by ID."""
    note = notes.pop(note_id, None)
    if note is None:
        abort(404)
    return '', 204

if __name__ == '__main__':
    # Enable debug mode for development
    app.run(debug=True)
