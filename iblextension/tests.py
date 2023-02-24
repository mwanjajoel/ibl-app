from django.test import TestCase
import pytest


# test creating a new greeting object
def test_greeting_creation():
    greeting = Greeting()
    greeting.save()
    assert greeting.pk == 1, "Should save an instance"

# test the string representation of the greeting object
def test_greeting_str():
    greeting = Greeting()
    greeting.save()
    assert str(greeting) == "Greeting object (1)", "Should be the string representation"

# test the __unicode__ representation of the greeting object
def test_greeting_unicode():
    greeting = Greeting()
    greeting.save()
    assert greeting.__unicode__() == "Greeting object (1)", "Should be the unicode representation"

# test the __repr__ representation of the greeting object
def test_greeting_repr():
    greeting = Greeting()
    greeting.save()
    assert greeting.__repr__() == "Greeting object (1)", "Should be the repr representation"

# test editing a greeting object
def test_greeting_edit():
    greeting = Greeting()
    greeting.save()
    greeting.greeting = "Hello"
    greeting.save()
    assert greeting.greeting == "Hello", "Should be able to edit the greeting"

# test deleting a greeting object
def test_greeting_delete():
    greeting = Greeting()
    greeting.save()
    greeting.delete()
    assert not Greeting.objects.filter(pk=1), "Should be able to delete the greeting"

# test the greeting view
def test_greeting_view(client):
    response = client.get('/greeting/')
    assert response.status_code == 200, "Should be able to get the greeting view"


