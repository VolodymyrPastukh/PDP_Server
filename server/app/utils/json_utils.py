from flask import jsonify

def success_response(result=None, message=None):
    if result == None and message == None:
        return jsonify({'success': True})
    elif result == None:
        return jsonify({'success': True, 'message': message})
    elif message == None:
        return jsonify({'success': True, 'result': result})

    return jsonify({'success': True, 'message': message, 'result': result})

def failure_response(message):
    return jsonify({'success': False, 'message': message})

def error_response(message):
    return jsonify({'message': message})
