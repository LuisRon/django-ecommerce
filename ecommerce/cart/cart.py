class Cart():

    def __init__(self, request):

        self.session = request.session

        # Returning user, getting the existing session
        cart = self.session.get('session_key')

        # New user, generating session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart