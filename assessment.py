"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    1) Abstraction:
    2) Polymorphism:
    3) Compartmentalization/Bundling: 

2. What is a class?
    
    A class is

3. What is an instance attribute?

    An instance attribute is a 

4. What is a method?

    A method is a function that lives with a class and is accessible to all of the class's subclasses.

5. What is an instance in object orientation?

    An instance is

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute belongs to a class, whereas an instance attribute lives on each object instantiated from a class. 

   That means that if you decide to instantiate a class with a particular instance attribute (or even add the instance attribute after instantiation), each instance will have a unique place in memory for its instance attribute. A thousand instances means a thousand instance attributes (assuming you initiate the object with the attribute).

    With a class attribute, the attribute lives with the class, so all instances of the class will have access to the attribute, but the attribute will only live in one place in memory, with the class.

    If you expect all or most of the instances of a class to have the same attribute, like all the members of a dog class having the species 'dog,' you'd want to use a class attribute. That way you don't have many places in memory storing the same information.

    If you expect the instances to need unique attributes, like a person's name or a credit card number, an instance attribute would make more sense.


"""


# Part 2
class Student(object):
    """A student class, takes a first name, last name, and address as arguments.
    """
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """A question class, takes a question and a correct answer as arguments.
    """
    def __init__(self, question, answer):
        self.question = question
        self.correct_answer = answer

class Exam(object):
    """An exam class, takes an exam name as an argument.
    """
    def __init__(self, name):
        self.name = name
        self.questions = []

