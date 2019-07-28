from unittest import TestCase


class TestPeople(TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_speak(self):
        from practice.People import People
        p = People('test', 10, 50)
        self.assertEqual(10, p.age)
        self.assertEqual('未成年人', p.justPeopleType())
        TestCase.skipTest(self, 'aaa')
