import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import user, dare


class TestBase(TestCase):

    def create_app(self):
            
        # pass in test configurations
        config_name = 'testing'
        
        app.config.update(SQLALCHEMY_DATABASE_URI=('mysql+pymysql://' + str(getenv('MYSQL_USER')) + ':' + str(getenv('MYSQL_PASSWORD')) + '@' + str(getenv('MYSQL_IP')) + '/' + str(getenv('MYSQL_DB_TESTS')))) 
        return app


    def setUp(self):
        """
        Will be called before every test
        """

        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin usersou
        admin = user(user_name="admin", email ="admin", dare="admin@admin.com")

        # create test non-admin user
        employee = User(first_name="test", last_name="user", email="test@user.com", password="test2016")
        
        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class ViewTest(TestBase):

    def test_homepage_view(self):
        response =self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
 

class ModelTest(TestBase):
    def test_user_model(self):
        user = User(first_name="yeet", last_name="yeet", email="yeet@gmail.com", password="yeet1")
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)

    def test_dare_model(self):
        event = Event(promoter="PVO", location ="london", date_posted = "02/1220:00",event_date = "02/1220:00")
        db.session.add(event)
        db.session.commmit()
        self.assertEqual(Event.query.count(), 1)

    def test_user_view(self):

        target_url= url_for('User', user_id=2)
        redirect_url = url_for('login', next=target_url)
        response = self.assertEqual(response.status_code,302)
        self.assertRedirects(response, reidrect_url)
