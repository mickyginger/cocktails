from index import app, db
from models.User import User
from models.Cocktail import Cocktail
from models.Comment import Comment

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User({
        'username': 'mickyginger',
        'email': 'mike.hayden@ga.co',
        'password': 'password'
    })
    user.save()

    mojito = Cocktail({
        'name': 'Mojito',
        'image': 'https://images.britcdn.com/wp-content/uploads/2015/05/Mason-Jar-Mojitos-feature.jpg',
        'ingredients': [
            { 'name': 'White rum', 'amount': '50ml' },
            { 'name': 'Gomme syrup', 'amount': '1 tsp' },
            { 'name': 'Lime', 'amount': '1/2' },
            { 'name': 'Mint', 'amount': 'Handful' },
            { 'name': 'Soda', 'amount': 'Dash' }
        ],
        'method': 'Muddle rum, lime, mint and gomme syrub. Add crushed ice. Top with soda, and stir.',
        'about': 'Traditionally, a mojito is a cocktail that consists of five ingredients: white rum, sugar (traditionally sugar cane juice), lime juice, soda water, and mint. Its combination of sweetness, citrus, and mint flavors is intended to complement the rum, and has made the mojito a popular summer drink. The cocktail has a relatively low alcohol content (about 10% alcohol by volume).',
        'user_id': user.id
    })
    mojito.save()

    comment = Comment({
        'content': 'Mmmmmojito',
        'user_id': user.id,
        'cocktail_id': mojito.id
    })
    comment.save()

    print('Database successfully seeded')
