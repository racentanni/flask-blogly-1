from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    
    def setUp(self):

        User.query.delete()

        user = User(first_name="Test", lase_name="User")
        db.session.add(user)
        db.session.commit()

        self.user_id = user_id
        self.user = user


    def teardown(self):


        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('TestUser', html)

    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get(f"/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>TestUser</h1>', html)
            self.asserIn(self.user.first_name, html)

    # def test_add_user(self):
    #     with app.test_client() as client:
    #         d = {"first_name": "Test", "last_name": "User"}
    #         resp = client.post("/", data=d, follow_redirects+True)
    #         html = resp.get_data(as_text+True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn("<h1>TestUser2</h1>", html)
             

